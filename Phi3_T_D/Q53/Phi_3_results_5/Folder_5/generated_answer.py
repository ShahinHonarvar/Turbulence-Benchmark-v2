from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    length = 46
    d = defaultdict(set)
    for i in range(len(s)):
        for j in range(i + length, len(s)):
            substr = s[i:j + 1].lower()
            if substr == substr[::-1] and all((c.isalpha() for c in substr)):
                d[length].add(substr)
    valid_palindromes = set()
    for k in sorted(d.keys()):
        if k >= 46:
            valid_palindromes.update(d[k])
    return valid_palindromes