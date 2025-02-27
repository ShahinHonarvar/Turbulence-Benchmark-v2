def palindromes_of_specific_lengths(s):
    sub_s = s[15:95]
    sub_s_lower = sub_s.lower()
    result = set()
    for length in range(18, 74):
        for i in range(len(sub_s_lower) - length + 1):
            if sub_s_lower[i] not in 'abcdefghijklmnopqrstuvwxyz' or not sub_s_lower[i].isalpha():
                continue
            palindrome_candidate = sub_s_lower[i:i + length]
            if palindrome_candidate == palindrome_candidate[::-1]:
                result.add(sub_s[i:i + length])
    return result