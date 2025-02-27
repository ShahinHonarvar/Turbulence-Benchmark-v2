def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    result_set = set()
    for i in range(len(s) - 67):
        substring = s[i:i + 68]
        if all((c.isalpha() for c in substring)) and is_palindrome(substring):
            result_set.add(substring.lower())
    return result_set