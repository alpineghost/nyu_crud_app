
#Reading CSV Files

import csv

csv_file_path = "data/products.csv"

###counting rows from Prof Rossetti
products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)


menu = """

    Welcome to the products app.

    There are {0} products.

    Please choose an operation: 'List', 'Show', 'Create', 'Update', 'Destroy'

""".format(len(products))

print(menu)

#chosen_operation = input(menu)
#chosen_operation = chosen_operation.title()

def list_products():
    print("LISTING PRODUCTS")

def show_product():
    print("SHOWING A PRODUCT")

def create_product():
    print("CREATING A PRODUCT")

def update_product():
    print("UPDATING A PRODUCT")

def destroy_product():
    print("DESTROYING A PRODUCT")

#if chosen_operation == "List":
#    list_products()
#elif chosen_operation == "Show":
#    show_product()
#elif chosen_operation == "Create":
#    create_product()
#elif chosen_operation == "Update":
#    update_product()
#elif chosen_operation == "Destroy":
#    destroy_product()
#else:
#     print("WRONG COMMAND. PLEASE TRY AGAIN.")

#Reading CSV Files

import csv

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
        print(row["id"], row["name"])

csv_file_path = "teams.csv"

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above
    writer.writerow({"city": "New York", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})
