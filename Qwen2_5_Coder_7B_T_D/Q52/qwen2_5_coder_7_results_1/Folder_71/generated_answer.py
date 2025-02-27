def palindrome_of_length_n(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    s = s.lower()
    result = set()
    for i in range(len(s) - 77):
        subs = s[i:i + 78]
        if is_palindrome(subs) and subs.isalpha():
            result.add(subs)
    return result