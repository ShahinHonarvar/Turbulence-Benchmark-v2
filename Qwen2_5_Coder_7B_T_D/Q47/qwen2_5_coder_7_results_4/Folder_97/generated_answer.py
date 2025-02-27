def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[28:95]
    result = set()
    for i in range(len(s) - 48):
        substring = s[i:i + 49]
        if is_palindrome(substring) and substring.isalpha():
            result.add(substring)
    return result