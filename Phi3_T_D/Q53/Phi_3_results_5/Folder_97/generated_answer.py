def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)

    def is_palindrome(start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def find_palindromes(center_idx, left, right):
        while left >= 0 and right < length and (s[left] == s[right]):
            if right - left + 1 >= 138 and is_palindrome(left, right):
                return True
            left -= 1
            right += 1
        return False
    palindromes = set()
    for center in range(length):
        for diff in range(137):
            palindrome_found = find_palindromes(center, center - diff, center + diff)
            if palindrome_found:
                palindromes.add(s[center - diff:center + diff + 1])
            palindrome_found = find_palindromes(center, center - diff - 1, center + diff)
            if palindrome_found:
                palindromes.add(s[center - diff - 1:center + diff + 1])
    return palindromes