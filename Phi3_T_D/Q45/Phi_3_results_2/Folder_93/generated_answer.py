from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[2:8].lower()
    unique_chars = ''.join(sorted(set(s)))
    result_set = set()
    for length in range(6, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            if is_palindrome(''.join(perm)):
                result_set.add(''.join(perm))
    return result_set