def palindromes_of_specific_lengths(s):
    start, end = (103, 276)
    target_str = s[start:end + 1]
    result_set = set()

    def is_valid_palindrome(sub):
        return all((c.isalpha() for c in sub)) and sub == sub[::-1]
    for length in range(100, 170):
        for i in range(start, end - length + 1):
            substr = target_str[i:i + length]
            if is_valid_palindrome(substr):
                result_set.add(substr.lower())
    return result_set