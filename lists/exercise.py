sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []
profit = 1.50

# Add another day to week 2 list by capturing a number as input
add = input('Add a sales number  for the additional day:')
sales_w2.append(int(add))
print(sales_w2)
# Combine the two lists into the list called 'sales'
sales_w1.extend(sales_w2)
sales = sales_w1.copy()
# sales = sales_w1 + sales_w2
sales.sort()
print(sales)
# Calculate/ print how much you have earned on:
# * the best day separately
best = sales [-1] * 1.5
print('The best day of profit is: ' + str(best))
# * the worst day
worst = sales [0] * 1.5
print('The worst day of profit is: ' + str(worst))
#and in total
total = best + worst
print('Total best + worst is: ' + str(total))