def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s.lower()
    n = 62
    result = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                result.add(s[i:j])
    return result