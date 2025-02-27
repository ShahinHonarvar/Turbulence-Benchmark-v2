def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def is_palindrome(sub):
        return sub == sub[::-1] and len(sub) >= 77
    words = s.split()
    return {word for word in words if is_palindrome(word)}