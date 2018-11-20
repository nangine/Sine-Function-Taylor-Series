def fact (n) :
    if n==0 :
        return 1
    else:
        return n*fact(n-1)

def sin (k):
    a=0
    pi=22/7
    x=k*(pi/180)
    for i in range (0,11,1):
        a+=((x**(2*i+1))/(fact(2*i+1)))*((-1)**i)
    return a

opt = "y"
while opt == "y":
    k = float(input("Insert angle in degree =  "))
    sin(k)
    print ("Value of sine (",k,") =",round(sin(k),3))
    opt = input ("Continue? y/t ")
    print ()
print ("***Done***")
print ()
