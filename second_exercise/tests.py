import re
import shopify
import sys
import os
from unittest import TestCase
from pyactiveresource.activeresource import ActiveResource
from pyactiveresource.testing import http_fake
from second_exercise.shopify_feat import api_call_with_retry, api_iterator
from unittest.mock import patch
from second_exercise.exceptions import (
    ClientErrorException,
    NotFoundException,
    ProductResourceException,
    UnAuthorizedException,
)


class TestShopifyProduct(TestCase):
    def setUp(self):
        ActiveResource.site = None
        ActiveResource.headers = None

        shopify.ShopifyResource.clear_session()
        shopify.ShopifyResource.site = "https://this-is-my-test-show.myshopify.com/admin/api/unstable"
        shopify.ShopifyResource.password = None
        shopify.ShopifyResource.user = None

        http_fake.initialize()
        self.http = http_fake.TestHandler
        self.http.set_response(Exception("Bad request"))
        self.http.site = "https://this-is-my-test-show.myshopify.com"

    def load_fixture(self, name, format="json"):
        with open(os.path.dirname(__file__) + "/fixtures/%s.%s" % (name, format), "rb") as f:
            return f.read()

    def fake(self, endpoint, **kwargs):
        body = kwargs.pop("body", None) or self.load_fixture(endpoint)
        format = kwargs.pop("format", "json")
        method = kwargs.pop("method", "GET")
        prefix = kwargs.pop("prefix", "/admin/api/unstable")

        if "extension" in kwargs and not kwargs["extension"]:
            extension = ""
        else:
            extension = ".%s" % (kwargs.pop("extension", "json"))

        url = "https://this-is-my-test-show.myshopify.com%s/%s%s" % (prefix, endpoint, extension)
        try:
            url = kwargs["url"]
        except KeyError:
            pass

        headers = {}
        if kwargs.pop("has_user_agent", True):
            userAgent = "ShopifyPythonAPI/%s Python/%s" % (shopify.VERSION, sys.version.split(" ", 1)[0])
            headers["User-agent"] = userAgent

        try:
            headers.update(kwargs["headers"])
        except KeyError:
            pass

        code = kwargs.pop("code", 200)
        self.http.respond_to(
            method, url, headers, body=body, code=code, response_headers=kwargs.pop("response_headers", None)
        )

    def test_api_call_retry(self):
        self.fake("products/632910392", body=self.load_fixture("product"))

        product = api_call_with_retry(shopify.Product.find, 632910392)
        self.assertEqual(product.title, 'IPod Nano - 8GB')

        # test errors
        # 404
        self.fake("products/632910391", body=self.load_fixture("product"), code=404)
        with self.assertRaises(NotFoundException):
            product = api_call_with_retry(shopify.Product.find, 632910391)

        # 401
        self.fake("products/632910391", body=self.load_fixture("product"), code=401)
        with self.assertRaises(UnAuthorizedException):
            product = api_call_with_retry(shopify.Product.find, 632910391)

        # test a general client error
        self.fake("products/632910391", body=self.load_fixture("product"), code=400)
        with self.assertRaises(ClientErrorException):
            product = api_call_with_retry(shopify.Product.find, 632910391)

        # 5xx
        self.fake("products/632910391", body=self.load_fixture("product"), code=500)
        with self.assertRaises(ProductResourceException):
            product = api_call_with_retry(shopify.Product.find, 632910391)

        # test retry after 429
        self.fake(
            "products/632910391", body=self.load_fixture("product"), code=429, response_headers={'Retry-After': 1}
        )
        with self.assertRaises(ClientErrorException):
            with patch('time.sleep', return_value=None) as patch_sleep:
                product = api_call_with_retry(shopify.Product.find, 632910391)
        # call count shound be equal to retry num
        self.assertEqual(patch_sleep.call_count, int(os.getenv('RETRY_NUM', 5)))

    def test_api_iterator(self):
        response_header = {
            "Link": '<https://able-test1.myshopify.com/admin/api/2021-07/products.json?limit=250&page_info=kk>; rel="previous", <https://able-test1.myshopify.com/admin/api/2021-07/products.json?limit=250&page_info=jj>; rel="bbb"'
        }
        self.fake(
            "products.json?limit=250",
            extension=False,
            method="GET",
            body=self.load_fixture("product"),
            response_headers=response_header,
        )

        product = api_iterator(shopify.Product)
        self.assertEqual(len(product), 1)
