import numpy as np
import csv

# Custom Exception
class NegativeValueError(Exception):
    def __init__(self, message="Array contains negative values"):
        self.message = message
        super().__init__(self.message)

# Function to check for negative values
def validate_array(arr):
    if np.any(arr < 0):
        raise NegativeValueError("Negative values are not allowed in the array.")

# Create a 2D numpy array (3x3)
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

try:
    # Validate array
    validate_array(array_2d)

    # Write to CSV
    with open("array_data.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(array_2d)
    print("2D array written to array_data.csv")

    # Read back from CSV
    with open("array_data.csv", "r") as file:
        reader = csv.reader(file)
        loaded_array = np.array([[int(cell) for cell in row] for row in reader])

    print("\nRead array from CSV:")
    print(loaded_array)

except NegativeValueError as ne:
    print("Custom Exception Occurred:", ne)
except Exception as e:
    print("Some other error occurred:", e)
