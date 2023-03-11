val = 0
out = 0
Fnum = int(input("Enter the First number:"))
print(Fnum)
Snum = int(input("Enter the Second number:"))
print(Snum)
print("For Addition print 1")
print("For Subtraction print 2")
print("For Multiplication print 3")
print("For Division print 4")
val=int(input("Enter your choice :"))
if val==1:
  out = Fnum + Snum
  print("Answer is :", out)
elif val == 2:
  out = Fnum - Snum
  print("Answer is :", out)
elif val == 3:
  out = Fnum * Snum
  print("Answer is :", out)
elif val == 4:
  out = Fnum / Snum
  print("Answer is :", out)
else:
  print("Invalid input")
