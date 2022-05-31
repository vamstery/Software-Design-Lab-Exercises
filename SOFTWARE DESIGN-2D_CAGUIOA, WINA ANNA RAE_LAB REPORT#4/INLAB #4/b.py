def  product(m,n):
    if m == 0:
        return 0

    if m > 0:
        return (n + product (n,m-1))

m = 15
n = 5

print("The product is: ", product(n,m))