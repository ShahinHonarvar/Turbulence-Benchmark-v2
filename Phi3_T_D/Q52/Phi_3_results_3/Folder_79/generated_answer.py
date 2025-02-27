def palindrome_of_length_n(s):
    length = 64
    s = s.lower()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = {s[i:i + length] for i in range(len(s) - length + 1) if is_palindrome(s[i:i + length]) and set(s[i:i + length]).issubset('abcdefghijklmnopqrstuvwxyz')}
    return palindromes