Falsecount = 0
Numslist = [1,2,3,0,6,4,5,8,9,7]
Duplicatelist = []
for Number in Numslist:
  Duplicate = Number in Duplicatelist
  if (Numslist.count(Number) > 1):
    if (Duplicate == False):
      Duplicatelist.append(Number)
  else :
    Falsecount = Falsecount + 1
for Finalnums in Duplicatelist :
  print(Finalnums)
if Falsecount == len(Numslist):
  print("No Duplicate Number Found.")