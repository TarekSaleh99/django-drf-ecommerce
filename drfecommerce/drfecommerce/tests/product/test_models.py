import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:

    def Test_str_method(self, category_factory):
        # Arrange
        # Act
        x = category_factory()
        # Assert
        assert x.__str__() == 'test_category'


class TestBrandModel:
    def Test_str_method(self, brand_factory):
        # Arrange
        # Act
        obj = brand_factory()
        # Assert
        assert obj.__str__() == 'test_brand'


class TestProductModel:
    def Test_str_method(self, product_factory):
        # Arrange
        # Act
        obj = product_factory(name='test_product')
        # Assert
        assert obj.__str__() == 'test_product'