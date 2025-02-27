def palindrome_of_length_n(s):
    s = s.lower()
    result = set()

    def is_palindrome(sub_str):
        return sub_str == sub_str[::-1]
    for i in range(len(s) - 205):
        if is_palindrome(s[i:i + 206]):
            result.add(s[i:i + 206])
    return result