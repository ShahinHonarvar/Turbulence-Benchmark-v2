from itertools import permutations

def palindromes_between_indices(s):
    letters = [char for char in s[3:10] if char.isalpha()]
    unique_letters = set(letters)
    result = set()
    for r in range(5, len(letters) + 1):
        for perm in permutations(unique_letters, r):
            perm_str = ''.join(perm)
            if perm_str.lower() == perm_str[::-1].lower():
                result.add(perm_str)
    return result