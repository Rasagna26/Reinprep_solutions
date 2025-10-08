n=int(input())
arr=list(map(int,input().split()))
if arr==sorted(arr):
  print("True")
else:
  print("False")
