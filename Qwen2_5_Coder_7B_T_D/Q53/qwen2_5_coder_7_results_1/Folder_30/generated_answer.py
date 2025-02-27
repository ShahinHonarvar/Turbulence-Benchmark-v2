def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 16
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes