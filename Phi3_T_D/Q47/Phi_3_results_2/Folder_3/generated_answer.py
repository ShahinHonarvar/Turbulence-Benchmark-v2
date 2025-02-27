import re

def palindromes_of_specific_lengths(s):
    subset = s[27:96]
    palindromes = set()
    for length in range(49, 52):
        for i in range(len(subset) - length + 1):
            substring = subset[i:i + length]
            alpha_only = re.sub('[^a-zA-Z]', '', substring)
            if len(alpha_only) == length and alpha_only.lower() == alpha_only[::-1].lower():
                palindromes.add(alpha_only)
    return palindromes