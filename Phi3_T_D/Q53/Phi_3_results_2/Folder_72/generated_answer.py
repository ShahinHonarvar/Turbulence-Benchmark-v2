def palindrome_of_length_at_least_n(s):
    s = s.lower()
    longest = min(len(s), 88)
    result_set = set()
    for i in range(len(s)):
        for j in range(i, longest)[::-1]:
            if j - i + 1 >= 88:
                chunk = s[i:j + 1]
                if chunk == chunk[::-1]:
                    result_set.add(chunk)
    return result_set