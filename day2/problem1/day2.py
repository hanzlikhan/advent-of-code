def is_safe_report(report):
    if not report or len(report) < 2:
        return False

    increasing, decreasing = True, True

    for i in range(len(report) - 1):
        diff = abs(report[i + 1] - report[i])
        if diff < 1 or diff > 3:
            return False  # Invalid difference, early exit

        if report[i + 1] > report[i]:
            decreasing = False
        elif report[i + 1] < report[i]:
            increasing = False

        if not increasing and not decreasing:
            return False  # Early exit if neither condition holds

    return True


def count_safe_reports(filename):
    safe_count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Convert the line into a list of integers
                report = list(map(int, line.strip().split()))
                
                if is_safe_report(report):
                    safe_count += 1
                else:
                    # Attempt to find a safe report by removing one element at a time
                    for i in range(len(report)):
                        temp_report = report[:i] + report[i+1:]  # Create a new list without the ith element
                        if is_safe_report(temp_report):
                            safe_count += 1
                            break

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)

    return safe_count


# File path
filename = r"C:\Users\PMLS\Desktop\advent of code\day2\problem1\input.txt"

# Count safe reports
safe_reports_count = count_safe_reports(filename)
print(f"Number of safe reports: {safe_reports_count}")
