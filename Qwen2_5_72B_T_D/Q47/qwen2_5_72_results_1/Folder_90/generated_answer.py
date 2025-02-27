def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    result = set()
    for i in range(106, 280 - 136 + 1):
        for j in range(i + 136, min(i + 152, 281)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result