from itertools import permutations

def palindromes_between_indices(text):
    ignored_chars = set(text[7:])
    filtered_chars = ''.join(filter(lambda char: char in ignored_chars, text[:7].lower()))
    palindromes = set()
    for length in range(3, len(filtered_chars) + 1):
        for perm in permutations(filtered_chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes