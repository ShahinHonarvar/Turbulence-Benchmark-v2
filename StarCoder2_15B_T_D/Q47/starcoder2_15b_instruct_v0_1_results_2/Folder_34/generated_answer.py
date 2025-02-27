def palindromes_of_specific_lengths(text):
    palindromes = set()
    lower_text = text.lower()
    for length in range(10, 51):
        for i in range(200, len(lower_text) - length + 1):
            substring = lower_text[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes