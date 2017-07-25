


import csv

#Reading CSV Files


###counting rows from Prof Rossetti
products = []

csv_file_path = "data/products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for ordered_dict in reader:
        products.append(dict(ordered_dict))

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
    for product in products:
        print(" + " , product)



def show_product():
    selected_id = input("Ok. Please specify the product's id: ")
    print("SHOWING A PRODUCT")
    for product in products:
        if product["id"] == selected_id:
            print(product)
            #print(products[product_id == selected_id])
    #csv_file_path = "data/products.csv"
    #with open(csv_file_path, "r") as csv_file:
    #    reader = csv.DictReader(csv_file)
    #    if row["id"] == selected_id:
    #        print(row)

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
    selected_id = input("Ok. Please specify the product's id: ")
    for product in products:
        if product["id"] == selected_id:
            selected_product = product

    print("Please specify the product's information...")
    new_name = input ("Change name from " + str(selected_product["name"]) + " to: ")
    new_aisle = input ("Change name from " + str(selected_product["aisle"]) + " to: ")
    new_department = input ("Change name from " + str(selected_product["department"]) + " to: ")
    new_price = input ("Change name from " + str(selected_product["price"]) + " to: ")

    for product in products:
        if product["id"] == selected_id:
            product["name"] = new_name
            product["aisle"] = new_aisle
            product["department"] = new_department
            product["price"] = new_price

    print("UPDATING A PRODUCT")


def destroy_product():
    selected_id = input("Ok. Please specify the product's id: ")
    print("DESTROYING THE FOLLOWING PRODUCT")
    for product in products:
        if product["id"] == selected_id:
            selected_product = product
            print(selected_product)
            products.remove(selected_product)
    #products.remove()

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
