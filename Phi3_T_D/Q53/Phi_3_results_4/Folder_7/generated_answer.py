def find_palindromes(s, mid, length):
    substr = s[mid - length // 2:mid + (length + 1) // 2]
    return substr == substr[::-1]

def palindrome_of_length_at_least_n(s):
    res = set()
    s = s.lower()
    for length in range(122, len(s) + 1):
        for mid in range(length // 2, len(s) - (length - 1) // 2):
            if find_palindromes(s, mid, length):
                res.add(s[mid - length // 2:mid + length // 2 + length % 2])
    return {x for x in res if x.isalpha()}