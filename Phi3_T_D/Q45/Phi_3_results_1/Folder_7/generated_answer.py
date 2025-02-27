from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(s):
    chars_subset = s[1:10].lower()
    unique_chars = ''.join(sorted(set(chars_subset)))
    palindromes = set()
    for length in range(7, len(unique_chars) + 1):
        for perm in set(permutations(unique_chars, length)):
            potential_palindrome = ''.join(perm)
            if is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome)
    return palindromes