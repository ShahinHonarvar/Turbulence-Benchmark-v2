from itertools import permutations

def palindromes_between_indices(s):
    letters = s[4:8].lower()
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for perm in permutations(letters, i):
            str_perm = ''.join(perm)
            if str_perm == str_perm[::-1]:
                palindromes.add(str_perm)
    return palindromes