def palindrome_of_length_at_least_n(string):

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    n = 64
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes