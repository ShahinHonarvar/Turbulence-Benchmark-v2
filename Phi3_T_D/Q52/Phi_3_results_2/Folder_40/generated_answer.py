def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 2):
        substr = s[i:i + 3]
        if substr[0] == substr[2]:
            palindromes.add(substr)
    return palindromes