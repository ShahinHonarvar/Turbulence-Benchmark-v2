from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[2:7]
    letters = ''.join(filter(str.isalpha, sub_str)).lower()
    unique_letters = set(letters)
    if len(letters) < 5:
        return set()
    combinations = set((''.join(p) for p in permutations(unique_letters, len(unique_letters))))
    palindromes = set()
    for combo in combinations:
        for c in unique_letters:
            palindromes.add(c + combo + c)
    return {p for p in palindromes if len(p) >= 4}