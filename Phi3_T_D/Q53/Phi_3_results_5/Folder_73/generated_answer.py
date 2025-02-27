def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(94, len(s) - start + 1):
            word = s[start:start + length]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes