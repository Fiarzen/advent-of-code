def check_safety(a):
    # Check if the sequence is strictly increasing or strictly decreasing
    diffs = [a[i + 1] - a[i] for i in range(len(a) - 1)]  # List of differences between adjacent levels
    
    # Check if all differences are either between 1 and 3 for increasing or between -1 and -3 for decreasing
    if (all(x < 0 and x in range(-3, 0) for x in diffs) or  # All differences are negative and between -3 and -1
        all(x > 0 and x in range(1, 4) for x in diffs)):    # All differences are positive and between 1 and 3
        return True
    else:
        return False


def safety_check():
    safe_count = 0  # Count of safe reports
    with open("day_2_input.txt") as f:
        for line in f:
            # Convert line into a list of integers
            line_lst = list(map(int, line.split()))

            # First, check if the line is already safe without modification
            if check_safety(line_lst):
                safe_count += 1
                continue
            
            # Now check if removing any one level makes the sequence safe
            for i in range(len(line_lst)):
                # Create a new list with the i-th element removed
                modified_line = line_lst[:i] + line_lst[i + 1:]
                
                # Check if the modified line is safe
                if check_safety(modified_line):
                    safe_count += 1
                    break  # Once we find a safe version by removing one level, no need to check further

    return safe_count


# Call the function and print the number of safe reports
print(safety_check())
