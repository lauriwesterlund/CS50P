def main():

    # Define fruits' nutritional values as a dictionary
    items = [
        {"item": "apple", "nutrition": "130"},
        {"item": "avocado", "nutrition": "50"},
        {"item": "banana", "nutrition": "110"},
        {"item": "cantaloupe", "nutrition": "50"},
        {"item": "grapefruit", "nutrition": "60"},
        {"item": "grapes", "nutrition": "90"},
        {"item": "honeydew melon", "nutrition": "50"},
        {"item": "kiwifruit", "nutrition": "90"},
        {"item": "lemon", "nutrition": "15"},
        {"item": "lime", "nutrition": "20"},
        {"item": "lime", "nutrition": "20"},
        {"item": "nectarine", "nutrition": "60"},
        {"item": "orange", "nutrition": "80"},
        {"item": "peach", "nutrition": "60"},
        {"item": "pear", "nutrition": "100"},
        {"item": "pineapple", "nutrition": "50"},
        {"item": "plums", "nutrition": "70"},
        {"item": "strawberries", "nutrition": "50"},
        {"item": "sweet cherries", "nutrition": "100"},
        {"item": "tangerine", "nutrition": "50"},
        {"item": "watermelon", "nutrition": "80"},
    ]

    # Prompt user for input, strip whitespace and turn into lowercase
    fruit = input("Item : ").strip().lower()

    # Iterate through the dictionary to find the item matching the user's input
    # If found, print out the nutritional value attached to it
    # Otherwise, nothing happens
    for item in items:
        if item["item"] == fruit:
            print("Calories: " + item["nutrition"])

main()