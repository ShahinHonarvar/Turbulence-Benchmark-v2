def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()

    def is_palindrome(subs):
        return subs == subs[::-1]
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            if j - i >= 3 and is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result