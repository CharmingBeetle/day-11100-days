print("***HOW MANY SECONDS ARE IN A YEAR?!***")
print()
#Normal year
year = ((60 * 60) * 24) * 365
answer = year
#Leap year
lyear = ((60 * 60) * 24) * 366
answer2 = lyear

ly = input("Is it a leap year?: ")
if ly == "yes" or ly == "YES" or ly == "Yes" or ly == "y":
  print()
  print(answer2)
print()
if ly == "no" or ly == "NO" or ly == "No" or ly == "n":
  print (answer)
