# -*- coding: utf-8 -*-
"""Data_Science_Exercises_part_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19PDefQ082PksR1MPdr1wTwdoQN3Q0tS4

**Note that you cannot and should not use loops in any of this HW. Use the cool numpy functions and become a Pythonista :)**
"""

import numpy as np

"""## Q1

Make a list of the max temperatures for the last month (June) in Philadelphia.

This is a multi-step process.  

Please follow these instructions in order.

1.  Visit the following URL https://www.wunderground.com/history/monthly/us/pa/philadelphia/KPHL/date/2022-6. 
2.  Scroll down and select all the daily weather information using your mouse. Copy it.
3. Open up Excel. Paste the data. (If you do not have Excel, you can get it through Penn from here: https://www.isc.upenn.edu/how-to/penno365-office-365-proplus#Getting-started). You can also do this in Google sheets if you prefer that
4.  Select and copy the max temperature column, not including the column header.
5.  Open up the website [delim.co](http://delim.co) and paste the column in the ”Column Data Here” box on the left.  Click the blue arrow pointing right.  In the ”Delimited Data Here” box on the right, you will now have a comma-separated list of max temperatures for the last month.

Create a max-temperature **array** in the cell below. Remember to store it in a variable.
"""

max_temp = np.array([87,87,80,85,79,82,79,85,84,81,74,80,90,84,87,77,95,79,77,82,81,77,73,83,90,90,81,80,87,90])

"""Write code to print average maximum temp:"""

average_max_temp = sum(max_temp) / len(max_temp)
print(average_max_temp)

"""Write code to print median maximum temp:"""

max_temp.sort()
median_max_temp = max_temp[len(max_temp)//2]
print(max_temp)
print(median_max_temp)

"""Write code to print the variance of max temps:"""

variance = average_max_temp - max_temp
print(abs(variance))

"""Write code to print the standard deviation of max temps:"""

print(np.std(max_temp))

"""## Q2

From the max temperatures array, select the portion of the array that has temperatures in the range 85-95 F (with both endpoints included).

Select portion of array with temps from 85-95
"""

partArray = max_temp[(max_temp >= 85) & (max_temp <= 95)]
print(partArray)

"""How many such days did Philly have in June?"""

print(len(partArray))

"""## Q3

From your original data, extract the mean temperature and the mean humidity information into 2 new arrays.  Use these two arrays to compute the number of days that were uncomfortable in the last month.  We'll define an uncomfortable day as one where the mean temperature is above 80 degrees and the humidity is over 70 percent.

Create arrays for mean temp and mean humidity:
"""

mean_temp = np.array([75,72.9,74.2,75.3,71.2,71.4,71.7,76.4,74.6,73.5,70.8,69,80.3,75.5,76.4,70.7,81.4,71,67.4,70.7,72.5,70.3,67.5,71.6,79.5,80.8,77,74.5,76.8,80.8])
mean_humidity = np.array([70.3,79.3,64.3,40.3,35.3,44,66.7,73.4,75.5,45.6,61.6,82,68,54.5,59.8,78.7,60.1,44.3,34.8,35.6,56.3,75.4,82,74.4,63.6,59.6,80,47.4,57.7,53.2])

"""Print number of "uncomfortable" days. You do not need to do this in one cell. Feel free to add more cells if needed."""

mean_temp_idx = np.where(mean_temp >= 80)
print(mean_temp_idx)
mean_humidity_idx = np.where(mean_humidity >= 70)
print(mean_humidity_idx)
finalAns = np.where(mean_temp_idx in mean_humidity_idx)

print(len(finalAns) - 1)

"""## Q4

What is the total amount of rain that Philly got in August? Please add code cells to compute this.
"""

totalRainArr = np.array([0.00,0.00,1.04,0.00,0.00,0.00,0.00,0.07,1.99,0.00,0.00,0.51,0.20,0.00,0.13,0.13,0.11,0.00,0.00,0.00,0.00,0.01,0.00,0.33,0.00,0.00,0.00,0.50,0.00,0.00])
print(sum(totalRainArr))

"""## Q5

Use the same process as above to get data for a city of your choice. The website has most major cities 
(international cities included).

Now, for the city that you picked, what was the total rainfall in the month of June. In terms of total rainfall, did it rain more in your city or in Philly.

Begin by telling us in a markdown cell, which city you picked
"""

# Picked Irvine, CA

"""Then get the rainfall data in an array"""

IRainfall_data = np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00])

"""Compute the total"""

print(sum(IRainfall_data))

"""Which city had more rain?"""

if sum(IRainfall_data) > sum(totalRainArr):
  print("Irvine")
else:
  print("Philly")

"""## Q6

Compute the factorial of 25 (25!). **You are not allowed to use math.factorial**. Try and do this with one single line of code.


*This one is a little tricky because of the fact that there is a such a thing as a maximum integer*
"""

print(np.prod(np.arange(1, 26), dtype=np.float64))

"""Make your factorial-computing code more general by taking in an input. Ask the user to input a number and then compute and print the factorial. Please feel free to add cells in order to complete the problem below."""

user_input = int(input("Give me a number: "))
print(np.prod(np.arange(1, user_input+1)))

"""## Q7

Compute the sum of the squares of integers from 1 to 10. Again, try and do this in 1 line using numpy functions
"""

print(np.sum(np.arange(1, 11) ** 2))

"""## Q8

Math claims that 1 + 0.5 + 0.25 + 0.125 + 0.0625 + .....  is supposed to converge to 2.

Write code that sums the first 50 terms of this series (1 + 0.5 + 0.25 would be considered the sum of the first 3 terms). How close does it get to 2?

A one cell answer is ideal, but feel free to break it into multiple cells (no points will be deducted)
"""

print(1 + sum(1 / (2 ** np.arange(1, 51))))

"""Estimate the fundamental math constant **e** via the following formula

$$
\begin{align*}
e = 1 + \frac{1}{1!} + \frac{1}{2!} + \ldots + 
\end{align*}
$$

We expect you to use the **vectorization of math.factorial** for this question. 

We do not require you to do this in one line. Feel free to add extra cells.
"""

import scipy.special as fact

print(1 + sum(1 / fact.factorial(np.arange(1, 200)))) #21 is the biggest number to the point it does not break
