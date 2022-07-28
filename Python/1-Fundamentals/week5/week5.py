# Excercise: Linear Search
'''def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x]==target: 
            print("Found at index", x)
            return x
    print("Target is not in the list")
    return -1

my_list=[5,3,5,2,6,9]
linear_search(my_list,3)'''

# Excercise: Binary Serch
def binary_search(the_list, target):
    lower_bound=0
    higher_bound=len(the_list)-1

    while lower_bound<=higher_bound:
        pivot = (higher_bound+lower_bound)//2

        if the_list[pivot] == target:
            return pivot
        if the_list[pivot]>target:
            higher_bound=pivot-1
        else:
            lower_bound=pivot+1
    return -1

my_list=[1,2,3,4,10,12]
print(binary_search(my_list,10))