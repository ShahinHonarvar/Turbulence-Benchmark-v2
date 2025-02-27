from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:7]
    letters_set = set(sub_str.lower())
    unique_letters = ''.join(letters_set)
    palindromes = set()
    for length in range(3, len(unique_letters) + 1):
        perms = set(permutations(unique_letters, length))
        for perm in perms:
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes