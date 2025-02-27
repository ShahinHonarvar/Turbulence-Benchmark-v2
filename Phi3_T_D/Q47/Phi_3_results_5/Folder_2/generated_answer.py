def palindromes_of_specific_lengths(s):
    substring = s[10:60]
    palindromes = set()
    n = len(substring)
    for L in range(18, 37):
        for i in range(n - L + 1):
            substr = substring[i:i + L]
            if substr.isalpha() and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes