def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    start_index = 155
    end_index = 283
    min_length = 104
    max_length = 120
    palindromes_set = set()
    for i in range(start_index, end_index + 1):
        for length in range(min_length, max_length + 1):
            if i + length <= end_index + 1:
                substring = s[i:i + length]
                if substring.isalpha() and is_palindrome(substring):
                    palindromes_set.add(substring.lower())
    return palindromes_set