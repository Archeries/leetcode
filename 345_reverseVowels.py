class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWEL = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        vowels = list(filter(lambda x : x in VOWEL, s_list))
        vowels.reverse()
        idxs = list(filter(lambda x : s_list[x] in VOWEL, range(len(s_list))))
        for i in range(len(vowels)):
            s_list.pop(idxs[i])
            s_list.insert(idxs[i], vowels[i])
        return "".join(s_list)

if __name__ == '__main__':
    s = "leetcode"
    print(Solution().reverseVowels(s))