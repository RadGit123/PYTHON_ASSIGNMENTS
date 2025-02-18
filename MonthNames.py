M=['January','February','March','April','May','June','July','Augest','September','October','November','December']

E=int(input("Enter the Number:"))       

if E>=1  and E<=12:
  print(f"THE MONTH {E} IS {M[E-1]}")
else:
  print("The number is not valid")
