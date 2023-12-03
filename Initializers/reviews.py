# - `Review __init__()`
#   - Reviews should be initialized with a customer, restaurant, and a rating (a number)
# - `Review rating()`
#   - returns the rating for a restaurant.
# - `Review all()`
#   - returns all of the reviews
class Review:
    reviews_list = []  

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self._rating = rating  
        Review.reviews_list.append(self)  

    @classmethod
    def get_all_reviews(cls):  
        return cls.reviews_list
    
    def set_rating(self, new_rating):
        if isinstance(new_rating, int):
            self._rating = new_rating
        else:
            print(" must be an integer")
    def __str__(self):
        return f"Review: Customer - {self.customer}, Restaurant - {self.restaurant}, Rating - {self._rating}"
