def palindrome_of_length_at_least_n(s):

    def all_substrings(string, min_length):
        length = len(string)
        return [string[i:j] for i in range(length) for j in range(i + min_length, length + 1)]

    def is_palindrome(string):
        return string.lower() == string[::-1].lower()
    substrings = all_substrings(s, 32)
    return {sub for sub in substrings if is_palindrome(sub) and sub.isalpha()}