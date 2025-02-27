def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    for length in range(3, 5):
        for start in range(0, 5 - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring.lower())
    return result