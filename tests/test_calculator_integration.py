"""Integration tests for calculator.py."""
import pytest
from unittest.mock import patch, call
from src.calculator import (
    print_menu, get_numbers, get_choice, 
    calculate, main
)


class TestPrintMenu:
    """Test menu printing."""
    
    def test_print_menu_output(self, capsys):
        """Test that menu prints correctly."""
        print_menu()
        captured = capsys.readouterr()
        assert "CALCULATOR MENU" in captured.out
        assert "1. Addition" in captured.out
        assert "2. Subtraction" in captured.out
        assert "3. Multiplication" in captured.out
        assert "4. Division" in captured.out


class TestGetNumbers:
    """Test number input."""
    
    @patch('builtins.input', side_effect=['5', '3'])
    def test_get_numbers_valid(self, mock_input):
        """Test getting valid numbers."""
        num1, num2 = get_numbers()
        assert num1 == 5.0
        assert num2 == 3.0
    
    @patch('builtins.input', side_effect=['5.5', '3.2'])
    def test_get_numbers_floats(self, mock_input):
        """Test getting float numbers."""
        num1, num2 = get_numbers()
        assert num1 == 5.5
        assert num2 == 3.2
    
    @patch('builtins.input', side_effect=['abc', '3'])
    def test_get_numbers_invalid_first(self, mock_input):
        """Test invalid first number raises ValueError."""
        with pytest.raises(ValueError, match="Invalid input"):
            get_numbers()
    
    @patch('builtins.input', side_effect=['5', 'xyz'])
    def test_get_numbers_invalid_second(self, mock_input):
        """Test invalid second number raises ValueError."""
        with pytest.raises(ValueError, match="Invalid input"):
            get_numbers()


class TestGetChoice:
    """Test menu choice input."""
    
    @patch('builtins.input', return_value='1')
    def test_get_choice_valid_1(self, mock_input):
        """Test valid choice 1."""
        assert get_choice() == 1
    
    @patch('builtins.input', return_value='4')
    def test_get_choice_valid_4(self, mock_input):
        """Test valid choice 4."""
        assert get_choice() == 4
    
    @patch('builtins.input', return_value='5')
    def test_get_choice_out_of_range(self, mock_input):
        """Test choice out of range raises ValueError."""
        with pytest.raises(ValueError, match="Choice must be between 1 and 4"):
            get_choice()
    
    @patch('builtins.input', return_value='0')
    def test_get_choice_zero(self, mock_input):
        """Test choice 0 raises ValueError."""
        with pytest.raises(ValueError):
            get_choice()
    
    @patch('builtins.input', return_value='abc')
    def test_get_choice_non_numeric(self, mock_input):
        """Test non-numeric choice raises ValueError."""
        with pytest.raises(ValueError, match="Invalid input"):
            get_choice()


class TestCalculate:
    """Test calculation function."""
    
    def test_calculate_addition(self):
        """Test addition calculation."""
        assert calculate(1, 10, 5) == 15
    
    def test_calculate_subtraction(self):
        """Test subtraction calculation."""
        assert calculate(2, 10, 5) == 5
    
    def test_calculate_multiplication(self):
        """Test multiplication calculation."""
        assert calculate(3, 10, 5) == 50
    
    def test_calculate_division(self):
        """Test division calculation."""
        assert calculate(4, 10, 5) == 2.0
    
    def test_calculate_division_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calculate(4, 10, 0)
    
    def test_calculate_division_floats(self):
        """Test division with floats."""
        result = calculate(4, 7, 2)
        assert result == 3.5


class TestMainIntegration:
    """Integration tests for main calculator flow."""
    
    @patch('builtins.input', side_effect=['1', '10', '5', 'n'])
    def test_main_addition_flow(self, mock_input, capsys):
        """Test complete addition flow."""
        main()
        captured = capsys.readouterr()
        assert "15" in captured.out or "15.0" in captured.out
        assert "Addition Result" in captured.out
    
    @patch('builtins.input', side_effect=['2', '10', '5', 'n'])
    def test_main_subtraction_flow(self, mock_input, capsys):
        """Test complete subtraction flow."""
        main()
        captured = capsys.readouterr()
        assert "5" in captured.out or "5.0" in captured.out
    
    @patch('builtins.input', side_effect=['4', '10', '0', 'n'])
    def test_main_division_by_zero_handling(self, mock_input, capsys):
        """Test division by zero error handling."""
        main()
        captured = capsys.readouterr()
        assert "Cannot divide by zero" in captured.out
    
    @patch('builtins.input', side_effect=['5', '1', '10', '5', 'n'])
    def test_main_invalid_choice_recovery(self, mock_input, capsys):
        """Test recovery from invalid menu choice."""
        main()
        captured = capsys.readouterr()
        assert "Error" in captured.out
    
    @patch('builtins.input', side_effect=['1', 'abc', '5', 'n'])
    def test_main_invalid_number_handling(self, mock_input, capsys):
        """Test invalid number input handling."""
        main()
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out
    
    @patch('builtins.input', side_effect=['1', '5', '3', 'y', '2', '10', '4', 'n'])
    def test_main_multiple_calculations(self, mock_input, capsys):
        """Test multiple calculations in sequence."""
        main()
        captured = capsys.readouterr()
        assert "8" in captured.out or "8.0" in captured.out  # 5+3
        assert "6" in captured.out or "6.0" in captured.out  # 10-4
