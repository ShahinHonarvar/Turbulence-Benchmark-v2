def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 75, length):
            sub = s[i:j + 1]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result