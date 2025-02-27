def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[12:57]
    palindromes = set()
    for length in [20, 21]:
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes