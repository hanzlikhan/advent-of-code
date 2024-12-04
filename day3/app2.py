import re

def parse_and_sum_with_conditions(file_path):
    try:
        # Step 1: Read the file
        with open(file_path, 'r') as file:
            data = file.read()

        # Step 2: Define patterns for mul, do, and don't instructions
        mul_pattern = r"mul\((\d+),(\d+)\)"
        do_pattern = r"do\(\)"
        dont_pattern = r"don't\(\)"

        # Step 3: Find all instructions in order
        instructions = []
        for match in re.finditer(f"{mul_pattern}|{do_pattern}|{dont_pattern}", data):
            if match.group(1) and match.group(2):
                # Found a mul(X,Y)
                instructions.append(('mul', int(match.group(1)), int(match.group(2))))
            elif match.group(0) == "do()":
                instructions.append(('do',))
            elif match.group(0) == "don't()":
                instructions.append(('dont',))

        # Step 4: Process instructions
        enabled = True  # Initially, mul is enabled
        result_sum = 0

        for instruction in instructions:
            if instruction[0] == 'mul':
                if enabled:
                    result_sum += instruction[1] * instruction[2]
            elif instruction[0] == 'do':
                enabled = True
            elif instruction[0] == 'dont':
                enabled = False

        return result_sum

    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
file_path = 'input.txt'  # Replace with your file path
result = parse_and_sum_with_conditions(file_path)
print("The sum of all enabled mul instructions is:", result)
