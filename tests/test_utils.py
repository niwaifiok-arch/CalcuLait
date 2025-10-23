"""Unit tests for utils.py functions."""
import pytest
from src.utils import add, subtract


class TestAdd:
    """Test cases for add function."""
    
    def test_add_two_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
    
    def test_add_multiple_numbers(self):
        """Test adding multiple numbers."""
        assert add(1, 2, 3, 4, 5) == 15
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-5, -10) == -15
    
    def test_add_mixed_numbers(self):
        """Test adding mix of positive and negative."""
        assert add(10, -5, 3) == 8
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(1.5, 2.5, 3.0) == 7.0
    
    def test_add_single_number(self):
        """Test adding single number."""
        assert add(42) == 42
    
    def test_add_no_arguments(self):
        """Test adding with no arguments returns 0."""
        assert add() == 0
    
    def test_add_zero(self):
        """Test adding with zeros."""
        assert add(0, 0, 0) == 0
    
    def test_add_large_numbers(self):
        """Test adding large numbers."""
        assert add(1000000, 2000000) == 3000000
    
    def test_add_non_numeric_raises_error(self):
        """Test that non-numeric input raises TypeError."""
        with pytest.raises(TypeError):
            add(1, "2", 3)
    
    def test_add_none_raises_error(self):
        """Test that None input raises TypeError."""
        with pytest.raises(TypeError):
            add(1, None, 3)


class TestSubtract:
    """Test cases for subtract function."""
    
    def test_subtract_two_numbers(self):
        """Test subtracting two numbers."""
        assert subtract(10, 3) == 7
    
    def test_subtract_multiple_numbers(self):
        """Test subtracting multiple numbers."""
        assert subtract(100, 20, 10, 5) == 65
    
    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative."""
        assert subtract(5, 10) == -5
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(10, -5) == 15
    
    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        result = subtract(10.5, 2.5, 1.0)
        assert abs(result - 7.0) < 0.0001
    
    def test_subtract_single_number(self):
        """Test subtract with single number returns that number."""
        assert subtract(42) == 42
    
    def test_subtract_to_zero(self):
        """Test subtracting to zero."""
        assert subtract(5, 5) == 0
    
    def test_subtract_from_zero(self):
        """Test subtracting from zero."""
        assert subtract(0, 5, 3) == -8
    
    def test_subtract_no_arguments_raises_error(self):
        """Test that no arguments raises ValueError."""
        with pytest.raises(ValueError):
            subtract()
    
    def test_subtract_non_numeric_raises_error(self):
        """Test that non-numeric input raises TypeError."""
        with pytest.raises(TypeError):
            subtract(10, "5", 3)
    
    def test_subtract_none_raises_error(self):
        """Test that None input raises TypeError."""
        with pytest.raises(TypeError):
            subtract(10, None)
