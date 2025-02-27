import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[32:72].lower()
    for length in range(21, 33):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i + length]
            if re.match('^[a-z]+$', substring_slice) and substring_slice == substring_slice[::-1]:
                result.add(substring_slice)
    return result