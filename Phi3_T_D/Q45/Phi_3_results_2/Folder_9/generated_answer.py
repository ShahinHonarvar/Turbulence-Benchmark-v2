from itertools import permutations

def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    first_six = s[:6]
    palindromes = set()
    for char in english_letters:
        shorter_first_six = ''.join(filter(lambda c: c in english_letters, first_six.replace(char, '', 1)))
        if len(shorter_first_six) < 6:
            continue
        for length in range(7, 13):
            for perm in permutations(shorter_first_six, length):
                candidate = ''.join(perm)
                if candidate.lower() == candidate.lower()[::-1]:
                    palindromes.add(candidate)
    return palindromes