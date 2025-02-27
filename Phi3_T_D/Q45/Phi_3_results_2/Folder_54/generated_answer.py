import itertools

def palindromes_between_indices(s):
    indices_range = s[3:10]
    letters = ''.join(filter(str.isalpha, indices_range)).lower()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for subset in itertools.permutations(letters, length):
            candidate = ''
            mid = length // 2
            candidate = ''.join(subset[:mid])
            if length % 2 == 0:
                candidate += candidate[::-1]
            else:
                candidate += subset[mid] + candidate[::-1]
            palindromes.add(candidate)
    return palindromes