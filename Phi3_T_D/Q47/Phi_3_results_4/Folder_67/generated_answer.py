def palindromes_of_specific_lengths(s):
    s = s[64:99].lower()
    palindromes = set()
    for length in range(26, 34):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes