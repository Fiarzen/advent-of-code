def list_compare(lst1, lst2):
    sorted_lst1 = sorted(lst1)
    sorted_lst2 = sorted(lst2)
    count = 0
    for i in range(len(sorted_lst1)):
        count += abs(sorted_lst1[i] - sorted_lst2[i])
    return count

def create_lists():
    lst1 = []
    lst2 = []
    with open("input.txt") as f:
        for line in f:
            # Split the line into two numbers
            num1, num2 = map(int, line.split())
            lst1.append(num1)
            lst2.append(num2)
    return (lst1, lst2)

create_lists()

print(list_compare(*(create_lists())))