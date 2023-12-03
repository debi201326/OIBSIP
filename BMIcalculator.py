# function to calculate BMI
def calculate_BMI(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# function to classify bmi into different categories
def categories_BMI(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

# main function
def main():
    print("Welcome to the BMI Calculator")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_BMI(weight, height)
    print(f'Your BMI is :  {bmi:.2f}')

    category = categories_BMI(bmi)
    print(f'You are categorized as: {category}')

if __name__ == '__main__':
    main()
