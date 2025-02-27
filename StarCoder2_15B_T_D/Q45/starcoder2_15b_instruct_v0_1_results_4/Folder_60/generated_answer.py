import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    letter_indices = [i for i, c in enumerate(string) if c.isalpha()]
    palindromes = set()
    for i, letter in enumerate(letters):
        if 3 <= letter_indices[i] <= 6:
            for permutation in itertools.permutations(letters[i + 1:]):
                palindrome = letter + ''.join(permutation)
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes