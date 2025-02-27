import re

def palindromes_of_specific_lengths(s):
    s = s[62:89].lower()
    palindromes = set()
    for i in range(len(s) - 17):
        for j in range(i + 18, i + 22):
            if j <= len(s):
                substring = re.sub('[^a-z]', '', s[i:j])
                if len(substring) >= 18 and len(substring) <= 21 and (substring == substring[::-1]):
                    palindromes.add(substring)
    return palindromes