def palindrome_of_length_n(text, n=73):
    text = text.lower()
    length = len(text)
    if length < n:
        return set()
    palindromes = set()
    for i in range(length - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes