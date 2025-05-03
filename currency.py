def calculate_mileage(distance, fuel):
    """Calculate the mileage (distance per unit of fuel)."""
    try:
        mileage = distance / fuel
        return mileage
    except ZeroDivisionError:
        print("Fuel consumption cannot be zero.")
        return None

def calculate_fuel_cost(fuel, price_per_liter):
    """Calculate the total cost of the fuel consumed."""
    try:
        total_cost = fuel * price_per_liter
        return total_cost
    except ValueError:
        print("Invalid input. Fuel or price must be a positive number.")
        return None

def bike_mileage_calculator():
    print("Welcome to the Bike Mileage Calculator with Fuel Cost in BDT!")
    
    while True:
        try:
            # Get user input for distance, fuel, and price per liter
            distance = float(input("\nEnter the distance traveled (in kilometers or miles): "))
            fuel = float(input("Enter the fuel consumed (in liters or gallons): "))
            price_per_liter = float(input("Enter the price of fuel per liter (in BDT): "))
            
            # Calculate the mileage
            mileage = calculate_mileage(distance, fuel)
            
            if mileage:
                print(f"\nYour bike mileage is: {mileage:.2f} units of distance per unit of fuel")
                
                # Calculate the fuel cost in BDT
                total_cost = calculate_fuel_cost(fuel, price_per_liter)
                if total_cost is not None:
                    print(f"Total cost of the fuel for this trip: BDT {total_cost:.2f}")
            else:
                print("Error: Could not calculate mileage.")
                
            # Ask if the user wants to calculate again
            calculate_again = input("\nDo you want to calculate again? (yes/no): ").lower()
            if calculate_again != 'yes':
                break

        except ValueError:
            print("Invalid input. Please enter numerical values for distance, fuel, and price.")

if __name__ == "__main__":
    bike_mileage_calculator()
