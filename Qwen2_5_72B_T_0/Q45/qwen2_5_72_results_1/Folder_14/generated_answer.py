from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:6].lower()
    letter_counts = Counter(substring)
    possible_palindromes = set()
    for letter, count in letter_counts.items():
        if count >= 2:
            for _ in range(count // 2):
                possible_palindromes.add(letter * 3)
                possible_palindromes.add(letter * 2 + letter)
    return possible_palindromes