def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(string) - 88):
        substring = string[i:i + 88]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes