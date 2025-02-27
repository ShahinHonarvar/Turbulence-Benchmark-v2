def palindrome_of_length_at_least_n(input_string):
    candidates = set()

    def is_valid_palindrome(s):
        return s == s[::-1] and all((char.isalpha() for char in s))
    n = len(input_string)
    for i in range(n):
        for j in range(i + 95, n + 1):
            substr = input_string[i:j].lower()
            if is_valid_palindrome(substr):
                candidates.add(substr)
    return candidates