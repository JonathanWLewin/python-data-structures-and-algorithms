from pyrefine.Classes import Example
from pyrefine.Classes.AlgorithmBaseObject import AlgorithmBaseObject
from pyrefine.Algorithms.TwoSum import TwoSum
import copy

class TwoSumImplementer(AlgorithmBaseObject):
    _title='Two Sum'
    _code_module = TwoSum
    _examples = [
        {
            "input": [2,7,11,15],
            "target": 9,
            "output": [0,1]
        },
        {
            "input": [3,2,4],
            "target": 6,
            "output": [1,2]
        },
        {
            "input": [3,3],
            "target": 6,
            "output": [0,1]
        }
    ]
    _methods = ["two_sum_brute_force", "two_sum_one_pass_hash_table", "two_sum_two_pass_hash_table"]
    _anchors = {
        "two_sum_brute_force": "anchor_1",
        "two_sum_one_pass_hash_table": "anchor_2",
        "two_sum_two_pass_hash_table": "anchor_3"
    }

    def __init__(self) -> None:
        super().__init__()

    def generate_steps(self, testNums, target, method=None):
        # Select generate steps based on the method passed in
        steps = []
        if method is None or method == "two_sum_brute_force":
            self.two_sum_brute_force_generate_steps(testNums, target, steps)
        if method == "two_sum_one_pass_hash_table":
            self.two_sum_one_pass_hash_table_generate_steps(testNums, target, steps)
        if method == "two_sum_two_pass_hash_table":
            self.two_sum_two_pass_hash_table_generate_steps(testNums, target, steps)
        return steps
    
    def generate_example(self, example_number=None, custom_example_input=None, method=None):
        # Generate examples based on the example index passed in, or use the custom input and target passed in
        if example_number is not None:
            example = self._examples[example_number]
        elif custom_example_input is not None:
            example = {
                "input": custom_example_input["input"],
                "target": custom_example_input["target"]
            }
        
        steps = self.generate_steps(example["input"], example["target"], method)
        example["steps"] = steps
        return example

    def two_sum_brute_force_generate_steps(self, nums, target, steps):
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
                steps.append({
                    "i": i,
                    "j": j,
                    "total": nums[i] + nums[j],
                    "answer_found": True if nums[i] + nums[j] == target else False
                })
                if nums[i] + nums[j] == target:
                    # If the sum is equal to the target, return the indices
                    return [i, j]
        return []
    
    def two_sum_one_pass_hash_table_generate_steps(self, nums, target, steps):
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
            steps.append({
                "i": i,
                "values_to_display": {
                    "Number Map":  copy.deepcopy(numberMap),
                    "Complement": complement
                },
                "answer_found": True if complement in numberMap and numberMap[complement] != i else False
            })
            if complement in numberMap and numberMap[complement] != i:
                # If the complement is in the hash table and the index of the complement is not the same as the current number, return the indices
                return [i, numberMap[complement]]
            # If the complement is not in the hash table, add the number and index to the hash table
            numberMap[nums[i]] = i
        return []
    
    def two_sum_two_pass_hash_table_generate_steps(self, nums, target, steps):
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
            steps.append({
                "i": i,
                "values_to_display": {
                    "Number Map":  copy.deepcopy(numberMap),
                    "Complement": target - nums[i]
                },
                "answer_found": True if target - nums[i] in numberMap and numberMap[target - nums[i]] != i else False
            })
            # Check if the complement of the number is in the hash table, and if the index of the complement is not the same as the current number
            complement = target - nums[i]
            if complement in numberMap and numberMap[complement] != i:
                # If the complement is in the hash table and the index of the complement is not the same as the current number, return the indices
                return [i, numberMap[complement]]

        return []