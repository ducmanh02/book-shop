t = int(input())
for _ in range(t):
    n = int(input())
    mu2 = 1
    mu3 = 1
    kq = 6
    if(n==1): print(1)
    elif(n<=2): print(2)
    elif(n<=4): print(4)
    else:
        while kq < n:
            if ((2**(mu2+1) * 3**(mu3)) < (2**(mu2) * 3**(mu3+1))):
                kq = 2**(mu2 +1) * 3**mu3
            else:
                kq = 2**(mu2) * 3**(mu3+1)
            uoc = (mu2+1) * (mu3+1)
        print(kq)