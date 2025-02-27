def palindrome_of_length_at_least_n(text):
    text = ''.join((c for c in text.lower() if c.isalpha()))
    palindromes = set()
    for i in range(len(text) - 26):
        substring = text[i:i + 27]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes