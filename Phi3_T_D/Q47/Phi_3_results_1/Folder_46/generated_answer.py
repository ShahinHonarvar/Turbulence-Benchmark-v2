def palindromes_of_specific_lengths(s):
    length_range = range(29, 63)
    substring = s[11:98]
    palindromes = set()
    for length in length_range:
        for i in range(11, len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.lower() == substr[::-1].lower() and substr.isalpha():
                palindromes.add(substr.lower())
    return palindromes