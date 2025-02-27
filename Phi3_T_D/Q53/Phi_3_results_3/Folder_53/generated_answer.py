def palindrome_of_length_at_least_n(input_string):

    def find_palindromes(s, i, j, n):
        while i >= 0 and j < len(s) and (n >= 64):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower():
                result.add(s[i:j + 1])
                i -= 1
                j += 1
            elif s[i:j + 1].lower() < s[i:j + 1][::-1].lower():
                i += 1
            else:
                j += 1
            n += 1
    result = set()
    for i in range(len(input_string)):
        find_palindromes(input_string, i, i, 0)
        find_palindromes(input_string, i, i + 1, 0)
    return result