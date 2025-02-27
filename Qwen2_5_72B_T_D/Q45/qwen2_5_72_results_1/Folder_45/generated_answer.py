from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letter_counts = Counter(substring)
    palindromes = set()
    for length in range(4, 11, 2):
        for candidate in generate_palindromes(letter_counts, length):
            palindromes.add(candidate)
    return palindromes

def generate_palindromes(letter_counts, length):
    half_length = length // 2
    letters = ''.join([letter * (count // 2) for letter, count in letter_counts.items()])
    for half in set(permutations(letters, half_length)):
        half_str = ''.join(half)
        palindrome = half_str + half_str[::-1]
        yield palindrome