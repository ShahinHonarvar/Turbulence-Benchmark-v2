def find_palindromes_in_substrings(s):

    def expand_around_center(left, right):
        results = set()
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            results.add(s[left:right + 1])
            left -= 1
            right += 1
        return results
    all_palindromes = set()
    for i in range(len(s)):
        center = expand_around_center(i, i)
        all_palindromes.update(center)
        center = expand_around_center(i, i + 1)
        all_palindromes.update(center)
    return all_palindromes

def palindrome_of_length_at_least_n(s):
    return {palindrome for palindrome in find_palindromes_in_substrings(s) if len(palindrome) >= 17}