from collections import Counter

def palindromes_between_indices(s):
    substring = s[0:5]
    counter = Counter(substring.lower())
    center = [char for char, count in counter.items() if count % 2 != 0]
    if len(center) > 1:
        return set()
    half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
    palindromes = set()
    for i in range(3, len(half_palindrome) * 2 + 2):
        if i % 2 == 0:
            for j in range(len(half_palindrome) - i // 2 + 1):
                palindrome = half_palindrome[j:j + i // 2] + half_palindrome[j:j + i // 2][::-1]
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
        else:
            for j in range(len(half_palindrome) - i // 2 + 1):
                for c in center:
                    palindrome = half_palindrome[j:j + i // 2] + c + half_palindrome[j:j + i // 2][::-1]
                    if len(palindrome) >= 3:
                        palindromes.add(palindrome)
    return palindromes