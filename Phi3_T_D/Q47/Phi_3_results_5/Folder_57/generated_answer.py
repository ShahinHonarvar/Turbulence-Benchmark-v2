def palindromes_of_specific_lengths(s):
    substring = s[16:95]
    return {substring[i:j] for i in range(len(substring)) for j in range(i + 39, i + 53) if substring[i:j].isalpha() and substring[i:j].lower() == substring[i:j][::-1]}