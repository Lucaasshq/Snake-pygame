def f_rec(x):
  if x==0:
    return 0
  s = x%10
  n = x//10
  return s+f_rec(n)

print(f_rec(123)) 