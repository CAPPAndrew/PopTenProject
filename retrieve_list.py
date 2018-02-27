import csv
import pickle
import pandas as pd

def find_list(category):
    with open('food.pickle', 'rb') as f:
        food_dict = pickle.load(f)
    print("food_dict assembled")

    with open('restaurant.pickle', 'rb') as g:
        restaurant_dict = pickle.load(g)
    print("restaurant_dict assembled")

    category_list = food_dict[category]
    print(len(category_list))
    restaurant_list = []

    for UID in category_list:
        restaurant = restaurant_dict[UID]
        restaurant_list.append(restaurant)


    return restaurant_list
