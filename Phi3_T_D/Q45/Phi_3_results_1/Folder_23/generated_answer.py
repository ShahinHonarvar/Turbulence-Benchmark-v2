from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[:7].lower()
    letters = ''.join(sorted(set(sub_str)))
    palindromes = set()
    for length in range(4, len(sub_str) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes