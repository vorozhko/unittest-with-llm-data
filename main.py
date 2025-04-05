""" Generating dummy test data for domain model tests """

from typing import List
import unittest
from mirascope import llm
from pydantic import BaseModel

class Electronics(BaseModel):
    """ Domain model for Electonics """
    model: str
    price: float



@llm.call(provider="openai", model="gpt-4o", response_model=List[Electronics])
def list_electronics(limit:int) -> List[Electronics]:
    """ Generate N items of products defined as Electronics """
    return f"Generate {limit} number of electronic products"


class TestProductMethods(unittest.TestCase):
    """ Test class using LLM to generate domain data """

    def setUp(self):
        """ Generating test data once """
        self._products = list_electronics(5)

    def test_model_is_string(self):
        """ Test product model field is string """
        for product in self._products:
            self.assertIsInstance(product.model, str)

    def test_price_is_float(self):
        """ Test product price field is float """
        for product in self._products:
            self.assertIsInstance(product.price, float)


if __name__ == '__main__':
    unittest.main()
