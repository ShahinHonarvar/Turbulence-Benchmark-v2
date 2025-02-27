def find_palindromes(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            yield s[left:right + 1]
            left -= 1
            right += 1
    all_palindromes = set()
    for i in range(len(s)):
        for palindrome in expand_around_center(i, i):
            all_palindromes.add(palindrome)
        for palindrome in expand_around_center(i, i + 1):
            all_palindromes.add(palindrome)
    palindromes_of_desired_length = {palindrome for palindrome in all_palindromes if len(palindrome) >= 84}
    return palindromes_of_desired_length

def palindrome_of_length_at_least_n(s):
    return find_palindromes(s)