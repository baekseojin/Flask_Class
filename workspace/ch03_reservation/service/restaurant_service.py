from model.restaurant import Restaurant

class RestaurantService:
    def __init__(self):
        self.restaurant = Restaurant()

    def get_restaurant(self):
        return self.restaurant.get_restaurant()
        