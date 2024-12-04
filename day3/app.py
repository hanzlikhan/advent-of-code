import re

def parse_and_sum_mul(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()

        # Regular expression to find valid mul(X,Y) patterns
        pattern = r"mul\((\d+),(\d+)\)"

        # Find all matches in the corrupted memory
        matches = re.findall(pattern, data)

        # Compute the sum of the results of all valid mul instructions
        result_sum = sum(int(x) * int(y) for x, y in matches)

        return result_sum

    except FileNotFoundError:
        return "Error: File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
file_path = 'input.txt'  # Replace with your actual file path
result = parse_and_sum_mul(file_path)
print("The sum of all valid mul instructions is:", result)
