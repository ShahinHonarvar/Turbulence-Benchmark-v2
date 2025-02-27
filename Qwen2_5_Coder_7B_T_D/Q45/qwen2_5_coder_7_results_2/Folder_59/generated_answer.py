def palindromes_between_indices(s):
    range_slice = s[8:10]
    letters = ''.join(filter(str.isalpha, range_slice)).lower()
    unique_letters = ''.join(sorted(set(letters)))
    result = set()
    for length in range(3, len(unique_letters) + 1):
        for perm in itertools.permutations(unique_letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result