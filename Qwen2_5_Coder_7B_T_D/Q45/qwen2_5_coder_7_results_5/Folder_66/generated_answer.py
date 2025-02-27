import itertools

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = set(s)
    palindromes = set()
    for length in range(5, len(s) + 1):
        for sequence in itertools.permutations(letters, length):
            if sequence == sequence[::-1]:
                palindromes.add(''.join(sequence))
    return palindromes