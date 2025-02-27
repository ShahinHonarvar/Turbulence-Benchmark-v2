import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    start_index = 5
    end_index = 9
    letters = text[start_index:end_index + 1].lower()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        permutations = itertools.permutations(letters, length)
        for permutation in permutations:
            candidate = ''.join(permutation)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes