def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[75:96].lower()
    result = set()
    for i in range(len(s) - 6):
        for j in range(i + 6, min(i + 10, len(s) + 1)):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result