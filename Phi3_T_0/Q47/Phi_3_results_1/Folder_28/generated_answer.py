def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_palindrome(word):
        return is_palindrome(word) and 21 <= len(word) <= 32 and word.isalpha()
    start, end = (32, 71)
    substring = s[start:end + 1].lower()
    palindromes = set()
    for length in range(21, 33):
        for i in range(len(substring) - length + 1):
            if valid_palindrome(substring[i:i + length]):
                palindromes.add(substring[i:i + length])
    return palindromes