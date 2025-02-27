import itertools

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = set(s)
    result = set()
    for length in range(5, len(s) + 1):
        for combination in itertools.permutations(letters, length):
            candidate = ''.join(combination)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result