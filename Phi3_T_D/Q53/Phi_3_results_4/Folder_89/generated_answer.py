def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 43, length + 1):
            sub_str = s[start:end].lower()
            if sub_str.isalpha() and is_palindrome(sub_str):
                result.add(sub_str)
    return result