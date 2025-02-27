def palindrome_of_length_at_least_n(s):
    text = s.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 5, len(text) + 1):
            substring = text[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes