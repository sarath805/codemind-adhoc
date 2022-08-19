a = int(input())
k = []
for i in range(1,a+1):
    k.append(i*"*")
k.reverse()
for i in k:
    print(i)