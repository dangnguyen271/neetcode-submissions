class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        cur_substring = []
        left = 0
        right = 1
        cur_substring.append(s[left])
        longest = 1
        i = 0
        print(cur_substring)
        while right < len(s):
            if s[right] not in cur_substring:
                cur_substring.append(s[right])
                right += 1
                print(cur_substring)
            else:
                cutoff = cur_substring.index(s[right])
                left += cutoff + 1
                del cur_substring[:cutoff+1]
                print(cur_substring)

            if len(cur_substring) > longest:
                longest = len(cur_substring)

        return longest
