def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    for length in range(5, 81):
        for start in range(0, 21 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                result.add(substring)
    return result