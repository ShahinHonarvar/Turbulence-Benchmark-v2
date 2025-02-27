def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    string = s.lower()
    OFFSET = 67
    palindromes = set()
    for i in range(len(string) - OFFSET + 1):
        substring = string[i:i + OFFSET]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes