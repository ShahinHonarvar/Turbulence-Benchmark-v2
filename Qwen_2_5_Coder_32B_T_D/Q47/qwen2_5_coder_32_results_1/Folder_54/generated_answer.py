import re

def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    palindromes = set()
    for i in range(len(s) - 17):
        for j in range(i + 18, i + 20):
            if j <= len(s):
                substring = re.sub('[^a-z]', '', s[i:j])
                if substring == substring[::-1] and 18 <= len(substring) <= 19:
                    palindromes.add(substring)
    return palindromes