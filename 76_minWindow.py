# ref: https://discuss.leetcode.com/topic/20692/12-lines-python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        need, missing = collections.Counter(t), len(t)
        res_i = res_j = i = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not res_j or res_j - res_i > j - i:
                    res_i, res_j = i, j
        return s[res_i: res_j]

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))