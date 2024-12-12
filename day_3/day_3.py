import re

def extract_and_multiply(memory_string):
    mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r'don\'t\(\)')

    total = 0
    mul_enabled = True

    pos = 0
    while pos < len(memory_string):

        if do_pattern.match(memory_string, pos):
            mul_enabled = True
            pos += 4  
        elif dont_pattern.match(memory_string, pos):
            mul_enabled = False
            pos += 6  
        else:

            mul_match = mul_pattern.match(memory_string, pos)
            if mul_match and mul_enabled:
                x, y = mul_match.groups()
                result = int(x) * int(y)
                total += result
                print(f"Found mul({x},{y}) = {result}")
            pos += 1

    print(f"Total Sum: {total}")
    return total


with open("inputs/day_3_input.txt") as f:
    corrupted_memory = f.read()

print(extract_and_multiply(corrupted_memory))
