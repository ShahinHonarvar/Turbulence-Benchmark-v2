def palindrome_of_length_n(s: str):
    s = s.lower()
    palindromes = {s[i:i + 74] for i in range(len(s) - 73) if s[i:i + 74].isalpha()}
    valid_palindromes = {substring for substring in palindromes if substring == substring[::-1]}
    return valid_palindromes