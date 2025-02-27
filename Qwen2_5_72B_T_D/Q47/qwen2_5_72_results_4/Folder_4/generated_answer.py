def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    for start in range(12, 93):
        for end in range(start + 16, min(93, start + 67)):
            sub = s[start:end + 1]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result