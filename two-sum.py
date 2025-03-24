"""
Solving Steps
* Problem breakdown
    * Input: 
        * A list of integers `nums` and an integer `target`.
    * Understanding (observations):
        * 1) We need to find two numbers in the list such that their sum equals the target.
        * 2) Return the indices of the two numbers.
        * 3) The problem can be solved efficiently using a hash map for constant-time lookups.
    * Goal: 
        * Find and return the indices of two numbers whose sum equals the target.
    * Output: 
        * A list of two integers representing the indices of the two numbers.

* Constraints
    * Min, max length:
        * Min: 2 (as at least two numbers are needed)
    * Kinds of data:
        * List of integers.
    * Sorted/unsorted:
        * Unsorted.
    * Unique/duplicates:
        * The list can have duplicate values.

* Examples:
    * Simple case 1: Input: nums = [2, 7, 11, 15], target = 9, Output: [0, 1]
    * Simple case 2: Input: nums = [3, 2, 4], target = 6, Output: [1, 2]
    * Simple case 3: Input: nums = [3, 3], target = 6, Output: [0, 1]
    * Edge case 1: Input: nums = [1, 1], target = 2, Output: [0, 1] (smallest case)
    * Edge case 2: Input: nums = [5, -1, -4], target = -5, Output: [1, 2]

* Approach
    * Brute force approach:
        * Visualize:
            * Use nested loops to check the sum of all possible pairs of numbers.
        * Steps:
            * For each pair of indices (i, j), check if nums[i] + nums[j] == target.
        * Complexity analysis:
            * Time complexity: O(n^2)
            * Space complexity: O(1)
        * Pros/cons (scalability):
            * Pros: Simple to understand and implement.
            * Cons: Inefficient for large inputs.

    * Optimized approach (hash map):
        * Visualize:
            * Use a hash map to store indices of numbers as we iterate through the list.
            * For each number, calculate the required complement (`target - nums[i]`) and check if it exists in the hash map.
        * Steps:
            * Initialize an empty hash map.
            * Traverse the list:
                * Calculate the complement of the current number.
                * If the complement exists in the hash map, return the indices.
                * Otherwise, add the current number and its index to the hash map.
        * Complexity:
            * Time complexity: O(n) (single pass with constant-time lookups).
            * Space complexity: O(n) (for the hash map).
        * Pros/cons (scalability):
            * Pros: Efficient and scalable for large inputs.
            * Cons: Slightly more complex to implement.

    * Approach to implement:
        * Approach: Optimized approach using a hash map.
        * Reason for selecting this approach:
            * It is efficient and meets the problem constraints.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in hashmap:
                return [i, hashmap[remaining]]
            hashmap[num] = i
            print(hashmap)
