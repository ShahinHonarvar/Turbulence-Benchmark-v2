def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    s = s[15:96]
    for length in range(20, 67):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring.isalpha():
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes