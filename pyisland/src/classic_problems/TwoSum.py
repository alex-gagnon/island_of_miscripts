from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for index, num in enumerate(nums):
            pair = target - num
            if pair in index_map:
                return [index_map[pair], index]
            index_map[num] = index
        return None


if __name__ == '__main__':
    a = Solution()
    arr = [4, 8, 1, 15]
    x = 9
    test1 = a.twoSum(nums=arr, target=x)
    print(test1)