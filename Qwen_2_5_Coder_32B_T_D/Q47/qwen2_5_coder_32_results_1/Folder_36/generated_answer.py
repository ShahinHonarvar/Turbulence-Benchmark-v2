def palindromes_of_specific_lengths(s):
    s = s[124:284].lower()
    palindromes = set()
    for start in range(len(s) - 114):
        for end in range(start + 114, min(start + 134, len(s)) + 1):
            substr = s[start:end]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes