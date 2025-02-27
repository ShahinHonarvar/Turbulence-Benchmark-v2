def palindrome_of_length_at_least_n(input_string):
    if len(input_string) < 70:
        return set()

    def is_palindrome(s):
        return s == s[::-1]

    def valid_chars(s):
        return all(('A' <= c <= 'Z' or 'a' <= c <= 'z' for c in s))
    result = set()
    for i in range(len(input_string)):
        for j in range(i + 70, len(input_string) + 1):
            substring = input_string[i:j]
            lowered_substring = substring.lower()
            if len(lowered_substring) >= 70 and valid_chars(lowered_substring) and is_palindrome(lowered_substring):
                result.add(lowered_substring)
    return result