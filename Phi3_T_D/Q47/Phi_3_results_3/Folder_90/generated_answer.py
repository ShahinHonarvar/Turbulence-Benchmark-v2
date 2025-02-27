def palindromes_of_specific_lengths(s):
    substring = s[106:281]
    palindromes = {substring[i:j] for i in range(len(substring)) for j in range(i + 136, i + 152 + 1) if substring[i:j].lower() == substring[i:j][::-1] and substring[i:j].isalpha()}
    return palindromes