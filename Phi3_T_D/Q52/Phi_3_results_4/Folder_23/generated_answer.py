def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    s = s.lower()
    length = 69
    for i in range(len(s) - length + 1):
        word = s[i:i + length]
        if word.isalpha() and is_palindrome(word):
            palindromes.add(word)
    return palindromes