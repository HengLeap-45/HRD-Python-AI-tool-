price = [3,0,2,3,4,5,6,7,10]
total =0 
print(f"First Item : ${price[0]}")
print(f"Last item : ${price[-2]}")
print(f"Number of item :{len(price )}")

for prices in  price :
    total += prices

print(f"Total bill : $ { total}")