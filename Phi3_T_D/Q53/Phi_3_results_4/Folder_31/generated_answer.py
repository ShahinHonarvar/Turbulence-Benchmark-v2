def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        for i in range(len(s) // 2):
            if s[i].lower() != s[-(i + 1)].lower():
                return False
        return True
    result = set()
    for length in range(34, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                result.add(substring)
    return result