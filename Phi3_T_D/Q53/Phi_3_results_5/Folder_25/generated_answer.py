def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 38, length + 1):
            substr = s[i:j]
            if substr == substr[::-1] and all((c.isalpha() for c in substr)):
                palindromes.add(substr)
    return palindromes