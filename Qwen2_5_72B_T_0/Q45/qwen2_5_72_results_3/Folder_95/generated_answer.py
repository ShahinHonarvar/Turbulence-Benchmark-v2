from collections import Counter

def palindromes_between_indices(s):
    substring = s[7:9].lower()
    counter = Counter(substring)
    middle = [char for char, count in counter.items() if count % 2 != 0]
    half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
    palindromes = set()
    if len(middle) <= 1 and len(half_palindrome) >= 1:
        for i in range(len(half_palindrome) + 1):
            for j in range(len(middle) + 1):
                candidate = half_palindrome[:i] + middle[0] * j + half_palindrome[i:][::-1]
                if len(candidate) >= 3:
                    palindromes.add(candidate)
    return palindromes