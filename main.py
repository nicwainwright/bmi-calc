# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:20:04 2019

@author: nicwainwright

BME547 Homework 3
BMI Calculator

Sources:
BMI math gotten from: http://bmi.emedtv.com/bmi/how-to-calculate-bmi.html
BMI ranges gotten from: https://www.builtlean.com/2013/07/17/bmi-chart/
"""


def getWeight():
    NAN = True  # not a number. will become false once valid weight inputted
    while NAN:
        weight = input("Enter weight in lbs or kg (ex: '175' or '65'):\n")
        try:
            # this will fail if alpha characters have been entered
            weight = float(weight)
            if (weight<0):
                print('Invalid input. No negative values or '
                  'non-numbers allowed\n')
                continue
            NAN = False
        except ValueError:
            print('Invalid input. No negative values or '
                  'non-numbers allowed\n')

    # not a unit. will become false once valid weight type inputted
    NAU = True
    while NAU:
        weight_type = input("What unit of weight? Please type 'lbs' "
                            "or 'kg':\n")
        # make lower to allow for capital typing
        weight_type = weight_type.lower()
        try:
            if (weight_type == 'lbs' or weight_type == 'kg'):
                NAU = False
            else:
                print("Invalid input. Please type either 'lbs' or 'kg'\n")
                continue
        except:
            print("Invalid. Try Again\n")
    return weight, weight_type


def getHeight():
    NAN = True  # not a number. will become false once valid height inputted
    while NAN:
        height = input("Enter height in inches or meters (ex: '71' "
                       "or '1.70'):\n")
        try:
            # this will fail if alpha characters have been entered
            height = float(height)
            if (height<0):
                print('Invalid input. No negative values or '
                  'non-numbers allowed\n')
            NAN = False
        except ValueError:
            print('Invalid input. No negative values or non-numbers allowed\n')

    NAU = True  # not a unit. becomes false once valid height type inputted
    while NAU:
        height_type = input("What unit of height? Please type 'in' or 'm': \n")
        height_type = height_type.lower()  # allow for capital typing
        try:
            if (height_type == 'in' or height_type == 'm'):
                NAU = False
            else:
                print("Invalid input. Please type either 'in' or 'm'\n")
                continue
        except:
            print("Invalid. Try Again.\n")
    return height, height_type


def calcBMI(weight, weight_type, height, height_type):
    # BMI calculation is much simpler when in Metric form
    # so if either height or weight is English, then convert
    if weight_type == 'lbs':
        weight = weight*0.45359237
    if height_type == 'in':
        height = height*0.0254
    BMI = weight/(height**2)
    print('Your BMI is: {}'.format(round(BMI, 2)))
    return round(BMI, 2)


def youFat(BMI):
    if BMI < 18.5:
        category = 'underweight'
    elif BMI >= 18.5 and BMI < 25:
        category = 'normal'
    elif BMI >= 25 and BMI < 30:
        category = 'overweight'
    elif BMI > 30:
        category = 'obese'
    print('You are', category, 'according to the CDC.')
    return category


def main():
    # take inputs of height and weight and clairfy if metric or not
    weight, weight_type = getWeight()
    height, height_type = getHeight()
    # print confirmation message
    print('You said you are', weight, weight_type, 'and', height, height_type)
    # get BMI
    BMI = calcBMI(weight, weight_type, height, height_type)
    # get grouping
    category = youFat(BMI)


if __name__ == "__main__":
    main()
