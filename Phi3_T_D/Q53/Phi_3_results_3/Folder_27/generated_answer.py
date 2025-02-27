def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    result_set = set()
    for i in range(len(s)):
        for j in range(i + 99, len(s) + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                result_set.add(sub)
    return result_set