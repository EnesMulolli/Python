import numpy as np
import pandas as pd

arr_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr_2d)

element = arr_2d[1,2]
print(element)

dimension = arr_2d.ndim
print(dimension)

arr_size = arr_2d.size
print(arr_size)


products = ['apples', 'oranges', 'tangerine', 'pears']

sales = [150, 200, 350, 90]


sales_series = pd.Series(sales, index=products)

print(sales_series)

total_sales = sales_series.sum()

print(total_sales)

best_selling_product = sales_series.idxmax()
highest_number = sales_series.max()

print(f"Best Selling product is: {best_selling_product}, with : {highest_number}")