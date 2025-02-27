def palindrome_of_length_at_least_n(s):
    s = s.lower()
    chars = set('abcdefghijklmnopqrstuvwxyz')
    n = min(32, len(s))

    def is_palindrome(word):
        return word == word[::-1] and all((c in chars for c in word))

    def extend_palindrome(center):
        left = center - 1
        right = center + 1
        palindrome = [s[center]]
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            if len(palindrome) <= n:
                palindrome.append(s[right])
                palindrome.insert(0, s[left])
            left -= 1
            right += 1
        return ''.join(reversed(palindrome)) if len(palindrome) >= 32 else ''
    palindromes = set()
    for i in range(len(s)):
        palindrome = extend_palindrome(i)
        if palindrome and len(palindrome) >= n and is_palindrome(palindrome):
            palindromes.add(palindrome)
        palindrome = extend_palindrome(i)
        if palindrome and len(palindrome) >= n and is_palindrome(palindrome):
            palindromes.add(palindrome)
    return palindromes