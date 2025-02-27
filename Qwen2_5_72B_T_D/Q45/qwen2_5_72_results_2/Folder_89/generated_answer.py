from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letter_counts = Counter(substring)
    possible_palindromes = set()
    for length in range(6, 11):
        for candidate in generate_palindromes(letter_counts, length):
            possible_palindromes.add(candidate)
    return possible_palindromes

def generate_palindromes(letter_counts, length):
    half_length = length // 2
    available_letters = ''.join([letter * (count // 2) for letter, count in letter_counts.items()])
    palindromes = set()
    for perm in set(permutations(available_letters, half_length)):
        half = ''.join(perm)
        full = half + (half[::-1] if length % 2 == 0 else half[:-1][::-1])
        palindromes.add(full)
    return palindromes