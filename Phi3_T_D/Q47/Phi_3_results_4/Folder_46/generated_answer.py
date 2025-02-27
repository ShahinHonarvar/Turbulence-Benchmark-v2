def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    substring = input_string[11:98].lower()
    ret_palindromes = set()
    for length in range(29, 63):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and is_palindrome(substr):
                ret_palindromes.add(substr)
    return ret_palindromes