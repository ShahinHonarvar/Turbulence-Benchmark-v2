def is_valid_char(char):
    return 'a' <= char <= 'z'

def generate_palindromes(s, length):
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        lower_substring = substring.lower()
        if substring == lower_substring[::-1] and all((is_valid_char(c) for c in lower_substring)):
            palindromes.add(substring)
    return palindromes

def palindrome_of_length_n(s):
    return generate_palindromes(s, 42)