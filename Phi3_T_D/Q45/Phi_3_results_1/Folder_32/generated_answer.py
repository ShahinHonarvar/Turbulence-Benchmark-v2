from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(candidate):
        return candidate == candidate[::-1]
    index_range = s[1:8]
    letters = ''.join(filter(str.isalpha, index_range)).lower()
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for perm in permutations(letters, i):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes