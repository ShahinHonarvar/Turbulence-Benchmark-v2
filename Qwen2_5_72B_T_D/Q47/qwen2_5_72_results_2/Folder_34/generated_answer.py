def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    start, end = (200, 300)
    min_len, max_len = (10, 50)
    s = s[start:end + 1]
    palindromes = set()
    for length in range(min_len, max_len + 1):
        for start_index in range(len(s) - length + 1):
            substring = s[start_index:start_index + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes