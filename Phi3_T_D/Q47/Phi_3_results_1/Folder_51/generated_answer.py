def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    for i in range(2, 8):
        for length in range(3, 5):
            if i + length <= 8:
                substring = s[i:i + length]
                if substring.isalpha() and is_palindrome(substring):
                    result.add(substring.lower())
    return result