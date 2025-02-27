def palindromes_of_specific_lengths(s):
    middle = s[18:89]
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(middle) - length + 1):
            substr = middle[i:i + length]
            if all((c.isalpha() for c in substr)) and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes