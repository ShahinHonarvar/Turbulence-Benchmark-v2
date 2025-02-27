from itertools import combinations
import re

def palindromes_of_specific_lengths(s):
    substring = s[17:73].lower()
    valid_letters = re.sub('[^a-z]', '', substring)
    palindromes = set()
    for length in range(50, 52):
        for start in range(len(valid_letters) - length + 1):
            segment = valid_letters[start:start + length]
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes