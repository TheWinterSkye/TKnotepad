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

# def logger(msg):

#     def log_message():
#         print('Log: ', msg)
#     return log_message

# log_hi = logger('Hi!')
# log_hi()

# def html_tag(tag):

#     def  wrap_text(msg):
#          print('<{0}>{1}</{0}>'.format(tag, msg))

#     return wrap_text

# print_h1 = html_tag('h1')
# print_h1('Text Headline!')
# print_h1('Another Headline!')

# print_p = html_tag('p')
# print_p('Test Paragraph!')

# Python Clossures

def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    
    return inner_function

hi_func = outer_function('Hi!')
hello_func = outer_function('Hello!')
hi_func()
hello_func()