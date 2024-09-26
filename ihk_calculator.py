# Function to calculate the percentage of points obtained
def calculate_percentage(points_obtained, total_points):
    if total_points == 0:  # Prevent division by zero
        return 0
    if total_points < 0:   # Prevent negative total points
        return "Total points cannot be negative"
    return (points_obtained / total_points) * 100


# Function to determine the grade based on the percentage
def get_grade(percentage):
    if percentage >= 92:
        return "1 - Sehr gut"
    elif percentage >= 81:
        return "2 - Gut"
    elif percentage >= 67:
        return "3 - Befriedigend"
    elif percentage >= 50:
        return "4 - Ausreichend"
    elif percentage >= 30:
        return "5 - Mangelhaft"
    elif percentage < 0:
        return "There was an error, percentage cannot be negative. Please check the input values."
    else:
        return "6 - Ungenügend"
