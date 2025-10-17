import requests
def cal_api():
    product=input("Enter a food : ")
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={product}&search_simple=1&action=process&json=1"
    return url


 
def search_product(link):
    response = requests.get(link)
    data = response.json()
    
    if "products" in data and len(data["products"]) > 0:
        item = data["products"][0]
        name = item.get("product_name", "Unknown")
        nutriments = item.get("nutriments", {})
        calories = nutriments.get("energy-kcal_100g", 0)
        protein_100g = nutriments.get("proteins_100g", 0)
        carbs_100g = nutriments.get("carbohydrates_100g", 0)
        fat_100g = nutriments.get("fat_100g", 0)
        print("WUU")
        return calories, protein_100g, carbs_100g, fat_100g
    
    else:
        print("We couldn't find anything")
        return None, None, None, None
    
    
    
def portion():
    ask_grams=float(input("How many grams did you consume?"))
    return ask_grams
    


def personalize_gr(cal,prote_gr,carb_gr,fat_gr,grams):
    total_cal=(cal*grams)/100
    total_prote=(prote_gr*grams)/100
    total_carb=(carb_gr*grams)/100
    total_fat=(fat_gr*grams)/100
    return total_cal,total_prote,total_carb,total_fat



#calling functions 
#url=cal_api()
#calories, protein_100g, carbs_100g, fat_100g=search_product(url)
#ask_grams=portion()
#personalize_gr(calories,protein_100g, carbs_100g, fat_100g,ask_grams)

    


