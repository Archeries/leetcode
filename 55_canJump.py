class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i, h in enumerate(nums, 0):
        	if i <= max_reach:
        		max_reach = max(max_reach, i + h)
        	else:
        		return False
        return True

if __name__ == '__main__':
	nums = [2, 2, 1, 0, 4]
	print(Solution().canJump(nums))