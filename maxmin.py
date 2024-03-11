# Challenge 3 - Task 2: 
# Given a list of integers, return the highest and lowest numbers in an array
# without using max() and min() 


def calculate_max_min(array_of_ints):
    print(array_of_ints)
    max = array_of_ints[0]
    min = array_of_ints[0]
    for i in range (len(array_of_ints)):
        if array_of_ints[i] > max:
            max = array_of_ints[i]
        if array_of_ints[i] < min:
            min = array_of_ints[i]

    result=[]
    result.append(min)
    result.append(max)
    print(f'Min and max array: {result}')
    return result

calculate_max_min([2,4,1,0,2,-1])
calculate_max_min([20,50,12,6,14,8])
calculate_max_min([100,-100])