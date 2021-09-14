# 5-6 Calories From Fat And Carbohydrates

# A nutritionist who works for a fitness club helps members by evaluating their diets.
# As part of her evaluation, she asks members for the number of fat grams and
# carbohydrate grams that they consumed in a day. Then, she calculates the number
# of calories that result from the fat, using the following formula:
#       calories from fat = fat grams * 9
# Next, she calculates the number of calories that result from the carbohydrates,
# using the following formula:
#       calories from carbs = carb grams * 4
# The nutritionist asks you to write a program that will make these calculations.

# Main function.
def main():
    fat_grams = int(input('Enter the amount of fat grams consumed in a day: '))
    carbo_grams = int(input('Enter the amount of carbohydrate grams consumed in a day: '))
    cals_from_fat(fat_grams)
    cals_from_carbs(carbo_grams)

# Calculate the fats using the cals_from_fat function.
def cals_from_fat(fats):
    fat_cals = fats * 9
    print('Amount of calories consumed from fats: ',
          format(fat_cals, ','))

# Calculate the carbs using the cals_from_carbs function
def cals_from_carbs(carbs):
    carb_cals = carbs * 4
    print('Amount of calories consumed from carbohydrates: ',
          format(carb_cals, ','))

# Call the main function.
main()