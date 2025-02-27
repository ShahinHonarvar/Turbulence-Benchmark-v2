import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    lower_case_string = string.lower()
    sub_string = lower_case_string[39:95]
    pattern = re.compile('[a-z]')
    matches = pattern.findall(sub_string)
    for length in range(14, 53):
        for i in range(len(matches) - length + 1):
            candidate = matches[i:i + length]
            if candidate == candidate[::-1]:
                palindromes.add(''.join(candidate))
    return palindromes