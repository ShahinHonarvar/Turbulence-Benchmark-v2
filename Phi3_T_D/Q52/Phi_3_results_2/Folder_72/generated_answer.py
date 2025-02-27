def is_valid_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    length = 16
    for i in range(len(string) - length + 1):
        if all((c.isalpha() for c in string[i:i + length])):
            substr = string[i:i + length]
            if is_valid_palindrome(substr):
                palindromes.add(substr)
    return palindromes