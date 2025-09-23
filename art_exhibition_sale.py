
import array  # Importing the array module (not used in this script)

# Define dictionaries for each product with their properties
pent = {"id": 100, "name": "pent", "value": 10000, "test": "for delete"}
jacket = {"id": 101, "name": "jacket", "value": 5000}
shoes = {"id": 102, "name": "shoe", "value": 3000}

del pent["test"]  # Remove the 'test' key from pent dictionary

shoes["value"] = 7000  # Update the value of shoes

# Print available products and their prices
print(
    "chose product.\n",
    pent['name'], ":", pent['value'], "\n",
    jacket['name'], ":", jacket['value'], " \n",
    shoes['name'], ":", shoes['value']
)

# Get user input for quantities of each product
pq = int(input("enter pent quantity if it is none enter 0:"))
jq = int(input("enter jacket quantity if it is none enter 0:"))
sq = int(input("enter shoes quantity if it is none enter 0:"))

nparray = [pq, jq, sq]  # Store quantities in a list

# Create and sort a list of strings
li = ["id", "100", "name", "value", "test"]
li.sort()  # Sort the list alphabetically

print(li)  # Print the sorted list

li.append("property")  # Add 'property' to the list

# If the 6th element exists, remove 'test' from the list
if(li[5]):
    li.remove("test")

print(li)  # Print the updated list

# Calculate total price based on quantities and product values
total = pq * pent['value'] + jq * jacket['value'] + sq * shoes['value']

# Calculate average price per item
average = total / (pq + jq + sq)

# Check if average price is greater than 15000
if(average > 15000):
    print("Average price is greater than 15000")
else:
    print("Average price is less than 15000")

# Find minimum and maximum price among the selected products
minimum = min(pq * pent["value"], jq * jacket["value"], sq * shoes["value"])
maximum = max(pq * pent["value"], jq * jacket["value"], sq * shoes["value"])

# Print summary statistics
report=f"Minimum price is {minimum} Maximum price is {maximum} Average price is {average} total price is {total}"
print(report)



