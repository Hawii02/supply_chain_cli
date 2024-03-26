from helpers import find_supplier_by_name, delete_customer, add_customer, get_suppliers, find_product_by_name


def main():
    while True:
        print("What do you want to enquire about?")
        print("1. To find a supplier")
        print("2. To find a product")
        print("3. To delete a customer")
        print("4. To add a customer")
        print("5. List all suppliers")
        print("6. Exit the application") 
        userschoice = input("what do you want to enquire about?")
        
        if userschoice == "1":
            find_supplier_by_name()

        elif userschoice == "2":
            find_product_by_name()
        elif userschoice == "3":
            delete_customer()
        elif userschoice == "4":
            add_customer()
        elif userschoice == "5":
            get_suppliers()
        elif userschoice == "6":
            print("Exiting the App, byee")
            exit()
        else:
            print("Invalid choice")
        
if  __name__ == '__main__':
    main()

    