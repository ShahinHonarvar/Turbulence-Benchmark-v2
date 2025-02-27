def palindrome_of_length_at_least_n(s):
    if len(s) < 144:
        return set()

    def find_palindromes(s, current, index, result):
        if current:
            result.add(current)
        for i in range(index, len(s)):
            if s[i].isalpha() and (len(current) + 1 >= 144 or len(current) < 144):
                find_palindromes(s, current + s[i], i + 1, result)
            if len(current) >= 144 and current == current[::-1]:
                break
    result_set = set()
    find_palindromes(s.lower(), '', 0, result_set)
    return result_set