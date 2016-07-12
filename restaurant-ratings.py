# your code goes here
def sort_restaurant_ratings(path):
    ratings_input = open(path)
    restaurant_ratings = {}
    for line in ratings_input:
        restaurant = line.strip()
        new_restaurant = restaurant.split(":")
        # assigning the first value from the list new_restaurant to the key and the
        # second value from the list to the dictionary value. 
        restaurant_ratings[new_restaurant[0]] = new_restaurant[1]
    # restaurant_ratings was our dictionary; used the .items method to return a list of
    # tuples called new_restaurant_ratings
    new_restaurant_ratings = restaurant_ratings.items()
    # sorted our new list of tuples
    new_restaurant_ratings.sort()
    #iterated over each tuple to extract key and value to print restaurant and score
    for name, score in new_restaurant_ratings:
        print "{} is rated at {}.".format(name, score) 

sort_restaurant_ratings("scores.txt")