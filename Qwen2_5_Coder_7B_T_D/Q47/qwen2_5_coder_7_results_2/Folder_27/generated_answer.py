def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    for i in range(13, 100):
        for j in range(i, min(i + 30, len(s))):
            if j - i + 1 >= 26 and j - i + 1 <= 29 and is_palindrome(s[i:j + 1]):
                result.add(s[i:j + 1])
    return result