from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:9].lower()
    letter_set = set(substring)
    palindromes = set()
    for perm in permutations(letter_set, len(letter_set)):
        for i in range(2, len(substring) + 1, 2):
            candidate = perm[:i // 2] + perm[:i // 2][::-1]
            if len(candidate) >= 4 and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes