from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for center in range(len(s)):
        for left in range(max(0, center - 34), center):
            right = left + 34
            if right >= len(s):
                break
            if s[left:right + 1] == s[left:right + 1][::-1]:
                palindromes.add(s[left:right + 1].upper())
    return palindromes