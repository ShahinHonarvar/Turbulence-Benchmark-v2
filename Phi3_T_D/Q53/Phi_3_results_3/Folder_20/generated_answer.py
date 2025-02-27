def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
            if s[left].lower() == s[right].lower():
                yield s[left:right + 1]
            else:
                break
            left -= 1
            right += 1

    def find_palindromes_with_center(left, right):
        palindromes = set()
        for palindrome in expand_around_center(left, right):
            if len(palindrome) >= 66:
                palindromes.add(palindrome.lower())
        return palindromes
    all_palindromes = set()
    for i in range(len(s)):
        palindromes = find_palindromes_with_center(i, i)
        all_palindromes.update(palindromes)
        palindromes = find_palindromes_with_center(i, i + 1)
        all_palindromes.update(palindromes)
    return all_palindromes