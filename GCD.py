# 9.Given a list of integers, return their Greatest Common Divisor (Divisor).



def min_m(x,y):
    if x>y:
        return x
    else:
        return y

def gcd(a,b):
    lower = min_m(a,b)
    for i in range(1,lower +1):
        if a%i==0 and b%i==0:
            gcd_n=i

    return gcd_n
def gcd_lst(num_list):

    gcd_num= num_list[0]
    for items in num_list:
        gcd_num= gcd(gcd_num,items)
    return gcd_num

list1= [15,20,10,35]

print(gcd_lst(list1))