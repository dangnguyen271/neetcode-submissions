class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-zA-Z]+', '', s)
        s = s.lower()

        if len(s) == 2:
            if s[0] != s[1]:
                return False

        for i in range(len(s)):
            j = len(s) - i - 1
            print(s[i], s[j])
            if s[i] != s[j]:
                return False

        return True