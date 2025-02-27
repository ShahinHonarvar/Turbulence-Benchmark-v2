from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:7].lower()
    letter_counts = Counter(substring)
    possible_palindromes = set()
    for letter, count in letter_counts.items():
        if count >= 2:
            possible_palindromes.add(letter * 3)
        for other_letter, other_count in letter_counts.items():
            if other_letter != letter and other_count > 0:
                if count >= 1:
                    possible_palindromes.add(letter + other_letter + letter)
    return possible_palindromes