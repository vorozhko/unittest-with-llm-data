""" Generating test data for domain model testing with LLM """

from typing import List
import unittest
from datetime import datetime
from mirascope import llm
from pydantic import BaseModel, Field, field_validator


class Electronics(BaseModel):
    """ Domain model for Electronics """
    model: str
    brand: str
    category: str
    price: float = Field(gt=0, description="Price must be greater than 0")
    release_date: str  # ISO 8601 format (e.g., "2023-01-01")

    @field_validator("release_date", mode="after")
    @classmethod
    def validate_release_date(cls, value):
        """ Ensure release_date is in the past """
        release_date = datetime.fromisoformat(value)
        if release_date > datetime.now():
            raise ValueError("release_date must be in the past")
        return value


@llm.call(provider="openai", model="gpt-4o", response_model=List[Electronics])
def list_electronics(limit: int) -> List[Electronics]:
    """ Generate N items of products defined as Electronics """
    return f"Generate {limit} number of electronic products"


class TestElectronics(unittest.TestCase):
    """ Test class using LLM to generate domain data """

    @classmethod
    def setUpClass(cls):
        """ Generating test data once """
        cls._products = list_electronics(5)

    def test_model_is_string(self):
        """ Test product model field is string """
        for product in self._products:
            self.assertIsInstance(product.model, str)

    def test_price_is_positive(self):
        """ Test product price field is positive """
        for product in self._products:
            self.assertGreater(product.price, 0)

    def test_release_date_is_valid(self):
        """ Test product release_date is in the past """
        for product in self._products:
            release_date = datetime.fromisoformat(product.release_date)
            self.assertLessEqual(release_date, datetime.now())

    def test_unique_models(self):
        """ Test product models are unique """
        models = [product.model for product in self._products]
        self.assertEqual(len(models), len(set(models)))


if __name__ == '__main__':
    unittest.main()
