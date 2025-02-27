from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(s):
    substring = s[5:7]
    chars = set(substring.lower())
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(sorted(chars), length):
            if len(perm) == len(chars):
                pal_str = ''.join(perm)
                if is_palindrome(pal_str):
                    palindromes.add(pal_str)
    return palindromes