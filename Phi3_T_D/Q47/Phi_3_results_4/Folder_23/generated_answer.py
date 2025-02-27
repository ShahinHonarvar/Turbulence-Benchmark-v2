def palindromes_of_specific_lengths(text):
    text = text[23:95].lower()
    palindromes = set()
    for length in range(17, 56):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes