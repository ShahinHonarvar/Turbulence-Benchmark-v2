def palindromes_of_specific_lengths(s):
    substring = s[12:57].lower()
    palindromes = set()
    palindrome_lengths = range(20, 22)
    for length in palindrome_lengths:
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes