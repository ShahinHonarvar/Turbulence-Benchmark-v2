def palindrome_of_length_at_least_n(s):

    def extend_palindrome(left, right, low, high):
        while left >= low and right <= high and (s[left].lower() == s[right].lower()):
            yield (left, right)
            left -= 1
            right += 1
    palindromes = set()
    n = len(s)
    for i in range(n - 47):
        left, right = (i, i + 47)
        while left >= 0 and right < n:
            for pair in extend_palindrome(left, right, low=max(left - 1, 0), high=min(right + 1, n)):
                palindromes.add(s[pair[0]:pair[1] + 1].lower())
            left -= 1
            right += 1
    return palindromes