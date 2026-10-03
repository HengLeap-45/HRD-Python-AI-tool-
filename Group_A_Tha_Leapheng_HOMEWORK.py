print("========= Get user input =========")

Product_name = input("Enter Product name : ")
Price = float(input("Enter Product price : "))
Quantity = int(input("Enter Product quantity : "))
Discount = float(input("Enter Discount percentage : "))

print("========= Calculate Value =========")

Total_price = Price * Quantity
Discount_amount = Total_price * Discount
Final_price = Total_price - Discount_amount

print("========= Display the receipt =========")

print("Product : ",Product_name)
print("Price : ",Price)
print("Quantity : ",Quantity)

print("==========================================================")

print(f"Total Price : {Total_price}")
print(f"Discount Amount : {Discount_amount}")
print(f"Final Price : {Final_price}")

print("==========================================================")
print("Thank you for shopping with us! See you next time!")



