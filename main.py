from ihk_calculator import calculate_percentage, get_grade  # Import the functions
import unittest


def main():
    # Example usage
    points_obtained = 90
    total_points = 100
    percentage = calculate_percentage(points_obtained, total_points)
    grade = get_grade(percentage)

    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
