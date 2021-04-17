# Generating the Fibonacci sequence up to 100 (in a column)

print("A list of the fibonacci sequence up to 100: \n")
limit = 88
Var2 = 1
counter = Var1 = Var3 = 0
while Var3 < limit:
    Var3 = Var1 + Var2
    Var1,Var2 = Var2, Var3
    print(Var3)
    counter +=1