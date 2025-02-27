from itertools import permutations

def palindromes_between_indices(s):
    filtered_chars = [char.lower() for char in s[2:9] if char.isalpha()]
    unique_chars = set(filtered_chars)
    four_letter_combinations = set(permutations(unique_chars, 4))
    palindromes = set()
    for combo in four_letter_combinations:
        candidate = ''.join(combo)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes