from itertools import permutations

def palindromes_between_indices(s):
    indices = list(range(3, 9))
    substring = ''.join(sorted((s[i] for i in indices))).lower()
    unique_letters = ''.join((char for char in substring if substring.count(char) == 1 or char == ' '))
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for perm in permutations(unique_letters, length):
            palindrome = ''.join(perm) + ''.join(perm[::-1])
            if palindrome != '':
                palindromes.add(palindrome)
    return palindromes