#selwyn kent onedo bscs 3a
#defensive programming
# 09142023
#sandwich order system using pyinput plus library

import pyinputplus as pyip

class SandwichOrderSystem:
    def __init__(self):
        # Prices dictionary for different sandwich components
        self.prices_dict = {
            'breads': {
                'wheat': 10.00,
                'white': 10.25,
                'sourdough': 20.00,
            },
            'proteins': {
                'chicken': 10.50,
                'turkey': 10.25,
                'ham': 10.75,
                'tofu': 20.00,
            },
            'cheeses': {
                'cheddar': 10.75,
                'Swiss': 10.25,
                'mozzarella': 11.25,
            },
            'addons': {
                'mayo': 5.5,
                'mustard': 5.25,
                'lettuce': 5.50,
                'tomato': 5.50,
            }
        }
        self.discountcode_list = [43312, 67433, 67886, 55534, 89074]  # List of valid discount codes
        self.total_price = 0  # Initialize total price

    def order_sandwiches(self):
        print("*********************************************")
        print("Welcome to the Sandwich Order System!\n")
        print("*********************************************")
        while True:
            try:
                sandwich_name = pyip.inputStr("Please enter your name: ")
                quantity = pyip.inputInt("Enter quantity: ", min=1)
                
                sandwich_price = 0  # Initialize sandwich price
                options = []  # List to store selected options

                # Prompt for bread type
                bread_type = pyip.inputMenu(list(self.prices_dict['breads'].keys()), numbered=True, prompt="\nChoose bread type: \n")
                sandwich_price += self.prices_dict['breads'][bread_type]
                options.append(f"Bread: {bread_type}")

                # Prompt for protein
                protein = pyip.inputMenu(list(self.prices_dict['proteins'].keys()), numbered=True, prompt="Choose protein: \n")
                sandwich_price += self.prices_dict['proteins'][protein]
                options.append(f"Protein: {protein}")

                # Prompt for cheese
                cheese_choice = pyip.inputYesNo("\nAdd cheese? (yes/no): ")
                if cheese_choice == 'yes':
                    cheese = pyip.inputMenu(list(self.prices_dict['cheeses'].keys()), numbered=True, prompt="Choose cheese: \n")
                    sandwich_price += self.prices_dict['cheeses'][cheese]
                    options.append(f"Cheese: {cheese}")

                # Prompt for add-ons
                add_ons_choice = pyip.inputYesNo("Add any add-ons? (yes/no): ")
                while add_ons_choice == 'yes':
                    add_on = pyip.inputMenu(list(self.prices_dict['addons'].keys()), numbered=True, prompt="Choose add-on: \n")
                    sandwich_price += self.prices_dict['addons'][add_on]
                    options.append(f"Add-on: {add_on}")
                    add_ons_choice = pyip.inputYesNo("Add another add-on? (yes/no): ")

                # Calculate the total price for this sandwich
                total_sandwich_price = sandwich_price * quantity
                self.total_price += total_sandwich_price

                # Print the details of the ordered sandwich
                print(f"\nOrdered {quantity} x {sandwich_name}:")
                for option in options:
                    print(f"  - {option}")
                print(f"  Total Price: ${total_sandwich_price:.2f}")

                add_more = pyip.inputYesNo("Add more sandwiches? (yes/no): ")
                if add_more == 'no':
                    break

            except pyip.RetryLimitException as e:
                print(f"Error: {e}")
                print("Please try again.")

    def apply_discount_code(self):
        has_discount_code = pyip.inputYesNo("Do you have a discount code? (yes/no): ")
        if has_discount_code == 'yes':
            while True:
                try:
                    discount_code = pyip.inputInt("Enter discount code: ", blockRegexes=[r'[1]'])  # Block codes containing the digit '1.' For example, it will block code 43312
                    if discount_code in self.discountcode_list:
                        discount_rate = 0.25  # Apply a 25% discount
                        self.total_price *= (1 - discount_rate) #formula to reduce the price from discount 
                        print(f"Discount code '{discount_code}' applied successfully.")
                        break
                    else:
                        print("Invalid discount code. Please try again.") # will display if discount code is invalid
                except pyip.RetryLimitException as e:
                    print(f"Error: {e}")
                    print("Please try again.")
        else:
            print("No discount code applied.") #print if no discount code applied

    def print_total_price(self):
        print(f"\nTotal Price: ${self.total_price:.2f}")
        print("*********************************************")

if __name__ == "__main__":
    order_system = SandwichOrderSystem()
    order_system.order_sandwiches()
    order_system.apply_discount_code()
    order_system.print_total_price()

#END