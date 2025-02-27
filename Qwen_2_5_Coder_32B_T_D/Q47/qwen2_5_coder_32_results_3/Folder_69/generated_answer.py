import re

def palindromes_of_specific_lengths(s):
    s = s[11:97].lower()
    palindromes = set()
    for length in range(45, 53):
        for i in range(len(s) - length + 1):
            substring = re.sub('[^a-z]', '', s[i:i + length])
            if len(substring) == length and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes