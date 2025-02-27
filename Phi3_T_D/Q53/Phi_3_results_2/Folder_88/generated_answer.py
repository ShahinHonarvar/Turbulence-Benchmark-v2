def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        yield s[left:right + 1]
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for center in range(len(s)):
        for p in expand_around_center(s, center, center):
            if len(p) >= 27 and p.isalpha():
                palindromes.add(p.lower())
        for p in expand_around_center(s, center, center + 1):
            if len(p) >= 27 and p.isalpha():
                palindromes.add(p.lower())
    return palindromes