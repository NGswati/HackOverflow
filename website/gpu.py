import random
import csv

# create an empty dictionary
data = {}

# add random values to the dictionary
data['price'] = [random.uniform(2000, 70000) for i in range(400)]
data['rating'] = [random.randint(0, 5) for i in range(400)]
data['reviews'] = [random.randint(0, 100) for i in range(400)]

# write to csv file
with open('gpu_train.csv', 'w', newline='') as csvfile:
    fieldnames = ['price', 'rating', 'reviews']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(400):
        writer.writerow({'price': data['price'][i], 'rating': data['rating'][i], 'reviews': data['reviews'][i]})
