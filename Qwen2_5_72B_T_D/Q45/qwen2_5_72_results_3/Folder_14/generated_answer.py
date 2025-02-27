from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:6].lower()
    letter_counts = Counter(substring)
    possible_palindromes = set()
    for letter, count in letter_counts.items():
        if count >= 2:
            for middle in letter_counts.keys():
                possible_palindrome = letter + middle + letter
                possible_palindromes.add(possible_palindrome)
    return possible_palindromes