def palindrome_of_length_at_least_n(s):

    def find_palindromes(s, left, right, palindromes):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
            if s[left].lower() != s[right].lower():
                break
            if right - left + 1 >= 64:
                palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        find_palindromes(s, i, i, palindromes)
        find_palindromes(s, i, i + 1, palindromes)
    return palindromes