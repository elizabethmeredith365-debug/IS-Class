# Get trip information
user_name = input("Enter your name: ")
destination = input("Enter your destination: ")
distance = float(input("Enter the one-way distance in miles: "))
mpg = float(input("Enter your vehicle's miles per gallon: "))
gas_price = float(input("Enter the gas price per gallon: "))
travelers = int(input("Enter the number of travelers: "))

# Calculate trip information
total_miles = distance * 2
gallons_needed = total_miles / mpg
total_cost = gallons_needed * gas_price
cost_per_traveler = total_cost / travelers

# Display the trip summary
print("\nRoad Trip Summary")
print("Traveler:", user_name)
print("Destination:", destination)
print("Total miles:", total_miles)
print("Gallons needed:", gallons_needed)
print("Total estimated cost: USD", total_cost)
print("Estimated cost per traveler: USD", cost_per_traveler)
