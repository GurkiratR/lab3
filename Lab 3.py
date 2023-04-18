#initialize an empty dictionary
shoppingCart = {}

#function to add products to the cart
def addProduct():
    num_items = int(input("Enter the number of items to be added in the shopping cart: "))
    count = 0
    while count < num_items:
        if len(shoppingCart) >= 5:
            print("Cart is full")
            break
        else:
            productName = input("Enter an item: ")
            productBrand = input("Enter the brand Name: ")
            shoppingCart[productName] = productBrand
            print("You added", productName, "to the cart.")
            count += 1

#function to search for a product in the cart
def searchProduct():
    productName = input("Enter the item to be searched: ")
    if productName in shoppingCart.keys():
        print(productName + ": " + shoppingCart[productName])
    else:
        print("No product exists with this name.")

#function to delete a product from the cart
def deleteProduct():
    if len(shoppingCart) == 0:
        print("Cart is empty, no item is found.")
    else:
        productName = input("Enter the item to be deleted: ")
        if productName in shoppingCart.keys():
            del shoppingCart[productName]
            print("Product deleted successfully.")
        else:
            print("No product exists with this name.")

#main function to display the menu
def main():
    while True:
        print("WELCOME TO THE AMANDO SHOPPING SITE\n")
        print("1. Add product to the cart.")
        print("2. Search the product.")
        print("3. Delete the product from the cart.")
        print("4. Quit.")
        choice = input("Enter your choice: ")
        if choice == "1":
            addProduct()
        elif choice == "2":
            searchProduct()
        elif choice == "3":
            deleteProduct()
        elif choice == "4":
            print("Thank you for using our shopping site.")
            break
        else:
            print("Wrong Option Entered.")

#call the main function
main()
