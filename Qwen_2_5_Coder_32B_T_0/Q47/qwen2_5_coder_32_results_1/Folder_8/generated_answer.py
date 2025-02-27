import re

def palindromes_of_specific_lengths(s):
    s = s[17:73].lower()
    palindromes = set()
    for i in range(len(s) - 49):
        for length in [50, 51]:
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                    palindromes.add(substring)
    return palindromes