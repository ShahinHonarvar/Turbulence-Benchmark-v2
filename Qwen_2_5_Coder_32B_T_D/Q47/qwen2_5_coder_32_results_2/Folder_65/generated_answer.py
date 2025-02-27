import re

def palindromes_of_specific_lengths(s):
    s = s[15:96].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for length in range(20, 67):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes