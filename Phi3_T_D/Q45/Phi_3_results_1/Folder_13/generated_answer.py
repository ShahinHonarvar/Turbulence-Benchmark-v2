from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[2:10]
    letters = ''.join((c.lower() for c in sub_str if c.isalpha()))
    unique_letters = set(letters)
    result_set = set()
    for length in range(5, len(unique_letters) + 1):
        perms = set((''.join(p) for p in permutations(unique_letters, length)))
        for perm in perms:
            if perm == perm[::-1]:
                result_set.add(perm)
    return result_set