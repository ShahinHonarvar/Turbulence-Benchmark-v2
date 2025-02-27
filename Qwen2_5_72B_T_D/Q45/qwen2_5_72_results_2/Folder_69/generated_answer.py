from collections import Counter

def palindromes_between_indices(s):
    substring = s[:4]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    possible_palindromes = set()
    for a in letter_counts:
        for b in letter_counts:
            if letter_counts[a] > 1 and letter_counts[b] > 1 and (a != b):
                palindrome_candidate = a + b + b + a
                if all((palindrome_candidate.count(letter) <= letter_counts[letter] for letter in set(palindrome_candidate))):
                    possible_palindromes.add(palindrome_candidate)
            if letter_counts[a] > 3:
                palindrome_candidate = a + a + a + a
                possible_palindromes.add(palindrome_candidate)
            if letter_counts[a] > 1:
                palindrome_candidate = a + a
                if all((palindrome_candidate.count(letter) <= letter_counts[letter] for letter in set(palindrome_candidate))):
                    possible_palindromes.add(palindrome_candidate)
    return possible_palindromes