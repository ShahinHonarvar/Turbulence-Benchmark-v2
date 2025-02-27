def palindromes_of_specific_lengths(s):
    substring = s[36:93]
    return {substring[i:j + 1].lower() for i in range(len(substring)) for j in range(i, min(i + 35, len(substring))) if substring[i:j + 1].isalpha() and substring[i:j + 1].lower() == substring[i:j + 1].lower()[::-1] and (10 <= len(substring[i:j + 1]) <= 35)}