def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 19, len(s) + 1):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                result.add(s[i:j])
    return result