''' Description:
Narrows down restaurant choices based on
dietary restrictions provided by the user.'''

#Ask if anyone in the party is vegetarian
vegetarian = input("Is anyone in your party a vegetarian?")

#Convert response to lowercase for easier comparison
vegetarian = vegetarian.lower()

#Ask if anyone in the party is vegan
vegan = input("Is anyone in your party a vegan?")

#Convert response to lowercase
vegan = vegan.lower()

#Ask if anyone in the party is gluten free
gluten_free = input("Is anyone in your party gluten free?")

#Convert response to lowercase
gluten_free = gluten_free.lower()

#Store restaurant names in variables
restaurant4 = "Farmacy Vegan Kitchen"
restaurant3 = "Wood Fired Pizza Wine Bar"
restaurant2 = "Villaggio's Risorante Italiano"
restaurant1 = "Council Oak Steaks and Seafood"

#Display heading
print("Here are your restaurant choices:")

#If there are no dietary restrictions, display all restaurants
if vegan == 'no' and vegetarian == 'no' and gluten_free == 'no':
    print(restaurant1)
    print(restaurant2)
    print(restaurant3)
    print(restaurant4)

#If someone is vegan, only display vegan-friendly restaurant
elif vegan == 'yes':
    print(restaurant4)

#If someone is gluten free, display gluten-free options
elif gluten_free == 'yes':
    print(restaurant3)
    print(restaurant4)

#If someone is vegetarian, display vegetarian-friendly options
elif vegetarian == 'yes':
    print(restaurant2)
    print(restaurant3)
    print(restaurant4)
