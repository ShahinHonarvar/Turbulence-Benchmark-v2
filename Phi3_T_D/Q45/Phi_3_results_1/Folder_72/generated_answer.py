def palindromes_between_indices(s):
    extracted_string = s[1:8]
    letter_counts = {}
    for letter in extracted_string:
        letter_counts[letter.lower()] = letter_counts.get(letter.lower(), 0) + 1
    palindromes_set = set()
    for length in range(6, sum(letter_counts.values()) + 1):
        combos = _find_palindromes(letter_counts, [], length // 2)
        palindromes_set.update([combo + combo[::-1] for combo in combos if combo])
    return palindromes_set

def _find_palindromes(letter_counts, partial_combo, length_needed):
    if length_needed == 0:
        return [partial_combo]
    letter = next((k for k, v in letter_counts.items() if v), None)
    if letter is None:
        return []
    new_partial_combo = partial_combo + letter.lower()
    new_letter_counts = letter_counts.copy()
    new_letter_counts[letter.lower()] -= 1
    if new_letter_counts[letter.lower()] == 0:
        del new_letter_counts[letter.lower()]
    combos = []
    for combo in _find_palindromes(new_letter_counts, new_partial_combo, length_needed - 1):
        combos.append(combo)
    return combos