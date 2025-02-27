def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(1, len(text) - 9):
        for j in range(i + 7, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes