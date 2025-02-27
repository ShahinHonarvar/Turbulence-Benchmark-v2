def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()

    def valid_char(char):
        return 'a' <= char.lower() <= 'z'

    def valid_length(palindrome):
        return 10 <= len(palindrome) <= 50
    s = s[200:301]
    palindromes = set()
    length = 10
    while length <= 50:
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((valid_char(c) for c in substring)) and is_palindrome(substring) and valid_length(substring):
                palindromes.add(substring.lower())
        length += 1
    return palindromes