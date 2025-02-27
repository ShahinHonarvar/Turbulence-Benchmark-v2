def palindromes_of_specific_lengths(s):
    s = s[17:96]
    palindromes = set()
    for length in range(13, 50):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr.isalpha() and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes