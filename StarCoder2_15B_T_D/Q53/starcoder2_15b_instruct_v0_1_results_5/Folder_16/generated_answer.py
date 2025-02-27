def palindrome_of_length_at_least_n(s):
    n = 119
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n - 1, len(s)):
            window = s[i:j + 1]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes