from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[1:8].lower()
    palindromes = set()
    for i in range(3, len(sub_str) + 1):
        perms = set(permutations(sub_str, i))
        for perm in perms:
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes