def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        length = len(s)
        results = set()
        while left >= 0 and right < length and ((left + right) % 2 == 1):
            palindrome = s[left:right + 1]
            if palindrome.lower() == palindrome[::-1].lower() and len(palindrome) >= 89:
                results.add(palindrome)
            left -= 1
            right += 1
        return results
    results = set()
    length = len(s)
    for i in range(length):
        results |= expand_around_center(i, i)
        if i + 1 < length and s[i].lower() == s[i + 1].lower():
            results |= expand_around_center(i, i + 1)
    return results