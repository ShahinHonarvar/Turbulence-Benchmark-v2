def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    length = 80
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes