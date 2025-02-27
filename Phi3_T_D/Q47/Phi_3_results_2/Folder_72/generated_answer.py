import re

def palindromes_of_specific_lengths(s):
    start_index = 26
    end_index = 90
    sub_string = s[start_index:end_index + 1].lower()
    valid_characters = re.compile('[a-z]')
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(sub_string) - length + 1):
            substring = sub_string[i:i + length]
            if valid_characters.match(substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes