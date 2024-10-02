"""
Sum functions
"""

test_list = [1, 5, 7]

answer = sum(test_list)

def sum(input_list):
    """User defined sum"""

    add = 0
    for i in input_list:
        add += i
    
    return add

def mean(my_list):

    from numpy import sum

    my_sum = sum(my_list)

    my_average = my_sum / len(my_list)

    return my_average

def squared_sum(my_list):

    add = sum(my_list)

    squared = add ** 2

    return squared

mean( [ squared_sum([1, 4, 5]), sum(test_list) ] )