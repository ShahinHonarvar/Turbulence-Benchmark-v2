def palindrome_of_length_at_least_n(string):

    def is_palindrome(s):
        return s == s[::-1]
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 81, len(string) + 1):
            substring = string[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes