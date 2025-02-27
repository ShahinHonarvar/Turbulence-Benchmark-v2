def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[15:87].lower()
    result = set()
    for i in range(len(s) - 50):
        for length in range(51, 61):
            if i + length <= len(s):
                candidate = s[i:i + length]
                if candidate.isalpha() and is_palindrome(candidate):
                    result.add(candidate)
    return result