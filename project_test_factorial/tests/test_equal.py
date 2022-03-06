import pytest

@pytest.mark.parametrize("repeat", [1])
def test_equal_values(repeat, method_post_factorial, generate_data_factorial):
    assert method_post_factorial == generate_data_factorial
