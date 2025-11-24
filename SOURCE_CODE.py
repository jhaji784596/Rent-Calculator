print("Rent Calculator by  @jhaji")

kiraya = int(input("Enter your hostel/flat kiraya = "))
khana = int(input("Enter the amount of khana ordered ="))
electricity_used = int(input("Enter the total electricity units used = "))

charge_per_unit = int(input("Enter  charge per unit = "))

persons = int(input("Enter the number of persons living in flat = "))


total_bill = electricity_used * charge_per_unit
output = (khana + kiraya + total_bill) // persons

print("Each person pays =", output)
print(" Thank you for using the Rent Calculator!")
