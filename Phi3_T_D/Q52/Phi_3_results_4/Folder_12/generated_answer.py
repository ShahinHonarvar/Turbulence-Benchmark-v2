def palindrome_of_length_n(text):
    txt_lower = text.lower()
    palindromes = set()
    for i in range(len(txt_lower) - 22):
        substring = txt_lower[i:i + 23]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes