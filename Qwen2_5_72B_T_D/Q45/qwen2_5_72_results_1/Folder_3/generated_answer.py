from collections import Counter

def palindromes_between_indices(s):
    substring = s[7:10].lower()
    letter_counts = Counter(substring)
    possible_palindromes = set()
    for first in letter_counts:
        for second in letter_counts:
            for third in letter_counts:
                if letter_counts[second] >= 2:
                    if first != second and first != third and (second == third):
                        possible_palindromes.add(first + second + third)
    return possible_palindromes