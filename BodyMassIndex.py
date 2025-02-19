W=float(input(" Enter your weight:"))
H=float(input(" Enter your height:"))

if W<=0 or H<=0:
 print("NO RESULT")

else:
   BMI=W/(H*H)


   if BMI <18.5:
    Catagory="underweight"
 
   elif 18.5<=BMI<25:
 
    Catagory="normal"
    
   elif 25<=BMI<30:
    
    Catagory="overweight"

   else:
    
    Catagory="obese"  

   print("your BMI is :",BMI)
   print(f"you are in the {Catagory} range")
    