import re

def palindromes_of_specific_lengths(s):
    s = s[32:72].lower()
    palindromes = set()
    for i in range(len(s) - 21 + 1):
        for j in range(21, 33):
            if i + j <= len(s):
                substring = re.sub('[^a-z]', '', s[i:i + j])
                if substring and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes