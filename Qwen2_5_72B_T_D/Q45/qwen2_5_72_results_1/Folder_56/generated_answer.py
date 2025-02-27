from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letter_counts = Counter(substring)
    potential_palindromes = set()
    for letter, count in letter_counts.items():
        if count >= 5:
            palindrome = letter * 5
            potential_palindromes.add(palindrome)
        if count >= 4 and len(potential_palindromes) == 0:
            for other_letter in letter_counts:
                if other_letter != letter:
                    palindrome = letter * 2 + other_letter + letter * 2
                    potential_palindromes.add(palindrome)
        if count >= 3 and len(potential_palindromes) == 0:
            for other_letter, other_count in letter_counts.items():
                if other_letter != letter and other_count >= 1:
                    palindrome = letter * 2 + other_letter + letter * 1
                    potential_palindromes.add(palindrome)
        if count >= 2 and len(potential_palindromes) == 0:
            for other_letter, other_count in letter_counts.items():
                if other_letter != letter and other_count >= 2:
                    palindrome = letter * 1 + other_letter * 1 + letter * 1
                    potential_palindromes.add(palindrome)
    return potential_palindromes