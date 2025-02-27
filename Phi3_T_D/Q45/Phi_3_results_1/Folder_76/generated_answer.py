from itertools import permutations

def palindromes_between_indices(s):
    start, end = (1, 4)
    lower_s = s[start - 1:end].lower()
    unique_letters = sorted(set(lower_s))
    palindrome_set = set()
    for size in range(4, len(unique_letters) + 1):
        for perm in permutations(unique_letters, size):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set