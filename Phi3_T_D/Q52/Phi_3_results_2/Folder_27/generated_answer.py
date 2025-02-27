from collections import defaultdict

def palindrome_of_length_n(s):
    length = 56
    s = s.lower()
    count = defaultdict(int)
    window = [0] * 26
    n = len(s)
    palindromes = set()
    for i in range(n):
        window[ord(s[i]) - ord('a')] += 1
        if i >= length - 1:
            if all((val % 2 == 0 for val in window.values())):
                mid = (i + 1) // 2
                left = (i - mid) // 2
                count_dict = {}
                for j in range(mid):
                    c = s[left + count_dict.get(s[left + j - mid], 0)]
                    count_dict[c] = count_dict.get(c, 0) + 1
                is_palindrome = all((count_dict.get(c, 0) % 2 == 0 for c in count_dict))
                if is_palindrome:
                    for c in string.ascii_lowercase:
                        palindromes.add(c * (count_dict.get(c, 0) // 2 * 2) + s[left + count_dict.get(c, 0) // 2] + c * (count_dict.get(c, 0) // 2 * 2))
            window[ord(s[i - length + 1]) - ord('a')] -= 1
    return palindromes