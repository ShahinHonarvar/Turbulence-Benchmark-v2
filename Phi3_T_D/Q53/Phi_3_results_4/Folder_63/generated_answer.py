from collections import defaultdict

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        yield (left, right)
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for left in range(len(s)):
        for right in range(left, len(s)):
            palindromes.update({s[i] for i in range(left, right + 1) if len(s[left:right + 1]) >= 37})
            for center in expand_around_center(s, left, right):
                palindrome_length = center[1] - center[0]
                if palindrome_length >= 37:
                    palindromes.add(s[center[0]:center[1] + 1])
    return palindromes