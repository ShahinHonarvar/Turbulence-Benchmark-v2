def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()

    def is_palindrome(subs):
        return subs == subs[::-1]
    for i in range(len(s)):
        for j in range(i + 31, len(s) + 1):
            subs = s[i:j]
            if is_palindrome(subs):
                result.add(subs)
    return result