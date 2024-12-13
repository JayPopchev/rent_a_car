def initialize_cars(): # car catalogue
    cars = [
      { "id": 1, "brand": "Toyota", "model": "Camry", "rental_price": 40, "available": True },
      { "id": 2, "brand": "Honda", "model": "Civic", "rental_price": 35, "available": False },
      { "id": 3, "brand": "Ford", "model": "Focus", "rental_price": 30, "available": True },
      { "id": 4, "brand": "Chevrolet", "model": "Malibu", "rental_price": 45, "available": True },
      { "id": 5, "brand": "Nissan", "model": "Altima", "rental_price": 38, "available": False },
      { "id": 6, "brand": "Hyundai", "model": "Sonata", "rental_price": 42, "available": True },
      { "id": 7, "brand": "Kia", "model": "Optima", "rental_price": 37, "available": True },
      { "id": 8, "brand": "Mazda", "model": "Mazda3", "rental_price": 34, "available": False },
      { "id": 9, "brand": "Subaru", "model": "Legacy", "rental_price": 39, "available": True },
      { "id": 10, "brand": "Volkswagen", "model": "Passat", "rental_price": 43, "available": True }
    ]
    return cars


def return_a_car(cars):
      """Return a car."""
      car_id = int(input("Please choose a car id: "))
      for car in cars:
          if car["id"] == car_id and not car["available"]: # checks for id and viability
            car["available"] = True # Changes the car viability
            return f"You have returned the {car['brand']} {car['model']} and you need to pay {car['rental_price']}."
      return "Car is available or invalid car ID."


def rent_car(cars):
      """Rent a car."""
      car_id = int(input("Please choose a car id: "))
      for car in cars:
          if car["id"] == car_id and car["available"]: # checks for id and viability
              car["available"] = False # Changes the car viability
              return f"You have rented the {car['brand']} {car['model']}."
      return "Car is unavailable or invalid car ID."


def display_cars(cars):
    """Display all cars."""
    print("\nAvailable Cars:")
    for car in cars:
        status = "Available" if car["available"] else "Rented" # add a car status
        print(f"ID: {car['id']} - {car['brand']} {car['model']} - ${car['rental_price']}/day - {status}") # prints the car catalogue


def main_menu():
    """Display the main menu."""
    print("Welcome to RentACar!")
    print("1. View Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    choice = int(input("Please choose an option (1-4): "))
    return choice

def main():
      """Main function to run the rent a car system."""
      car_catalogue = initialize_cars() # sets up a name for the function
      # Process user input based on their choice
      while True:
          choice = main_menu()
          if choice == 1: # Display the menu
              display_cars(car_catalogue)
          elif choice == 2: # Rent a car option
              print(rent_car(car_catalogue))
          elif choice == 3: # Return a car option
              print(return_a_car(car_catalogue))
          elif choice == 4: # Exit option
              print("Thanks for using our service!") # Nice words for goodbye
              break
