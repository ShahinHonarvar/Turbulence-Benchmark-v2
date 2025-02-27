from itertools import permutations

def palindromes_between_indices(s):
    letters = s[2:6].lower()
    unique_letters = set(letters)
    result = set()
    for length in range(4, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            pal = ''.join(perm) + ''.join(perm[::-1])
            result.add(pal)
    return result