from itertools import permutations

def palindromes_between_indices(s):
    lower_index = 1
    upper_index = 7
    substr = s[lower_index:upper_index].lower()
    letters = ''.join(sorted(set(substr), key=substr.index))
    palindromes = set()
    for perm_len in range(3, min(len(letters) + 1, upper_index - lower_index + 1)):
        for perm in permutations(letters, perm_len):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes