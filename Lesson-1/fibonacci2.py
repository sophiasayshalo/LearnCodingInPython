# Generating the Fibonacci sequence up to 100 (in a row)

print("The Fibonacci sequence up to 100: \n")
limit = 89
Var2 = 1
counter = Var1 = Var3 = 0
Fib = [0, 1]
while Var3 < limit:
    Var3 = Var1 + Var2
    Var1,Var2 = Var2, Var3
    Fib.insert(counter + 2, Var3)
    counter +=1
print(Fib)
