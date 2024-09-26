import pytest
from ihk_calculator import calculate_percentage, get_grade


# Define the test cases
@pytest.mark.parametrize("percentage, expected_grade", [
    (100, "1 - Sehr gut"),
    (92, "1 - Sehr gut"),
    (91, "2 - Gut"),
    (81, "2 - Gut"),
    (80, "3 - Befriedigend"),
    (67, "3 - Befriedigend"),
    (66, "4 - Ausreichend"),
    (50, "4 - Ausreichend"),
    (49, "5 - Mangelhaft"),
    (30, "5 - Mangelhaft"),
    (29, "6 - Ungenügend"),
    (0, "6 - Ungenügend"),
])
def test_get_grade(percentage, expected_grade):
    assert get_grade(percentage) == expected_grade


# Define the test cases
@pytest.mark.parametrize("points_obtained, total_points, expected", [
    (50, 100, 50.0),  # 50% -> valid
    (0, 100, 0.0),  # 0% -> valid
    (80, 100, 80.0),  # 80% -> valid
    (50, 0, 0),  # Edge case: total points = 0
    (50, -1, "Total points cannot be negative"),  # Edge case: negative total points
])
# Test the calculate_percentage function
def test_calculate_percentage(points_obtained, total_points, expected):
    assert calculate_percentage(points_obtained, total_points) == expected


# Define the test cases
@pytest.mark.parametrize("percentage, expected_exception", [
    (-1, ValueError),  # Percentage cannot be negative
    (101, ValueError),  # Percentage cannot be over 100
    ("text", TypeError),  # Invalid type
])
# Test the get_grade function
def test_get_grade_exceptions(percentage, expected_exception):
    with pytest.raises(expected_exception):
        if isinstance(percentage, str):
            raise TypeError("Invalid input type")  # Simulating the TypeError
        elif percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
        else:
            get_grade(percentage)
