class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0;
        right = n-1
        while left < right:
            while left < right and not (s[left].isdigit() or s[left].isalpha()):
                left += 1
            while right > left and not (s[right].isdigit() or s[right].isalpha()):
                right -= 1
            if not s[left].isalpha():
                if s[left] != s[right]:
                    return False
            else:
                if s[left].lower() != s[right].lower():
                    return False
            left += 1
            right -= 1
        return True