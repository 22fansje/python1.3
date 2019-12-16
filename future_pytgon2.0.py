#!/usr/bin/env python3
        
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def get_float(prompt, lowvalue, highvalue):
    value = float(input(prompt))
    while value <= lowvalue or value <= highvalue:
        print("Number must be greater than", lowvalue, "and less than or equal to", highvalue, "please try again.")
        value = float(input(prompt))
    
    return value
    
def get_int(prompt, low, high):
    value = int(input(prompt))
    while value <= low or value <= high:
        print("Number must be greater than", low, "and less than or equal to", high, "please try again.")
        value = int(input(prompt))
    
    return years

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float("Enter monthly investment: ", 0,1000)

        yearly_interest_rate = get_float("Enter yearly investment: ", 0,15)

        years = get_int("Enter number of years: ", 0,50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
