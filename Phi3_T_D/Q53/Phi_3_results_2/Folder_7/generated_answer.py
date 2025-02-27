def find_palindromes_in_substring(s, length, i):
    while i + length <= len(s):
        substring = s[i:i + length]
        if substring.lower() == substring[::-1].lower() and substring.isalpha():
            yield substring.lower()
        i += 1

def palindrome_of_length_at_least_n(s):
    result_set = set()
    s = s.lower()
    for length in range(122, len(s) + 1):
        result_set.update(find_palindromes_in_substring(s, length, 0))
    return result_set