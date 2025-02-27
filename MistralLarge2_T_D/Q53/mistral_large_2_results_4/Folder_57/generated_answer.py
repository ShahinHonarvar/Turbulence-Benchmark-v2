def palindrome_of_length_at_least_n(string):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    n = 93
    string = ''.join((c for c in string if c.isalpha())).lower()
    for length in range(n, len(string) + 1):
        for start in range(len(string) - length + 1):
            substring = string[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes