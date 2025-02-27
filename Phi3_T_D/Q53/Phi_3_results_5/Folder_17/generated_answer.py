from collections import deque

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        if right - left + 1 >= 36:
            yield s[left:right + 1]
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for palindrome in list(expand_around_center(s, i, i)):
            palindromes.add(palindrome)
        for palindrome in list(expand_around_center(s, i, i + 1)):
            palindromes.add(palindrome)
    return palindromes