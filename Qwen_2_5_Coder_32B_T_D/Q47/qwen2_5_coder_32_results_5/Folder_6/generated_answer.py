def palindromes_of_specific_lengths(s):
    s = s[45:99].lower()
    palindromes = set()
    for length in range(40, 48):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes