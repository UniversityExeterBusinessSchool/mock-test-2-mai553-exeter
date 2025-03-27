#######################################################################################################################################################
# 
# Name: Nguyen Sao Mai
# SID: 740098557
# Exam Date: 27 March 2025
# Module: BEMM458 - Programming for Business Analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/bemm458-mock-test-mai553-exeter
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################

# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# Calculate and print the average sales.

# Calculate the average sales
average_sales = sum(weekly_sales) / len(weekly_sales)

# Print the average sales
print(f"Average sales: {average_sales}")

# Iterate through the list and check if each week's sales were above or below the average
for week, sales in enumerate(weekly_sales, start=1):
    if sales > average_sales:
        print(f"Week {week}: Sales ({sales}) were above average.")
    elif sales < average_sales:
        print(f"Week {week}: Sales ({sales}) were below average.")
    else:
        print(f"Week {week}: Sales ({sales}) were exactly average.")

# Explanation:
# 1. The average sales are calculated using the sum of the list divided by its length.
# 2. A for loop iterates through the weekly sales, and each week's sales are compared to the average.
# 3. The output specifies whether the sales were above, below, or equal to the average.

#######################################################################################################################################################

# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.

# Find the first and last occurrence of 'good'
good_start = customer_feedback.find('good')
good_end = good_start + len('good') if good_start != -1 else -1

# Find the first and last occurrence of 'improved'
improved_start = customer_feedback.find('improved')
improved_end = improved_start + len('improved') if improved_start != -1 else -1

# Store the positions in a list as tuples
positions = [
    ('good', (good_start, good_end)),
    ('improved', (improved_start, improved_end))
]

# Print the list of positions
print(positions)

# Explanation:
# 1. The `find` method is used to locate the first occurrence of the words 'good' and 'improved'.
# 2. The end position is calculated by adding the length of the word to its start position.
# 3. If the word is not found, `find` returns -1, and the end position is also set to -1.
# 4. The positions are stored as tuples in a list and printed.

#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.

# Question 3 - Functions for Business Metrics

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
def calculate_net_profit_margin(net_profit, revenue):
    if revenue == 0:
        return "Revenue cannot be zero."
    return (net_profit / revenue) * 100

# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
def calculate_cac(total_marketing_cost, new_customers_acquired):
    if new_customers_acquired == 0:
        return "New customers acquired cannot be zero."
    return total_marketing_cost / new_customers_acquired

# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
def calculate_nps(promoters, detractors, total_respondents):
    if total_respondents == 0:
        return "Total respondents cannot be zero."
    return ((promoters - detractors) / total_respondents) * 100

# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.
def calculate_roi(net_gain, investment_cost):
    if investment_cost == 0:
        return "Investment cost cannot be zero."
    return (net_gain / investment_cost) * 100

# Example calls with sample values (using student ID digits for customization)
net_profit_margin = calculate_net_profit_margin(7400, 98557)  # Example: Net Profit = 7400, Revenue = 98557
cac = calculate_cac(5000, 74)  # Example: Total Marketing Cost = 5000, New Customers Acquired = 74
nps = calculate_nps(50, 10, 74)  # Example: Promoters = 50, Detractors = 10, Total Respondents = 74
roi = calculate_roi(7400, 553)  # Example: Net Gain = 7400, Investment Cost = 553

# Print the results
print(f"Net Profit Margin: {net_profit_margin:.2f}%")
print(f"Customer Acquisition Cost (CAC): {cac:.2f}")
print(f"Net Promoter Score (NPS): {nps:.2f}%")
print(f"Return on Investment (ROI): {roi:.2f}%")

# Explanation:
# 1. Each function calculates a specific business metric using the provided formula.
# 2. Error handling is included to avoid division by zero.
# 3. Example values are based on the student's ID digits for customization.
# 4. The results are printed with two decimal places for clarity.

#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.
import pandas as pd

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.

import pandas as pd

# Sales data dictionary
sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(sales_data)

# Display the DataFrame
print("Sales Data:")
print(df)

# Calculate the cumulative monthly sales
df['Cumulative Sales'] = df['Sales'].cumsum()

# Display the DataFrame with cumulative sales
print("\nSales Data with Cumulative Sales:")
print(df)

# Explanation:
# 1. The `pd.DataFrame` function is used to create a DataFrame from the sales_data dictionary.
# 2. The `cumsum` method calculates the cumulative sum of the 'Sales' column.
# 3. A new column 'Cumulative Sales' is added to the DataFrame to store the cumulative sales.
# 4. The updated DataFrame is printed to show the cumulative sales for each month.

#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
prices = np.array([15, 18, 20, 22, 25, 27, 30]).reshape(-1, 1)  # Reshape for sklearn
demand = np.array([200, 180, 170, 160, 150, 140, 130])

