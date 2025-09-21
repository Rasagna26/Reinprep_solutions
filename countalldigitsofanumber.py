n=int(input())
t=0
if n==0|n<=9:
  print(1)
else:
  c=0
  while n!=0:
    n=n//10
    c=c+1
  print(c)
