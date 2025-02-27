def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1] and sub.isalpha()
    result = set()
    for length in range(5, 11):
        for start in range(100, min(201, len(s) - length + 1)):
            substring = s[start:start + length]
            if is_palindrome(substring):
                result.add(substring.lower())
    return result