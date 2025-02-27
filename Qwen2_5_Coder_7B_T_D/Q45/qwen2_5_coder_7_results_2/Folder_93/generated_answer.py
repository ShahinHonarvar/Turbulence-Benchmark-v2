from itertools import permutations

def palindromes_between_indices(s):
    filtered_chars = [char for char in s[2:8] if char.isalpha()]
    unique_chars = sorted(set(filtered_chars), key=str.lower)
    palindromes = set()
    for r in range(3, 9):
        for perm in permutations(unique_chars, r):
            perm_str = ''.join(perm)
            if perm_str.lower() == perm_str.lower()[::-1] and len(perm_str) >= 6:
                palindromes.add(perm_str.lower())
    return palindromes