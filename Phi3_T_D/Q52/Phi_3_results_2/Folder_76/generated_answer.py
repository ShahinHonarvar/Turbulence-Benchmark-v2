def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    palindromes = set()
    length = 257
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if all((char.isalpha() for char in substring)) and is_palindrome(substring):
            palindromes.add(substring.lower())
    return palindromes