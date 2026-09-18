def largest(a,b,c):
    if a>b and a>c:
        return f"largest number is {a}"
    elif b>a and b>c:
        return f"largest number is {b}"
    else:
        return f"largest number is {c}"
print(largest(10,50,30))