n=int(input())
c=0
if n==0:
  c=1
else:
  while n>0:
    n=n//10
    c+=1
print(c)
