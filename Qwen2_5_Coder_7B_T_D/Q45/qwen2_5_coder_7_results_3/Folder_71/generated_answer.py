import itertools

def palindromes_between_indices(s):
    result = set()
    letters = s[1:4]
    for length in range(4, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            candidate = ''.join(combination)
            if candidate.lower() == candidate[::-1].lower():
                result.add(candidate)
    return result