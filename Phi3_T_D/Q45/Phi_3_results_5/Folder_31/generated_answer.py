from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[0:8].lower()
    letters_set = set(sub_string)
    palindromes = set()
    for i in range(5, 9):
        for perm in permutations(letters_set, i):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes