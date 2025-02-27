def palindrome_of_length_at_least_n(s):

    def is_palindrome(string):
        return string == string[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(5, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes