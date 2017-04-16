X = 0
Y = 0
Z = 1

a1 = (X and not Y) or Z

print("a)",a1)

a2 = X and (not Y or Z)

print("б)",a2)

a3 = X or (not(Y or Z))

print("в)",a3)
