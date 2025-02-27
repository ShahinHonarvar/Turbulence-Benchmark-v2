def get_all_common_case_insensitive_arrangements(string):

    def permute(s, l, r, ans_set):
        if l == r:
            if s == s[::-1]:
                ans_set.add(s)
        else:
            swapped = False
            for i in range(l, r + 1):
                s = list(s)
                s[l], s[i] = (s[i], s[l])
                s = ''.join(s)
                permute(s, l + 1, r, ans_set)
                s = list(answer)
                s[l], s[i] = (s[i], s[l])
                s = ''.join(s)
                swapped = True
            if not swapped:
                break
    chars = sorted(set(string.lower()[4:9]), reverse=True)
    palindrome_set = set()
    permute(''.join(chars), 0, len(chars) - 1, palindrome_set)
    return palindrome_set

def palindromes_between_indices(s):
    sub_string = s[4:9]
    arrangements = get_all_common_case_insensitive_arrangements(sub_string)
    return {p.upper() for p in arrangements if len(p) >= 3}