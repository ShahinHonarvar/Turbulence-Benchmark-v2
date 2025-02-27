import re

def is_english_letter(char):
    return re.match('[a-zA-Z]', char) is not None

def palindromes_of_specific_lengths(s):
    start = 15
    end = 72
    min_length = 19
    max_length = 55
    palindromes = set()
    for length in range(min_length, max_length + 1):
        for i in range(start, end - length + 2):
            substring = s[i:i + length]
            if all((is_english_letter(c) for c in substring)) and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes