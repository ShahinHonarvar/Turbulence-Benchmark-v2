import itertools

def palindromes_between_indices(s):
    filtered_chars = {ch.lower() for ch in s[3:6]}
    palindromes = set()
    for length in range(4, min(len(filtered_chars) + 1, 6) + 1):
        for subset in itertools.combinations(filtered_chars, length):
            subset_str = ''.join(subset)
            if subset_str == subset_str[::-1]:
                palindromes.add(subset_str)
    return palindromes