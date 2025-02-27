from collections import defaultdict

def palindrome_of_length_n(s):
    s = s.lower()
    l = len(s)
    if l < 77:
        return set()
    palindromes = set()
    for i in range(l - 76):
        substring = s[i:i + 77]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes