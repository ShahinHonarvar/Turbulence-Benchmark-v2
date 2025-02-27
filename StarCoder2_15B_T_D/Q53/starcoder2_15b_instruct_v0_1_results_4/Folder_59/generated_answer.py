def palindrome_of_length_at_least_n(text):
    palindromes = set()
    n = 20
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes