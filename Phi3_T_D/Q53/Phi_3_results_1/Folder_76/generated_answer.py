def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]

    def get_palindromes(string):
        palindromes = set()
        length = len(string)
        for i in range(length):
            for j in range(i + 137, length + 1):
                substring = string[i:j]
                if is_palindrome(substring):
                    palindromes.add(substring.lower())
        return palindromes
    return get_palindromes(s)