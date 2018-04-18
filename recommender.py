import pandas as pd
import numpy as np

data = pd.read_csv('orders.csv')
user_products = dict()
products_user = dict()
users = set()
products = set()

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
    products.add(product)
    users.add(user)
    if user.id not in user_products.keys():
        user_products[user.id] = {product}
    else:
        user_products[user.id].add(product)
    if product.id not in products_user.keys():
        products_user[product.id] = {user}
    else:
        products_user[product.id].add(user)


def jaccard_coeff(user1, user2):
    products1 = user_products[user1]
    products2 = user_products[user2]
    intersection = products1.intersection(products2)
    union = products1.union(products2)
    return len(intersection) / len(union)


def like_coeff(user, product):
    sum = 0.0
    for u in products_user[product]:
        if user != u.id:
            sum += jaccard_coeff(user, u.id)
    return sum / len(products_user[product])


user = 4063
recommendations = list()

for p in products:
    coeff = like_coeff(user, p.id)
    recommendations.append((p, coeff))

recommendations = sorted(recommendations, key=lambda x:x[1], reverse=True)

for i in range(0, 5):
    print(str(recommendations[i][0]) + " " + str(recommendations[i][1]))




