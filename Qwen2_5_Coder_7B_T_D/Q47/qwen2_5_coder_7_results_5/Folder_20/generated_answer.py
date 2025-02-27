def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    for i in range(20, 75):
        for j in range(i + 36, min(len(s), j + 43)):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result