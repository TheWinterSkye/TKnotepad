# First Class Functions.
# def square(x):
#     return x * x


# Set the value of f to the function. Now you can treat f like a function.
# f = square

# print out function information, an entity which supports all the operations avail to other entities.
# print(square)
# print out the returned vaule from the square function
# print(f(5))

# def square(x):
#     return x * x

# def cube(x):
#     return x * x * x

# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result
    
# squares = my_map(cube, [1, 2, 3, 4, 5])

# print(squares)

def logger(msg):

    def log_message():
        print('Log: ', msg)
    return log_message

log_hi = logger('Hi!')
log_hi()