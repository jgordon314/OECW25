def recipe_search(data):
    return data

def find_meals(inp):
    all_meals = []
    meals = recipe_search(inp)
    for meal in meals:
        meal = meal['recipe']
        current_meal_information = []
        current_meal_information.append(meal['label'])  
        current_meal_information.append(meal['image'])
        current_meal_information.append(fixed_link(meal['shareAs']))
        all_meals.append(current_meal_information)
    return all_meals

def fixed_link(current_link):
    return str(current_link).replace("%0D%0A", "")