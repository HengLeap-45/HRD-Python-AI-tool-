
fruits  = {
    "apple" :  1,
    "banana" :  4 ,
    "grape" :  7,
    "orange" :  10,
    "mango" :  13,
    "strawberry" :  16,
    "watermelon" :  19,
    "pineapple" :  22,
    "kiwi" :  25,
    "papaya" :  28,
    "melon" :  1,
    "cherry" :  4,
    "lemon" :  7,
    "lime" :  10,
    "peach" :  21,
    "pear" :  18,
    "plum" :  15,
    "raspberry" :  12,
    "blueberry" :  9,
    " blackberry" :  6,
}

print("Apple price :",  fruits["apple"])
print("banana price :" , fruits["banana"])
print("grape pricce :", fruits["grape"])
fruits["grape"] = 5
fruits["age"] = 20 
print(f"Number of item : {len(fruits)} ")

    #use for loop to get the total 3
total = 0 
for price in fruits.values():
    total = total + price 
    
print(f"TOtal bill : {total}")