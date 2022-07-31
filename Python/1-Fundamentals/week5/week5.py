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
'''def binary_search(the_list, target):
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
print(binary_search(my_list,10))'''

# CC:Linear Search Dictionary
'''def linear_search_dictionary(dict,target):
    for key,value in dict.items():
        if value==target:
            print(f"Target found at key {key}")
            return key
    print("Target is not in the dictionary")
    return None

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)'''

# Excercise: Bubble Sort =======
'''unsorted_list = [101,49,3,12,56]

def bubblesort(the_list):
    high_idx=len(the_list)-1
    
    for i in range(high_idx):
        list_changed=False
        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]
            if item>next:
                the_list[j]=next
                the_list[j+1]=item
                list_changed=True
        # If there was no swapping in a pass-thru then it's sorted, so break
        if list_changed:break

bubblesort(unsorted_list)
print(unsorted_list)'''


# Excercise: Quicksort
# Divide and Conquer. A pivot is chosen first

'''unsorted_list = [101,49,3,12,56]

def sort_part(the_list,low_idx,high_idx):
    pivot_idx=high_idx

    while low_idx!=pivot_idx:
        low_val=the_list[low_idx]
        if low_val>the_list[pivot_idx]:
            the_list[low_idx]=the_list[pivot_idx-1]
            the_list[pivot_idx-1]=the_list[pivot_idx]
            the_list[pivot_idx]=low_val
            pivot_idx-=1
        else:
            low_idx+=1
    return pivot_idx

def quicksort(the_list,low_idx,high_idx):
    if low_idx>high_idx: return
    pivot_idx=sort_part(the_list,low_idx,high_idx)
    quicksort(the_list,low_idx,pivot_idx-1)
    quicksort(the_list,pivot_idx+1,high_idx)

quicksort(unsorted_list,0,len(unsorted_list)-1)
print(unsorted_list)'''

# Code Challenge: FizzBuzz
def fizzbuzz(num):
    for i in range(1,num+1):
        if i%3 == 0 and i%5==0: print("FizzBuzz")
        elif i%3 == 0: print("Fizz")
        elif i%5 == 0: print("Buzz")
        else:print(i)

fizzbuzz(50)