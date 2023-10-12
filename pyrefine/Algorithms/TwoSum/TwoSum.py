'''
    Problem: Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
'''

'anchor_1'
def two_sum_brute_force(nums, target):
    '''
        O(n^2)
        Minimal memory required, however the runtime is the longest
    '''
    # Get length for use in for loops
    length = len(nums)
    # Iterate through the list of numbers
    for i in range(length - 1):
        # For each number, iterate through the rest of the list, and check if the sum is equal to the target
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                # If the sum is equal to the target, return the indices
                return [i, j]
    return []

'anchor_2'
def two_sum_one_pass_hash_table(nums, target):
    '''
        O(n)
        Smallest runtime, but requires larger memory
    '''
    # Create a hash table with the number as the key and the index as the value
    numberMap = {}
    length = len(nums)

    for i in range(length):
        # Check if the complement of the number is in the hash table, and if the index of the complement is not the same as the current number
        complement = target - nums[i]
        if complement in numberMap and numberMap[complement] != i:
            # If the complement is in the hash table and the index of the complement is not the same as the current number, return the indices
            return [i, numberMap[complement]]
        # If the complement is not in the hash table, add the number and index to the hash table
        numberMap[nums[i]] = i
    return []

'anchor_3'
def two_sum_two_pass_hash_table(nums, target):
    '''
        O(n)
        Smallest runtime, but requires larger memory
    '''
    numberMap = {}
    length = len(nums)

    # Create a hash table with the number as the key and the index as the value
    for i in range(length):
        numberMap[nums[i]] = i
    
    # Iterate through the list of numbers
    for i in range(length):
        # Check if the complement of the number is in the hash table, and if the index of the complement is not the same as the current number
        complement = target - nums[i]
        if complement in numberMap and numberMap[complement] != i:
            # If the complement is in the hash table and the index of the complement is not the same as the current number, return the indices
            return [i, numberMap[complement]]

    return []