def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    for length in range(109, 127):
        for start in range(125, 284):
            end = start + length
            if end <= len(s):
                substring = s[start:end]
                if is_palindrome(substring):
                    result.add(substring)
    return result