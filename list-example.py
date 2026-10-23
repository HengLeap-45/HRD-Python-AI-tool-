# Create list 
fruits = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
#print The whole list
print("The whole list :", fruits)
#3.Accessing items by index 
print ("The first item in the list is : ", fruits[0])
print("The second item in the list is : ", fruits[1])
print("The third item in the list is : ", fruits[2])
#Accessing items by negative index 
print("The last item in the list is :", fruits[-1])
print("The second last item in the list is :", fruits[-2])
print("The third last item in the list is :", fruits[-3])
# use an item inside a string 
print(f"My fruit is :{fruits[0]}")
#Find out how many items are in the list 
print("The number of item in y the  list is : ",len(fruits))

# use for loop 

for fruit in fruits :
        print(f"I like this fruit : {fruit}")

# Accessing items in the list by using index
for i in range(len(fruits)):
        print(f"Fruit number {i+1} (index {i}) : {fruits[i]}")

# Creat the list 
store = [3,5,2,4,6]
#Access the list 
print("the first item in the lsit is  : ", store[0],"$")
print("The last item in the list is  : ", store[-1],"$")
print("the number of the list is : ", len(store))
#use sum() function to get the total bill
print("the total bill is : ", sum(store),"$")

# Loop throught the list 
Total_bill = 0

for item in store :
    Total_bill = Total_bill + item
print("the total bill after loop is : ",Total_bill,"$") 
   
    #use the index to access the list foe get the total bill      
    











