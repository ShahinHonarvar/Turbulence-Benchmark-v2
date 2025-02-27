def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    result = set()
    for i in range(len(s) - 21):
        for j in range(i + 22, len(s) + 1):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result