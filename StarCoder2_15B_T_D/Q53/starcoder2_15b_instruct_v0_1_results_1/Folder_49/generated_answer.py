def palindrome_of_length_at_least_n(string):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    words = [word for word in string.split() if len(word) >= 73]
    palindromes = [word for word in words if is_palindrome(word)]
    return set(palindromes)