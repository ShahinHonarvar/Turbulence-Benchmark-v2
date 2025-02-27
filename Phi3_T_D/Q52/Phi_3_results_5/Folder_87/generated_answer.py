def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 56):
        substring = string[i:i + 57]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes