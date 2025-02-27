def palindrome_of_length_n(text):
    n = 7
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes