from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:7]
    letters = set(substring.lower())
    palindromes = set()
    for length in range(4, min(len(substring) + 1, len(letters) + 1)):
        for perm in permutations(letters, length):
            candidate = ''.join(perm) + ''.join(reversed(perm))
            half_length = length // 2
            for i in range(half_length):
                if candidate[i] != candidate[-(i + 1)]:
                    break
            else:
                palindromes.add(candidate)
    return palindromes