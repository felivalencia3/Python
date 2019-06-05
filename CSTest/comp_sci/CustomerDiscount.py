import time
import json
#Constants
one_to_nine = 0.95
ten_to_thirty = 0.9
thirty_more = 0.85
VAT = 1.2
tempValue = 0
totalValue = 0
# Dictionary/Objects replace Switch Statement
products = {
    "book": 2,
    "coffee": 3,
    "computer": 10,
    "paper": 1,
    "apple": 2
}
while(True):
    print("The Products available are the following\n\t")
    print(json.dumps(products,indent=4))
    productName = input("Enter Product Name:\n\t ")
    product_name = productName
    if not product_name or product_name == "":
        print("We hope you were satisfied with your shopping")
        time.sleep(1)
        print("\n\n Your final value is: {0}".format(totalValue))
        break
    productName = productName.lower()
    tempValue = products[productName]
    quantity = input("How many {0}s do you want:\t".format(product_name))
    # Quantity Checks
    quantity = int(quantity)
    tempValue *= quantity
    if quantity >= 1 and quantity <= 9:
        tempValue *= one_to_nine
    elif quantity >= 10 and quantity <= 29:
        tempValue *= ten_to_thirty
    elif quantity >= 30:
        tempValue *= thirty_more

    totalValue += tempValue
    totalValue *= VAT
    print("\n\tYou have to pay ${0}".format(tempValue))
    time.sleep(1)
    print("\nWhen you are done shopping, hit enter when prompted for your product.")