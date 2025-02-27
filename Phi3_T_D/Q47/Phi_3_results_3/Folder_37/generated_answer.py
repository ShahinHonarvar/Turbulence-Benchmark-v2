def palindromes_of_specific_lengths(text):
    palindromes = set()
    if len(text) < 10:
        return palindromes
    for i in range(9):
        for length in range(3, 6):
            if i + length > 9:
                break
            substr = text[i:i + length].lower()
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes