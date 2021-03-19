# Calculating the sum of even numbers from 1 to 100

answer = 0
for number in range(1, 101):
    if(number % 2 == 0):
        answer += number
answer = str(answer)
print("The sum of even numbers from 1 to 100 is: " + answer)
