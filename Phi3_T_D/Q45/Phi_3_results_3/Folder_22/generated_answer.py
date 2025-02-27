from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(string):
    try:
        substring = string[5:7]
        substring = substring.lower()
        letters = set(substring)
        palindromes = set()
        for length in range(3, len(substring) + 1):
            for perm in permutations(letters, length):
                if is_palindrome(''.join(perm)):
                    palindromes.add(''.join(perm))
        return palindromes
    except IndexError:
        return set()