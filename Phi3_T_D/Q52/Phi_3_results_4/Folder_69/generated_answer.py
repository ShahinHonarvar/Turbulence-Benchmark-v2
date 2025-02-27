def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 471):
        substr = s[i:i + 472]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes