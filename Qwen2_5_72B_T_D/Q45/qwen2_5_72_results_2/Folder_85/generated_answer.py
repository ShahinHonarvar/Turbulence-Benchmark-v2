from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    letter_set = set(substring)
    palindromes = set()
    for perm in permutations(letter_set, len(letter_set)):
        perm_str = ''.join(perm)
        for length in range(7, len(perm_str) + 1):
            for i in range(len(perm_str) - length + 1):
                candidate = perm_str[i:i + length]
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes