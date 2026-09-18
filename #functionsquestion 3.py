#functions 3
#WAF to print the length of a list(list is the parameter)
#cities = ["lucknow","delhi","mumbai","chennai"]
#A=["a","e","i","o","u"]
#def print_len(list):
#    print(len(list))#
#
#print_len(cities)
#print_len(A)

#WAF to print the element of a list in a single line

cities = ["lucknow","delhi","mumbai","chennai"]
def print_sameline(list):
    for item in list:
        print(item,end=" ")
print_sameline(cities)


def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
cal_fact(5)