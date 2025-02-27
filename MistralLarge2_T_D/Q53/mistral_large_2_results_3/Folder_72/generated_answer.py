def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 88
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes