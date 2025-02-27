from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[4:6]
    unique_letters = set(sub_string.lower())
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not any((c.isalpha() for c in sub_string)):
        return set()
    palindromes = set()
    for i in range(3, len(unique_letters) + 1):
        if i in range(3, len(unique_letters) + 1):
            for perm in permutations(unique_letters, i):
                cand = ''.join(perm)
                cand_mid = cand[len(cand) // 2] if len(cand) % 2 == 1 else None
                mirrored_cand = cand + cand[::-1][len(cand) % 2:]
                if mirrored_cand[0] == cand_mid:
                    palindromes.add(mirrored_cand)
    return palindromes