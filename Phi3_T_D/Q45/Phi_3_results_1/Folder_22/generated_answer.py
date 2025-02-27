from itertools import permutations

def palindromes_between_indices(s):
    index_range = s[5:7]
    palindromes = set()
    for length in range(3, len(index_range) + 1):
        for perm in permutations(index_range, length):
            candidate = ''.join(perm)
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes