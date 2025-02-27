def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()

    def is_palindrome(sub_str):
        return sub_str == sub_str[::-1]
    for i in range(len(s)):
        for j in range(i + 29, len(s) + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                result.add(substr)
    return result