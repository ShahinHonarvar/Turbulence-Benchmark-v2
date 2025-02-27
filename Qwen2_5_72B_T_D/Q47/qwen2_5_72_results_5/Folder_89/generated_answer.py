def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substr = s[18:89].lower()
    palindromes = set()
    for length in range(12, 15):
        for start in range(len(substr) - length + 1):
            if is_palindrome(substr[start:start + length]):
                if substr[start:start + length].isalpha():
                    palindromes.add(substr[start:start + length])
    return palindromes