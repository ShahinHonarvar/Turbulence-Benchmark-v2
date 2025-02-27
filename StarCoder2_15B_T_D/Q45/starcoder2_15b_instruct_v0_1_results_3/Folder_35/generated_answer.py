import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string if ch.isalpha()]
    palindromes = set()
    for combination in itertools.combinations(letters, 4):
        for permutation in itertools.permutations(combination):
            palindrome = ''.join(permutation)
            if palindrome.lower() == palindrome.lower()[::-1]:
                palindromes.add(palindrome)
    return palindromes