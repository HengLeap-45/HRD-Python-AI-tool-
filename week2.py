# this signal 
# " == " mean equal
# " > " mean greater than
# " < " mean less than
# " >=" mean greater than or equal to
# "<=" mean less than or equal to
# "!=" mean not equal to
# "=" for price of variable

import _collections_abc
color = "red"
if color == "blue":
    print("The color is red")
else:
    print("The color is not red")

print("=====================")
a = 18 
print(f"This is the value of a: {a}")

a == 18 
print(a==18)

print("=====================")

age = 24 
print(age == 18)
print("=====================")

print(age!=18)
print(age>18)
print("======================")

# and or not # and: All condition must be true
# or: Any one condition must be true
# not: Reverse the condition
is_drinking = False
is_raining = True
print(not is_raining)
print(is_raining)
print("========================")
#and 
print( is_raining and is_drinking  )
print("========================")
# or 
print(is_drinking or is_raining)

print("============Condistion statement===========")
age = 15
if age >= 16 :
    print ("You are can working") 

print("==================================")
battery = 25
if battery != 20 :
    print("not alert")
else :
    print("alert")

print("==================")
score = 100 
if score == 100 :
    print("pass")
else :
    print("fail")

print("========Traffic_lignt ==========")

traffic_lignt = input("Enter the traffic lignt : ")

if traffic_lignt == "Green" :
    print("go")
elif traffic_lignt == "Yellow" :
    print("Slow")
elif traffic_lignt == "Red" :
    print("stop")    
else :
    print("Invalid traffic_lignt")    

# If syntax is use : If conditaion , operator: 
    

