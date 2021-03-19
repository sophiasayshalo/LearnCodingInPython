i = 1
total = 10
while i <= 100:
    total = total + i
    # i = 1, total = 1
    print("1 = {0}, total = {1}".format(i, total))
    i = i + 1
print("final total: {0}".format(total))

while True: 
    animal = input("What animal is it? ")
    if animal == "dog":
        print("bark")
        print("bark")
    elif animal == "cat":
        print("meow")
        print("meow")
    elif animal == 'bye':
        break
    elif animal == 'con':
        continue
    else:
        print("I don't know you!")

    print('go to next round!')
