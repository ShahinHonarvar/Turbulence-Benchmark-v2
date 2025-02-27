def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    s = s.lower()
    length = 88
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes