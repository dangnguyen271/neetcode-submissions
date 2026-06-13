class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-zA-Z0-9]+', '', s)
        s = s.lower()

        for i in range(len(s)):
            j = len(s) - i - 1
            print(s[i], s[j])
            if s[i] != s[j]:
                return False

        return True