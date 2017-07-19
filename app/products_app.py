menu = """

    Welcome to the products app.

    There are 28 products.

    Please choose an operation: 'List', 'Show', 'Create', 'Update', 'Destroy'

"""

chosen_operation = input(menu)

if chosen_operation.title() == "List":
    print("LISTING PRODUCTS")
elif chosen_operation.title() == "Show":
    print("SHOWING PRODUCTS")
elif chosen_operation.title() == "Create":
    print("CREATING PRODUCTS")
elif chosen_operation.title() == "Update":
    print("UPDATING PRODUCTS")
elif chosen_operation.title() == "Destroy":
    print("DESTROYING PRODUCTS")
else:
     print("WRONG COMMAND")           
