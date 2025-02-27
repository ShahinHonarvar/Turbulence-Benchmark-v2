from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:10]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    possible_palindromes = set()
    for char, count in letter_counts.items():
        if count >= 3:
            possible_palindromes.add(char * 6)
        if count >= 2:
            for char2, count2 in letter_counts.items():
                if char2 != char and count2 >= 2:
                    possible_palindromes.add(char * 3 + char2 * 3)
    return possible_palindromes