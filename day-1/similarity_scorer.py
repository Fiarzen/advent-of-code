def create_lists():
    lst1 = []
    lst2 = []
    with open("input.txt") as f:
        for line in f:
            num1, num2 = map(int, line.split())
            lst1.append(num1)
            lst2.append(num2)
    return (lst1, lst2)

def simularity_scorer(lst1, lst2):
    score = 0
    for i in lst1:
        count = 0
        for x in lst2:
            if i == x:
                count +=1
        score += i*count
    print(score)

simularity_scorer(*(create_lists()))
