def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    length = len(s)
    result_set = set()
    for i in range(length):
        for j in range(i + 91, length + 1):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                result_set.add(sub)
    return result_set