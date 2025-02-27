def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 29, n + 1):
            word = s[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes