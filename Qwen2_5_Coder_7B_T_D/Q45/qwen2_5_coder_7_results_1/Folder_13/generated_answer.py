import itertools

def palindromes_between_indices(s):
    sub_string = s[3:10].lower()
    letters = set(sub_string)
    result = set()
    for length in range(5, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            for permutation in itertools.permutations(combination):
                candidate = ''.join(permutation)
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result