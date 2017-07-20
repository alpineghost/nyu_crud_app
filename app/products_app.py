


import csv

#Reading CSV Files
csv_file_path = "data/products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
        print(row["id"], row["name"])

###counting rows from Prof Rossetti
products = []

csv_file_path = "data/products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

other_path = "data/other_products.csv"
##writing csv file
#with open(other_path, "w", newline = '') as csv_file:
#    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle","department","price"])
#    writer.writeheader() # uses fieldnames set above
#    for product in products:
#        writer.writerow(product)



menu = """

    Welcome to the products app.

    There are {0} products.

    Please choose an operation: 'List', 'Show', 'Create', 'Update', 'Destroy'

""".format(len(products))

#print(menu)

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

def list_products():
    print("LISTING PRODUCTS")

def show_product():
    print("SHOWING A PRODUCT")

def create_product():
    print("CREATING A PRODUCT")
    product_name = input("Enter the new product's name: ")
    product_aisle = input("Enter the new product's aisle: ")
    product_department = input("Enter the new product's department: ")
    product_price = input("Enter the new product's price: ")
    new_product = {
        "id": len(products)+ 1 ,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("NEW PRODUCT IS", new_product)
    products.append(new_product)





def update_product():
    print("UPDATING A PRODUCT")

def destroy_product():
    print("DESTROYING A PRODUCT")

if chosen_operation == "List":
    list_products()
elif chosen_operation == "Show":
    show_product()
elif chosen_operation == "Create":
    create_product()
elif chosen_operation == "Update":
    update_product()
elif chosen_operation == "Destroy":
    destroy_product()
else:
     print("WRONG COMMAND. PLEASE TRY AGAIN.")

with open(csv_file_path, "w", newline = '') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)     
