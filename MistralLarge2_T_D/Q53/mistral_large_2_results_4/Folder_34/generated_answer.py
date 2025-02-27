def palindrome_of_length_at_least_n(string):

    def is_palindrome(s):
        return s == s[::-1]
    length = len(string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 68, length + 1):
            substring = string[i:j]
            if is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes