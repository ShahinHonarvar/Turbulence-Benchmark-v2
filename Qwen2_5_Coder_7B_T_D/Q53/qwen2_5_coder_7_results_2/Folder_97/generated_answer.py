def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1] and sub.isalpha()
    s = s.lower()
    result = set()
    for i in range(len(s) - 137):
        for j in range(i + 137, len(s) + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result