import itertools
from collections import Counter

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(string):
    substring = string[4:8].lower()
    letters = ''.join(filter(str.isalpha, substring))
    counter = Counter(letters)
    unique_letters = ''.join([letter for letter in counter if counter[letter] >= 2])
    if len(unique_letters) < 5:
        return set()
    palindromes = set()
    for length in range(5, len(unique_letters) + 1):
        for combo in itertools.combinations_with_replacement(unique_letters, length):
            count_combo = Counter(combo)
            if all((count_combo[char] >= counter[char] for char in counter)):
                for perm in itertools.permutations(combo):
                    palindromes.add(''.join(perm))
    return palindromes