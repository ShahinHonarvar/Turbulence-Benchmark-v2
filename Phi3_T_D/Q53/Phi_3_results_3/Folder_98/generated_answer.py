from itertools import combinations

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    result_set = set()

    def is_palindrome(s):
        return s == s[::-1]
    for length in range(6, len(string) + 1):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                result_set.add(substring)
    return result_set