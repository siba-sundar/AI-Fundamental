import random
import time


class RestaurantAgent:
    def __init__(self):
        self.restaurants = [
            {"name": "Pizza Palace", "type": "Italian", "price": "cheap"},
            {"name": "Sushi Express", "type": "Japanese", "price": "medium"},
            {"name": "Taco House", "type": "Mexican", "price": "cheap"},
            {"name": "Burger King", "type": "American", "price": "cheap"},
            {"name": "Fusion Grill", "type": "Modern", "price": "expensive"}
        ]

    def recommend_restaurants(self, cuisine=None, price=None):
        matching_restaurants = []

        for r in self.restaurants:
            if cuisine is not None:
                if r["type"].lower() != cuisine.lower():
                    continue
            if price is not None:
                if r["price"].lower() != price.lower():
                    continue
            matching_restaurants.append(r)

        return matching_restaurants


def generate_user_preferences():
    cuisines = ["Italian", "Japanese", "Mexican", "American", "Modern", None]
    prices = ["cheap", "medium", "expensive", None]

    while True:
        time.sleep(random.randint(2, 4))

        c = random.choice(cuisines)
        p = random.choice(prices)

        return c, p

def main():
    agent = RestaurantAgent()

    while True:
        cuisine, price = generate_user_preferences()

        print("\nUser is looking for a restaurant...")
        print("Cuisine preference: ", cuisine if cuisine else "Any")
        print("Price preference: ", price if price else "Any")

        matches = agent.recommend_restaurants(cuisine, price)

        print("\nHere are some recommendations:")
        if len(matches) > 0:
            for m in matches:
                print(m["name"], " - ", m["type"], "cuisine, ", m["price"], " price")
        else:
            print("No matching restaurants found.")

        print("-----------------------------------")


if __name__ == "__main__":
    main()
