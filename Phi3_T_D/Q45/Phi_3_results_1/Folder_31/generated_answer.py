from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    relevant_chars = set(s)
    palindromes = set()
    for length in range(6, len(relevant_chars) + 1):
        for perm in permutations(relevant_chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes