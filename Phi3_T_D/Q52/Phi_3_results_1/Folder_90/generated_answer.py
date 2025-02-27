def is_palindrome(string):
    return string.lower() == string[::-1].lower()

def all_substrings(string, length):
    return [string[i:i + length] for i in range(len(string) - length + 1)]

def palindrome_of_length_n(string):
    length = 318
    palindromes = {substring for substring in all_substrings(string, length) if is_palindrome(substring)}
    return palindromes