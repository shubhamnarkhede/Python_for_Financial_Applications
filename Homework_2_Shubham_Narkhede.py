# %% [markdown]
# # 1 Loop Practice: Gradient Decent (30 pts)
# 
#     In statistics, linear regression is a linear approach to modelling the relationship between a dependent variable and one or more independent variables. Let X be the independent variable and Y be the dependent variable. We will define a linear relationship between these two variables as follows:
#         Y = wX + c
#     This is the equation for a line that you studied in high school. w is the slope of the line and c is the y intercept. Today we will use this equation to train our model with a given dataset and predict the value of Y for any given value of X.Our challenge today is to determine the value of w and c, such that the line corre-sponding to those values is the best fitting line or gives the minimum error. One way to solve this problem is to use Gradient Decent (The reference here contain more details of Gradient decent and sample code, try not use numpy in this question):
# 
#     You don’t need the knowledge of optimization to finish the question. Please just implement the following algorithm step by step. The Algorithm of gradient decent to find w and c is :
# 
#         1.Set initial variable. w=0 and c=0, Learning rate L=0.001, number of iterations.
#         2. Write a for loop, in this loop, go over all pair (xi, yi):
#         (a) calculate ypred
#         i = xi ∗ w + c
#         (b) calculate xi(ypred
#         i − yi), and store it in list Dw
#         (c) calculate (ypred
#         i − yi), and store it in list Dc
#         3. calculate the average for list Dw and Dc, and assign the values to dw and dc
#         respectively.
#         4. update m by: w = w − L × dw
#         5. update c by: c = c − L × dc
#         6. (Bonus 3 pts) What you have done above are one iteration of gradient descent,
#         once you repeat from step 2 to 5 again and again, the w and c will be converged
#         to the true value. Can you wrap them in big loop for 200 iteration?
#         you can test your result by using following dataset
#         input:
#         x = [0.18, 1.0, 0.92, 0.07, 0.85, 0.99, 0.87]
#         y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
#         Output:
#         for one iteration
#         w = 0.10275336, c = 0.13336
#         for 200 iterations:
#         w = 17.72481065, c = 22.97599012903927

# %%
# Define the input data
x = [0.18, 1.0, 0.92, 0.07, 0.85, 0.99, 0.87]
y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]


# %%
#Set varibales 
w = 0
c = 0
learning_rate = 0.001
iterations = 200
dw = 0
dc = 0

#Loop to do calculation on all datapoint
for xi, yi in zip(x, y):
    y_pred = xi * w + c
    dw += xi * (y_pred - yi)
    dc += (y_pred - yi)
    
dw /= len(x)
dc /= len(x)
w -= learning_rate * dw
c -= learning_rate * dc


# Print the result
print("w =", w)
print("c =", c)


# %% [markdown]
# BONUS

# %%
w = 0
c = 0

# Implement gradient descent for 200 iteration
for _ in range(iterations):
    dw = 0
    dc = 0
    for xi, yi in zip(x, y):
        y_pred = xi * w + c
        dw += xi * (y_pred - yi)
        dc += (y_pred - yi)
    dw /= len(x)
    dc /= len(x)
    w -= learning_rate * dw
    c -= learning_rate * dc

# Print the result
print("w =", w)
print("c =", c)


# %% [markdown]
# # 2 Control Flow Practice: Element-wise logical opera-tions (30 pts)
#     
#         1. (10 pts) Given two same-length lists of bool-type variables (True/False), you need to implement the element-wise and, or, and not operations. Element-wise means the operations are applied to each pair of two element, and the results form another list. 
#         In the following sample code, the first element in result and is False because x[0] and y[0] equals False (True and False == False). Complete the following code to obtain the three lists.
#         x = [True, True, False, False, True, False, True]
#         y = [False, True, True, True, False, False, True]
#         <complete the code>
#         # return three lists: result_and, result_or, result_not_x which are
#         # respectively the result of element-wise AND, element-wise OR,
#         # and element-wise NOT
#         # result_and is [False, True, False, False, False, False, True]
#         # result_or is [True, True, True, True, True, False, True]
#         # result_not_x is [False, False, True, True, False, True, False]
#         
#         You need to use FOR loop to do this. A hint is to check zip() function which can zip two same-length lists to pairs. Check the link: https://docs.python.org/3.7/library/functions.html#zip.
#         
#         
# 

# %%
x = [True, True, False, False, True, False, True]
y = [False, True, True, True, False, False, True]


# %%

# Initialize result lists
result_and = []
result_or = []
result_not_x = []

# Perform element-wise AND, OR, and NOT using for loop and zip
for x_val, y_val in zip(x, y):
    result_and.append(x_val and y_val)
    result_or.append(x_val or y_val)
    result_not_x.append(not x_val)

# Print the results
print("result_and =", result_and)
print("result_or =", result_or)
print("result_not_x =", result_not_x)


# %% [markdown]
# 2.2
#     
# (10 pts) Implement another operation: given a list of bool-type variables If True takes 40% or more of the total number of element of this list,give True as the result, otherwise give False. For an example,
# 
#             x = [True, True, False, False, True]
# 
#             y = [True, False, False, False, False]
# 
#             # your code gives True for x, as True takes 3/5 (60%>=40%)
# 
#             # your code gives False for y, as True takes 1/5 (20%<40%)
# 

# %%
def check_majority_true(lst):
    true_count = lst.count(True)
    return true_count / len(lst) >= 0.4


# %%
x = [True, True, False, False, True]
y = [True, False, False, False, False]

# %%
result_x = check_majority_true(x)
result_y = check_majority_true(y)

print("Result for x:", result_x)
print("Result for y:", result_y)

# %% [markdown]
# # 3 Practice Dictionary (20 pts)
#         1. (2pts) Define a string of ‘python is an interpreted dynamic programming language’
#         2. (3pts) Create a list (list A) of single-character strings out of the above string in 1 (e.g., ’hello’->[’h’, ’e’, ’l’, ’l’, ’o’]).
#         3. (8pts) Write a loop to count the number of each unique character(ignore spaces) into dictionary, where your keys are characters in the list A, and value is the count corresponding to each character. Your result should look like : {’h’: 1, ’e’: 1, ’l’: 2, ’o’: 1}.
#         4. (7pts) Print the characters which shows up more than 1 time. (Hint: use loop and
#         if statement).

# %%
input_string = 'python is an interpreted dynamic programming language'


# %%
list_A = [char for char in input_string if char != ' ']


# %%
list_A

# %%
# Initialize an empty dictionary to store character counts
char_count = {}

# Iterate through the characters in list_A
for char in list_A:
    # Check if the character is already in the dictionary
    if char in char_count:
        # If it is, increment the count
        char_count[char] += 1
    else:
        # If it's not, add it to the dictionary with a count of 1
        char_count[char] = 1

# Print the character counts
print(char_count)


# %%
for char, count in char_count.items():
    if count > 1:
        print(char)


# %% [markdown]
# # 4 Loop Practice: Sum (20 pts)
# 
# Write a loop for calculate the average of a list. For example: if you have a  list A = [1, 2, 3, 4, 5, 6], after your loop calculation, you need to get a total num equals to 3.5.
# 

# %%
# Define a list
A = [1, 2, 3, 4, 5, 6]


# %%
# Initialize variables for sum and count
total_sum = 0
count = 0

# Calculate the sum and count using a loop
for num in A:
    total_sum += num
    count += 1

# Calculate the average
average = total_sum / count

# Print the average
print("Average:", average)



