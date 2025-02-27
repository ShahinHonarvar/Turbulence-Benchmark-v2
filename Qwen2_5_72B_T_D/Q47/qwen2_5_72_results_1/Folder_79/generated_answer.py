def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    for length in range(3, 5):
        for start in range(1, 9 - length + 1):
            sub = s[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub.lower())
    return result