
year = int(input("please Enter year: "))
checkRemainder = year % 4
checkCentury1 = year % 100
checkCentury2 = year % 400

if checkRemainder == 0 and checkCentury1 != 0:

  print(f"{year} is a Leap Year")

elif checkCentury1 == 0 and checkCentury2 == 0:

  print(f"{year} is a Leap Centuary Year" )

else:

  print(f"{year} is not a Leap Year")