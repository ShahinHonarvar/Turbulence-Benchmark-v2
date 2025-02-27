from collections import Counter
        from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:7].lower()
    char_count = Counter(substring)
    possible_chars = char_count.elements()

    def generate_palindromes(length, possible_chars):
        unique_combos = set([''.join(p) for p in permutations(possible_chars, length // 2)])
        return {''.join([combo, combo[::-1]]) for combo in unique_combos}
    possible_palindromes = set()
    for length in range(4, 5):
        possible_palindromes.update(generate_palindromes(length, possible_chars))
    return possible_palindromes