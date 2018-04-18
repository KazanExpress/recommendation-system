import pandas as pd
import numpy as np

data = pd.read_csv('orders.csv')
user_products = dict()
products_user = dict()

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return str(self.id) + ' ' + self.name


class Category:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __str__(self):
        return str(self.id) + ' ' + self.title


class Product:
    def __init__(self, id, title, category, is_in_favorites):
        self.id = id
        self.title = title
        self.category = category
        self.is_in_favorites = is_in_favorites

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return str(self.id) + ' ' + self.title


for index, row in data.iterrows():
    user = User(int(row['customer_id']), row['first_name'])
    category = Category(int(row['category_id']), row['category_title'])
    product = Product(int(row['product_id']), row['product_title'], category, row['is_in_favorites'])
    if user not in user_products:
        user_products[user] = {product}
    else:
        user_products[user].add(product)
    if product not in products_user:
        products_user[product] = {user}
    else:
        products_user[product].add(user)