# Create and train the linear regression model
model = LinearRegression()
model.fit(prices, demand)

# Predict the demand for a price of £26
predicted_demand = model.predict([[26]])
print(f"Predicted demand for price £26: {predicted_demand[0]:.2f} units")

# Plot the data points and regression line
plt.scatter(prices, demand, color='blue', label='Data Points')
plt.plot(prices, model.predict(prices), color='red', label='Regression Line')
plt.scatter([26], predicted_demand, color='green', label=f'Prediction (26, {predicted_demand[0]:.2f})')

# Add labels, title, and legend
plt.xlabel('Price (£)')
plt.ylabel('Demand (Units)')
plt.title('Price vs Demand - Linear Regression')
plt.legend()
plt.grid(True)
plt.show()

# Explanation:
# 1. The dataset is converted into NumPy arrays, and prices are reshaped to a 2D array for sklearn compatibility.
# 2. A LinearRegression model is created and trained using the prices and demand data.
# 3. The model predicts the demand for a price of £26.
# 4. A scatter plot of the data points and the regression line is created, with the prediction point highlighted.

#######################################################################################################################################################

# Question 6 - Error Handling
# You are given a dictionary of prices for different products.
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
# Include error handling in your function and explain where and why it’s needed.

# Function to calculate the total price of all items, skipping non-numeric values
def calculate_total_price(prices_dict):
    total_price = 0
    for product, price in prices_dict.items():
        try:
            # Attempt to add the price to the total
            total_price += float(price)
        except (ValueError, TypeError):
            # Handle non-numeric values by skipping them
            print(f"Skipping non-numeric price for product {product}: {price}")
    return total_price

# Calculate the total price
total_price = calculate_total_price(prices)

# Print the total price
print(f"Total price of all items: {total_price:.2f}")

# Explanation:
# 1. The function iterates through the dictionary and attempts to convert each price to a float.
# 2. If a ValueError or TypeError occurs (e.g., for non-numeric values), the exception is caught, and the item is skipped.
# 3. This ensures the program does not crash and continues processing valid prices.
# 4. The total price is returned and printed with two decimal places for clarity.

#######################################################################################################################################################

# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

import matplotlib.pyplot as plt
import random

# Generate 50 random numbers between 1 and 500
random_numbers = [random.randint(1, 500) for _ in range(50)]

# Plot a histogram
plt.hist(random_numbers, bins=10, color='blue', edgecolor='black')

# Add labels and title
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.title('Histogram of Random Numbers')

# Show the plot
plt.grid(True)
plt.show()

# Explanation:
# 1. The `random.randint` function generates 50 random integers between 1 and 500.
# 2. The `plt.hist` function creates a histogram with 10 bins to group the numbers into ranges.
# 3. Labels for the x-axis, y-axis, and a title are added for clarity.
# 4. The `plt.grid` function adds a grid to the plot for better visualization.

#######################################################################################################################################################

# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
# Print the original and the new lists.

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
doubled_quantities = [q * 2 for q in quantities if q >= 10]

# Print the original and the new lists
print("Original quantities:", quantities)
print("Doubled quantities (10 or more):", doubled_quantities)

# Explanation:
# 1. The list comprehension iterates through the `quantities` list.
# 2. For each quantity `q`, it checks if `q` is 10 or more.
# 3. If the condition is met, the quantity is doubled and added to the new list.
# 4. The original list remains unchanged, and the new list contains only the doubled values for quantities >= 10.

#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}
# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}

# Filter out products with a rating of less than 4
filtered_ratings = {product: rating for product, rating in ratings.items() if rating >= 4}

# Print the filtered dictionary
print("Filtered ratings (rating >= 4):", filtered_ratings)

# Explanation:
# 1. A dictionary comprehension is used to iterate through the `ratings` dictionary.
# 2. For each product and its rating, the condition `rating >= 4` is checked.
# 3. If the condition is met, the product and its rating are added to the new dictionary `filtered_ratings`.
# 4. The resulting dictionary contains only the products with a rating of 4 or higher.

#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:
values = [10, 20, 30, 40, 50]
total = 0
for i in values:
    total = total + i
average = total / len(values)
print("The average is" + average)

# Corrected Code:
values = [10, 20, 30, 40, 50]
total = 0

# Iterate through the list and calculate the total
for i in values:
    total += i  # Corrected syntax for adding to the total

# Calculate the average
average = total / len(values)

# Print the average with proper string formatting
print(f"The average is {average:.2f}")

# Explanation of Fixes:
# 1. The original code attempted to concatenate a string with a float in `print("The average is" + average)`.
#    This caused a `TypeError`. Fixed by using an f-string for proper formatting.
# 2. The `+=` operator was used to simplify `total = total + i`.
# 3. The corrected code calculates the total and average correctly and prints the result with two decimal places.

# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.

#######################################################################################################################################################
