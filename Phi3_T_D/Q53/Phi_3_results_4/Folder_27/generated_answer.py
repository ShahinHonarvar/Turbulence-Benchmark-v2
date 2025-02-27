from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    n = len(s)
    all_palindromes = set()

    def extend_palindrome(left, right, length):
        while left >= 0 and right < n and (s[left].lower() == s[right].lower()):
            if length >= 100:
                all_palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(n):
        extend_palindrome(i, i, 0)
        extend_palindrome(i, i + 1, 0)
    return all_palindromes