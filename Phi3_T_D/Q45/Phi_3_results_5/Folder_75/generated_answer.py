from itertools import permutations

def palindromes_between_indices(s):
    extracted = s[2:5].lower()
    palindrome_set = set()
    for i in range(3, len(extracted) + 1):
        for p in set(permutations(extracted, i)):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set