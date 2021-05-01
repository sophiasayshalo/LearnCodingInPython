def assignment(n):

    c = n[0] * n[0] + n[1] * 2

    return c

numbers = [
    [5, 6],
    [3, 5], 
    [2, 4]
]

for num in numbers:
    result = assignment(num)

    print(result)