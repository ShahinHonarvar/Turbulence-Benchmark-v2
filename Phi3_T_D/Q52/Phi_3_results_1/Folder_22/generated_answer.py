def palindrome_of_length_n(string):
    length = 20
    palindromes = set()
    string = string.lower()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(string) - length + 1):
        if is_palindrome(string[i:i + length]) and all((c.isalpha() for c in string[i:i + length])):
            palindromes.add(string[i:i + length])
    return palindromes