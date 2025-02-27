def palindrome_of_length_at_least_n(string):

    def is_palindrome(string):
        return string.lower() == string[::-1].lower()
    result = set()
    for i in range(len(string) - 2):
        for j in range(i + 3, len(string) + 1):
            substring = string[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result