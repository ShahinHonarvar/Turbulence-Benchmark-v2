def longest_palindrome_at_start(s, k):
    for i in range(min(len(s), k)):
        if s[i] != s[-1 - i]:
            return False
    return True

def expand_around_center(s, left, right, odd):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        if odd and left != right:
            yield s[left:right + 1]
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(string):
    results = set()
    count = {}
    for char in string:
        if char.isalpha():
            count[char.lower()] = count.get(char.lower(), 0) + 1
        if all((val >= 2 for val in count.values())):
            if len(count) >= 2:
                center = len(count) // 2
                for left in range(center * 2 - 1, 0, -2):
                    if longest_palindrome_at_start(string, left):
                        start = (left - 1) // 2
                        result = expand_around_center(string, start - 1, start, left % 2 == 1)
                        results.update(result)
            if all((val == 2 for val in count.values())):
                for i in count:
                    if len(string) > len(i) * 2:
                        result = expand_around_center(string, 0, len(string) // 2 - 1, True)
                        results.update(result)
            break
    return {palindrome.upper() for palindrome in results if len(palindrome) >= 28}