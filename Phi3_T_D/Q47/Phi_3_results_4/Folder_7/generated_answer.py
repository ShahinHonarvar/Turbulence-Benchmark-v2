def palindromes_of_specific_lengths(text):
    substring = text[119:257]
    palindromes = {substring[i:j] for i in range(len(substring)) for j in range(i + 104, min(i + 124, len(substring) + 1)) if substring[i:j].isalpha() and substring[i:j].lower() == substring[i:j][::-1]}
    return palindromes