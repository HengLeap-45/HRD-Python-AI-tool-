price = [3,1,2,3,4,4,5,6,7]
total =0 
print(f"First Item : ${price[0]}")
print(f"Last item : ${price[-1]}")
print(f"Number of item :{len(price )}")

for prices in  price :
    total += price 

print(f"Total bill : $ { total}")