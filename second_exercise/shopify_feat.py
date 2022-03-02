import os
import time
from typing import Any
from urllib.error import HTTPError
from dotenv import load_dotenv

import shopify
from second_exercise.exceptions import NotFoundException, ProductResourceException, UnAuthorizedException, UnprocessableEntityException, ForbiddenException
from pyactiveresource.connection import ResourceNotFound, ServerError, ResourceInvalid, UnauthorizedAccess, ForbiddenAccess, ClientError

load_dotenv()
API_KEY = os.getenv('API_KEY')
PASSWORD = os.getenv('PASSWORD')

shop_url = f"https://{API_KEY}:{PASSWORD}@able-test1.myshopify.com/admin/api/2021-07"
shopify.ShopifyResource.set_site(shop_url)


# Print info from the first product
# api_product = shopify.Product.count()
# print(shopify.ShopifyResource.connection.response.code)
# print(api_product)
# print(api_product.title)
# print(api_product.to_dict())

# # Retrive the first couple product variants
# for api_variant in shopify.Variant.find(limit=5):
#     print(api_variant)



def api_call_with_retry(api_product: Any, product_id: int, **kwargs: Any) -> Any:
    retry_count = 0
    num_of_tries = int(os.getenv('RETRY_NUM', 5))
    while retry_count < num_of_tries:
        try:
            product = api_product(product_id, **kwargs)
            return product
        except ResourceNotFound as e:
            raise NotFoundException(e)
        except ServerError as e:
            raise ProductResourceException(e)
        except ResourceInvalid as e:
            raise UnprocessableEntityException(e)
        except ForbiddenAccess as e:
            raise ForbiddenException(e)
        except UnauthorizedAccess as e:
            raise UnAuthorizedException(e)
        except ClientError as e:
            response = shopify.ShopifyResource.connection.response
            if response.code == 429:
                # get the seconds to retry
                retry_after = response.headers['Retry-After']
                # sleep
                time.sleep(float(retry_after))
                retry_count+=1
                continue
    else:
        raise ClientError(response.msg)

# print(api_call_with_retry(shopify.Product.find, 4459014226001))




# for i in range(100):
#     print(shopify.Variant.find(30111927631953))
