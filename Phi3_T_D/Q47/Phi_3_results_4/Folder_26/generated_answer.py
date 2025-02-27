def palindromes_of_specific_lengths(text):
    start, end = (24, 84)
    palindromes = set()
    for length in range(21, 32):
        for i in range(start, end - length + 1):
            substring = text[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes