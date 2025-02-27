def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    s = s.lower()
    for i in range(len(s) - 6):
        substring = s[i:i + 7]
        if is_palindrome(substring):
            result.add(substring)
    return result