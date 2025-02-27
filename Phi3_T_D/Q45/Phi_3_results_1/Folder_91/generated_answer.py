from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7]
    chars = [char.lower() for char in substring if char.isalpha()]
    unique_chars = set(chars)
    length = len(unique_chars)
    if length < 3:
        return set()
    palindromes = set()
    for i in range(length, 0, -1):
        for subset in permutations(unique_chars, i):
            if any((c.isupper() for c in substring)):
                palindrome_mul = [c.upper() if subset.count(c.lower()) > chars.count(c) else c for c in subset]
            else:
                palindrome_mul = subset
            palindrome = ''.join(palindrome_mul)
            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes