def palindrome_of_length_n(text):
    n = 64
    valid_chars_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n].lower()
        if all((char in valid_chars_set for char in substring)) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes