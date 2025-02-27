def palindromes_of_specific_lengths(s):
    start_idx = 10
    end_idx = 59
    min_len = 18
    max_len = 36
    s = s[start_idx:end_idx + 1].lower()
    result = set()

    def is_palindrome(subs):
        return subs == subs[::-1]
    for length in range(min_len, max_len + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result