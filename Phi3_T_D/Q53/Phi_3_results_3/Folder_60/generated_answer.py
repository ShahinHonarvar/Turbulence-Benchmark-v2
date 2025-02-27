def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 80, len(s) + 1):
            word = s[i:j]
            if all((c.isalpha() for c in word)) and word == word[::-1]:
                palindromes.add(word)
    return palindromes