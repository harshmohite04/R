class Dish:
    def __init__(self, dish_name, price, cuisine_type):
        self.dish_name = dish_name
        self.price = price
        self.cuisine_type = cuisine_type

    def display_info(self):
        print(f"Dish: {self.dish_name}, Price: ${self.price:.2f}, Cuisine Type: {self.cuisine_type}")


class Appetizer(Dish):
    def __init__(self, dish_name, price, cuisine_type, is_spicy):
        super().__init__(dish_name, price, cuisine_type)
        self.is_spicy = is_spicy

    def display_info(self):
        super().display_info()
        print(f"Is Spicy: {'Yes' if self.is_spicy else 'No'}")


class VegetarianAppetizer(Appetizer):
    def __init__(self, dish_name, price, is_spicy):
        super().__init__(dish_name, price, cuisine_type="Vegetarian", is_spicy=is_spicy)


# Example usage:
if __name__ == "__main__":
    # Create instances of classes
    dish1 = Dish("Pasta", 12.99, "Italian")
    appetizer1 = Appetizer("Spring Rolls", 7.99, "Asian", True)
    veg_appetizer1 = VegetarianAppetizer("Bruschetta", 5.99, False)

    # Display information
    dish1.display_info()
    print("\n")
    appetizer1.display_info()
    print("\n")
    veg_appetizer1.display_info()
