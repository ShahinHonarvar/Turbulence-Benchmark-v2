def palindromes_of_specific_lengths(s):
    s = s[100:296]
    palindromes = set()
    for i in range(136, 161):
        for start in range(len(s) - i + 1):
            substr = s[start:start + i]
            if substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes