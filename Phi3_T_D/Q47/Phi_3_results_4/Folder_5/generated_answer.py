def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower() and word.isalpha()
    result = set()
    for length in range(4, 6):
        for i in range(63, 71 - length):
            if is_palindrome(s[i:i + length]):
                result.add(s[i:i + length].lower())
    return result