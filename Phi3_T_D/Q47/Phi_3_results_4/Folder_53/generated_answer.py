from itertools import combinations_with_replacement

def palindromes_of_specific_lengths(s):
    substring = s[1:300]

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    palindromes = set()
    for l in range(3, 11):
        for combination in combinations_with_replacement('abcdefghijklmnopqrstuvwxyz', l):
            half_length = l // 2
            temp = ''.join(combination * half_length)
            palindrome_candidate = temp + temp[:l % 2]
            if is_palindrome(palindrome_candidate) and palindrome_candidate in substring:
                palindromes.add(palindrome_candidate)
    return palindromes