def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:])+string[0]

s = input("Enter a string: ")
print("Reverse string: ", reverse(s))