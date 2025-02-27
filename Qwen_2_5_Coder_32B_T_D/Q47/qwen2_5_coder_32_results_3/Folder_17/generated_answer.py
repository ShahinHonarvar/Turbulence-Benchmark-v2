import re

def palindromes_of_specific_lengths(s):
    s = s[22:96].lower()
    p = re.compile('[a-z]')
    letters_only = ''.join(p.findall(s))
    result = set()
    for i in range(len(letters_only) - 51):
        for length in range(52, 56):
            substring = letters_only[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result