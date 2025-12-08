"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

@pytest.fixture
def calc():
    return Calculator()

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_too_large_values(self):
        """Test adding values that exceed the maximum limit."""
        calc = Calculator()
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(1000001, 1)
        assert "outside the valid range " in str(exc_info.value)

    def test_add_too_small_values(self):
        """Test adding values that exceed the minimum limit."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(-1000001, -1)
    
    def test_add_too_large_values_for_b(self, calc):
        """Test adding values where the second argument exceeds the limit."""
        with pytest.raises(InvalidInputException):
            calc.add(1, 1000001)

    def test_add_too_small_values_for_b(self, calc):
        """Test adding values where the second argument exceeds the minimum limit."""
        with pytest.raises(InvalidInputException):
            calc.add(1, -1000001)

    def test_add_max_boundary_value(self, calc):
        """Test adding the exact max value"""
        # Arrange
        a = 1000000
        b = 1
        expected = 1000001

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected
    
    def test_add_min_boundary_value(self, calc):
        """Test adding the exact min value"""
        # Arrange
        a = -1000000
        b = 1
        expected = -999999

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected
    
    def test_subtract_negative_numbers(self, calc):
        """Test subtracting two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected
    
    def test_subtract_too_large_values(self):
        """Test subtracting values that exceed the maximum limit."""
        calc = Calculator()
        with pytest.raises(InvalidInputException) as exc_info:
            calc.subtract(1000001, 1)
        assert "outside the valid range " in str(exc_info.value)

    def test_subtract_too_small_values(self):
        """Test subtracting values that exceed the minimum limit."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(-1000001, -1)
    
    def test_subtract_too_large_values_for_b(self, calc):
        """Test subtracting values where the second argument exceeds the limit."""
        with pytest.raises(InvalidInputException):
            calc.subtract(1, 1000001)

    def test_subtract_too_small_values_for_b(self, calc):
        """Test subtracting values where the second argument exceeds the minimum limit."""
        with pytest.raises(InvalidInputException):
            calc.subtract(1, -1000001)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self,calc):
        """Test multiplying positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected
    
    def test_multiply_too_large_values(self):
        """Test multiplying values that exceed the maximum limit."""
        calc = Calculator()
        with pytest.raises(InvalidInputException) as exc_info:
            calc.multiply(1000001, 1)
        assert "outside the valid range " in str(exc_info.value)

    def test_multiply_too_small_values(self):
        """Test multiplying values that exceed the minimum limit."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(-1000001, -1)
    
    def test_multiply_too_large_values_for_b(self, calc):
        """Test multiplying values where the second argument exceeds the limit."""
        with pytest.raises(InvalidInputException):
            calc.multiply(1, 1000001)

    def test_multiply_too_small_values_for_b(self, calc):
        """Test multiplying values where the second argument exceeds the minimum limit."""
        with pytest.raises(InvalidInputException):
            calc.multiply(1, -1000001)


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # Arrange
        a = 6
        b = 3
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_by_zero(self, calc):
        """Test dividing by zero."""
        with pytest.raises(ValueError) as exc_info:
            calc.divide(10, 0)
        assert "Cannot divide by zero" in str(exc_info)
    
    def test_divide_too_large_values(self):
        """Test dividing values that exceed the maximum limit."""
        calc = Calculator()
        with pytest.raises(InvalidInputException) as exc_info:
            calc.divide(1000001, 1)
        assert "outside the valid range " in str(exc_info.value)

    def test_divide_too_small_values(self):
        """Test dividing values that exceed the minimum limit."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(-1000001, -1)
    
    def test_divide_too_large_values_for_b(self, calc):
        """Test dividing values where the second argument exceeds the limit."""
        with pytest.raises(InvalidInputException):
            calc.divide(1, 1000001)

    def test_divide_too_small_values_for_b(self, calc):
        """Test dividing values where the second argument exceeds the minimum limit."""
        with pytest.raises(InvalidInputException):
            calc.divide(1, -1000001)