def palindrome_of_length_at_least_n(s):
    n = 27
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n - 1, len(s)):
            substring = s[i:j + 1]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes