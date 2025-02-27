def palindrome_of_length_n(s):

    def is_palindrome(subs):
        return subs.lower() == subs[::-1].lower()
    result_set = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - 8):
        substr = s_lower[i:i + 9]
        if is_palindrome(substr):
            result_set.add(substr)
    return result_set