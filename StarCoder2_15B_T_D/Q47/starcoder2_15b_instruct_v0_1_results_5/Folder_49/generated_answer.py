def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text[10:101]
    for length in range(10, 51):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes