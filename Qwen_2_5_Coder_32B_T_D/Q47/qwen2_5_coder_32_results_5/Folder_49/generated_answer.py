def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[10:101].lower()
    result = set()
    for start in range(len(s) - 9):
        for end in range(start + 10, min(start + 51, len(s) + 1)):
            substring = ''.join(filter(str.isalpha, s[start:end]))
            if len(substring) >= 10 and is_palindrome(substring):
                result.add(substring)
    return result