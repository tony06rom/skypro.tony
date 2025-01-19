from unittest.mock import Mock
from src.external_api import convert_amount

def test_convert_amount():
    mock_random = Mock(return_value=5)
    random.randint = mock_random
    assert convert_amount() == 5
    mock_random.assert_called_once_with(0, 10)




def get_random_number():
    return random.randint(0, 10)

def test_get_random_number():
    mock_random = Mock(return_value=5)
    random.randint = mock_random
    assert get_random_number() == 5
    mock_random.assert_called_once_with(0, 10)