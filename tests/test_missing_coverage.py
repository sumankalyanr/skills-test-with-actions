import pytest
from calculations import area_of_circle, get_nth_fibonacci

def test_area_of_circle_negative_radius():
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(-1)

def test_get_nth_fibonacci_negative():
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(-5)
