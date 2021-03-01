def partitionArray(A, k):


flag = 0

if not A and k == 1:

return "Yes"

if k > len(A) or len(A) % len(A):

return "No"

flag += 1

cnt = {i: A.count(i) for i in A}

if len(A)//k < max(cnt.values()):

return "No"

flag += 1

if(flag == 0):

return "Yes"

k = int(input("k= "))

n = int(input("n= "))

print("A= ")

A = list(map(int, input().split()))[:n]

print(partitionArray(A, k))
