def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 37):
        if s[i:i + 38].isalpha():
            substr = s[i:i + 38]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes