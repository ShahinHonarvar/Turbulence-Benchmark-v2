import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[13:96].lower()
    for length in range(57, 61):
        for i in range(len(substring) - length + 1):
            substring_chunk = substring[i:i + length]
            if re.match('^[a-z]*$', substring_chunk) and substring_chunk == substring_chunk[::-1]:
                result.add(substring_chunk)
    return result