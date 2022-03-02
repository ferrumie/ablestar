import os
import time
from typing import Any, List
from dotenv import load_dotenv

import shopify
from second_exercise.exceptions import (
    ClientErrorException,
    NotFoundException,
    ProductResourceException,
    UnAuthorizedException,
    UnprocessableEntityException,
    ForbiddenException,
)
from pyactiveresource.connection import (
    ResourceNotFound,
    ServerError,
    ResourceInvalid,
    UnauthorizedAccess,
    ForbiddenAccess,
    ClientError,
)

load_dotenv()
API_KEY = os.getenv('API_KEY')
PASSWORD = os.getenv('PASSWORD')

shop_url = f"https://{API_KEY}:{PASSWORD}@able-test1.myshopify.com/admin/api/2021-07"
shopify.ShopifyResource.set_site(shop_url)


def api_call_with_retry(api_product: shopify.Product.find, product_id: int = None, **kwargs: Any) -> Any:
    """This calls shopify Product.find() and retry if rate limit is hit"""
    retry_count = 0
    num_of_tries = int(os.getenv('RETRY_NUM', 5))
    while retry_count < num_of_tries:
        try:
            if product_id:
                product = api_product(product_id, **kwargs)
            else:
                product = api_product(**kwargs)
            return product
        except ResourceNotFound as e:
            # 404
            raise NotFoundException(e)
        except ServerError as e:
            # 5xx
            raise ProductResourceException(e)
        except ResourceInvalid as e:
            # 422
            raise UnprocessableEntityException(e)
        except ForbiddenAccess as e:
            # 403
            raise ForbiddenException(e)
        except UnauthorizedAccess as e:
            # 401
            raise UnAuthorizedException(e)
        except ClientError as e:
            # 4xx
            response = shopify.ShopifyResource.connection.response
            if response.code == 429:
                # get the seconds to retry
                retry_after = response.headers['Retry-After']
                # sleep
                time.sleep(float(retry_after))
                retry_count += 1
                continue
            else:
                raise ClientErrorException(e)
    else:
        raise ClientErrorException(response.msg)


def api_iterator(product_function: shopify.Product, **kwargs: Any) -> List:
    page_info = ''
    products = []
    while True:
        products.extend(api_call_with_retry(product_function.find, limit=250, page_info=page_info))
        cursor = shopify.ShopifyResource.connection.response.headers.get('Link')
        if cursor and 'next' in cursor:
            page_info = cursor.split(';')[-2].strip('<>').split('page_info=')[1]
        else:
            break
    return products

