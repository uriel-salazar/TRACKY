from open_food.spoon import cal_api,search_product,portion,personalize_gr
from open_food.show_ingr import product_macro,csv_meal,food_added


def calling():
    url = cal_api()
    name,calories, protein_100g, carbs_100g, fat_100g = search_product(url)

    if calories is None:
        print("Your food couldn't be calculated")
        return None, None, None, None  # Stop here safely

    # If product found
    grams = portion()
    total_cal, total_prote, total_carb, total_fat = personalize_gr(
        calories, protein_100g, carbs_100g, fat_100g, grams
    )
    m_cal,m_prote,m_carb,m_fat=product_macro(total_cal, total_prote, total_carb, total_fat)
    file,meal_api=csv_meal(name,m_cal,m_prote,m_carb,m_fat)
    food_added(file)
    
    return total_cal, total_prote, total_carb, total_fat

