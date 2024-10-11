potions = {
    "Invisibility Potion": ["Moonstone", "Dragon Scale", "Fairy Dust"],
    "Flying Potion": ["Phoenix Feather", "Troll Tooth", "Mermaid Scale"],
    "Healing Potion": ["Unicorn Horn", "Elf Hair", "Golden Apple"]
}

print("Available potions:")
for i, potion in enumerate(potions.keys(), 1):
    print(f"{i}.{potion}")
    
choice = int(input("Enter the number of the potion you want to make: ")) - 1
chosen_potion = list(potions.keys())[choice]

print(f"\nYou have chosen to make the {chosen_potion}.")
ingredients = potions[chosen_potion]
purchased_ingredients = []

i = 0
while i < len(ingredients):
    ingredient = ingredients[i]
    buy = input(f"Do you want to buy {ingredient}? (yes/no): ").lower()
    
    if buy == 'yes':
        purchased_ingredients.append(ingredient)
        print(f"You have purchased the {ingredient}.")
        i += 1
    elif buy == 'no':
        print("Shopping has stopped.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        
if len(purchased_ingredients) == len(ingredients):
    print(f"\nCongratulations! You have purchased all of the required ingredients for the {chosen_potion}.")
    print("Ingredients purchased:", ", ".join(purchased_ingredients))
else:
    print("\nYou did not purchase all of the ingredients necessary. Better luck next time!")
    print("Ingredients purchased:", ", ".join(purchased_ingredients))