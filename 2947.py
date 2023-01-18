a = list(map(int,input().split()))

while True:
    for i in range(4):
        if a[i]>a[i+1]:
            b = a[i]
            a[i] = a[i+1]
            a[i+1] = b
            print(''.join(map(str,a)))

    if a == [1,2,3,4,5]:
        break
        

