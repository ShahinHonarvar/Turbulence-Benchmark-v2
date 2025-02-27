def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    start, end = (155, 283)
    palindromes = {s[i:i + length] for length in range(104, 121) for i in range(start, end - length + 1)}
    return {palindrome for palindrome in palindromes if palindrome.isalpha() and is_palindrome(palindrome)}