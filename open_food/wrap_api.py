from open_food.spoon import cal_api,search_product,portion,personalize_gr
from open_food.show_ingr import product_macro


def calling():
    
    url = cal_api()


    calories, protein_100g, carbs_100g, fat_100g = search_product(url)

    grams = portion()

    total_cal, total_prote, total_carb, total_fat = personalize_gr(
        calories, protein_100g, carbs_100g, fat_100g, grams
    )

    product_macro(total_cal, total_prote, total_carb, total_fat)
    return total_cal, total_prote, total_carb, total_fat