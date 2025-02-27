from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindrome_set = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set