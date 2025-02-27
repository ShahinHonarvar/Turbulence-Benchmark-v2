def palindromes_between_indices(s):

    def all_subsets(chars):
        if not chars:
            return [[]]
        subsets = all_subsets(chars[1:])
        return subsets + [[chars[0]] + subset for subset in subsets]

    def is_palindrome(sub_s):
        return sub_s == sub_s[::-1]
    chars = [c.lower() for c in s[3:9]]
    result = set()
    for subset in all_subsets(chars):
        sub_s = ''.join(subset)
        if len(sub_s) >= 4 and is_palindrome(sub_s):
            result.add(sub_s)
    return result