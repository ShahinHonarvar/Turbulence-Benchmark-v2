from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[5:8].lower()
    unique_chars = set(sub_str)
    palindromes = set()
    for perm in permutations(unique_chars, len(unique_chars)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes