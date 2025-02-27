def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    return {s[i:i + 289] for i in range(len(s) - 288) if is_palindrome(s[i:i + 289]) and s[i:i + 289].isalpha()}