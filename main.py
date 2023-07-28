# Problem 1

# Given a list nums of n integers where nums[i] is in the range [1, list length], write a function that solves the following problem; return a list of all the integers in the range [1, list length] that do not appear in nums.
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1] Output: [5,6]
# Example 2:
# Input: nums = [1,1] Output: [2]

# Analysis: What we need is to have a list of integers from 1 to the len of our list, and then check if
# all that numbers are inside our list, if not add them to a new list and return that list,
# from this analysis, we can find some important points:

# 1. We don't care if the list is ordered or not, so let's not focus on that
# 2. We also don't care if there are five "3", or just one, this could help us in the future to improve our code


#  O(n)
def find_missing_nums(nums: list)->list:
   # Check if all elements in the list are numbers
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements in the input list must be integers.")

    # We need to be sure there are no duplicated values in the list
    # we can eliminate duplicates converting the list into a Python set
    # by doing this, we achieve to improve our function when we are looking if a number is in our list
    new_nums = set(nums)
    missing_numbers = [] 

    # This loop is what  defines our O(n) TC , a) because is the more complex operation and
    # b) because the execution of the function
    # will have a linear relationship with the size of the input on our list
    for i in range(1, len(nums) +1): # we are ussing range function to itererate over [1, list length] in Python, 
        # the second argument of the range function is not inclusive, so we need to add +1
        if i not in new_nums:  # check if the intenger i is inside our  set
            # if not, add it to the missing_numbers list
            missing_numbers.append(i)
    
    return missing_numbers # finally we return a list with all the missing integers



# Problem 2
# Given a list of integers nums and an integer target, write a function that solves the following problem; return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order. Example 1:
# Input: nums = [2,7,11,15], target = 9 Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6 Output: [0,1]


# Analysis: we are reciving two params, a list and an int, we will need to iterate over all the values in the list
# hold the first value, and iterate over all the list again and check if the sum of i + z match with our target value
# it will be important to check that we are not using the same index twice, altough this would give us the correct answer,
# the TC will be a quadratic one, and I think we can solve it using a different approach

#  O(n)
def find_matching_numbers(nums:list, target:int)->list:
    # Check if all elements in the list are numbers
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements in the input list must be integers.")
    # Check if the target is an int
    if not isinstance(target,int):
        raise ValueError("The target must be an int.")
    
    
    num_indices = {}  # Dictionary to store the index of each element

    # we iterate over the nums list using the enumerate function to get the value and index of each number
    # this is our most TC operation in the function, O(n), with a linear relationship between the nums list size
    # and the time
    for index, num_one in enumerate(nums):
        num_two = target - num_one # we reverse engenier our process, instead of looking the sum of two numbers, we will substrac our num_one
        # to the target number, so our new target becomes to find the num_two. We do this to avoid having a nested loop
        # first, we check if we have already the number that we are looking for in our dict
        # we need to check first if the number is already in our dict to avoid using the same element in our array
        if num_two in num_indices:
            # we return de value  of our key in the dict num_indices
            return [num_indices[num_two], index]
        # if we don't have a match, we will store the key:value pair in our dict. This way it will be available  for the next iteration with another number
        num_indices[num_one] = index

    return "No matches found"


if __name__ == "__main__":
    print("---------------Problem 1, Example 1---------------------")
    result_1_1 = find_missing_nums([4,3,2,7,8,2,3,1])
    print(f"The result of the problem 1, example 1 is: {result_1_1}")

    print("---------------Problem 1, Example 2---------------------")
    result_1_2 = find_missing_nums([1,1])
    print(f"The result of the problem 1, example 2 is: {result_1_2}")

    print("---------------Problem 2, Example 1---------------------")
    result_2_1 = find_matching_numbers([2,7,11,15], 9)
    print(f"The result of the problem 2, example 1 is: {result_2_1}")

    print("---------------Problem 2, Example 2---------------------")
    result_2_2 = find_matching_numbers([3,2,4], 6)
    print(f"The result of the problem 2, example 2 is: {result_2_2}")

    print("---------------Problem 2, Example 3---------------------")
    result_2_3 = find_matching_numbers([3,3], 6)
    print(f"The result of the problem 2, example 3 is: {result_2_3}")