def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 89):
        substr = s[i:i + 96]
        if all((c.isalpha() for c in substr)) and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes