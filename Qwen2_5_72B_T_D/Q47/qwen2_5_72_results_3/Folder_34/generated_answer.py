def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[200:301]
    result = set()
    for i in range(len(s)):
        for j in range(i + 10, min(i + 51, len(s) + 1)):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                result.add(s[i:j].lower())
    return result