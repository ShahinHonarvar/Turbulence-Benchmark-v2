def palindrome_of_length_at_least_n(s):
    n = 96
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n - 1, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes