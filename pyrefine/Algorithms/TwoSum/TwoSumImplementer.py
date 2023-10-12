from pyrefine.Classes import Example
from pyrefine.Classes.AlgorithmBaseObject import AlgorithmBaseObject
from pyrefine.Algorithms.TwoSum import TwoSum

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
        }
    ]

    def __init__(self) -> None:
        super().__init__()

    def generate_steps(self, testNums, target):
        steps = []
        self.two_sum_brute_force_generate_steps(testNums, target, steps)
        return steps
    
    def generate_example(self, example_number=None, inputted_example=None):
        if example_number is not None:
            example = self._examples[example_number]
            steps = self.generate_steps(example["input"], example["target"])
            example["steps"] = steps
            return example
        elif inputted_example is not None:
            example = inputted_example
            steps = self.generate_steps(example["input"], example["target"])
            example["steps"] = steps
            return example
    
    def generate_step(self, i, j, i_plus_j_val, steps):
        steps.append({
            "special_content": {
                "i": i,
                "j": j
            },
            "Total": i_plus_j_val
        })


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
                self.generate_step(i, j, nums[i] + nums[j], steps)
                if nums[i] + nums[j] == target:
                    # If the sum is equal to the target, return the indices
                    return [i, j]
        return []