def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 223 + 1):
        substring = text[i:i + 223]
        if substring.lower() == substring[::-1].lower():
            if substring.isalpha():
                palindromes.add(substring)
    return palindromes