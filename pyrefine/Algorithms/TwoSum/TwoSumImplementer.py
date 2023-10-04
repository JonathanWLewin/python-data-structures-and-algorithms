from pyrefine.Classes import Example
from pyrefine.Classes.AlgorithmBaseObject import AlgorithmBaseObject
from pyrefine.Algorithms.TwoSum import TwoSum

class TwoSumImplementer(AlgorithmBaseObject):
    _title='Two Sum'
    _code_module = TwoSum

    def __init__(self) -> None:
        super().__init__()

    def generate_steps(self):
        testNums = []
        target = 0
        self.two_sum_brute_force_generate_steps(testNums, target)

    def two_sum_brute_force_generate_steps(nums, target):
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