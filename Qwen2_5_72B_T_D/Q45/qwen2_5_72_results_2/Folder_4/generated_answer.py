from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    counter = Counter(substring)
    middle = [char for char, count in counter.items() if count % 2 != 0]
    half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
    if len(middle) > 1 or len(half_palindrome) < 3:
        return set()
    else:
        if middle:
            palindromes = {half_palindrome[:i] + middle[0] + half_palindrome[i:] for i in range(len(half_palindrome) + 1)}
        else:
            palindromes = {half_palindrome + half_palindrome[::-1]}
        return {palindrome for palindrome in palindromes if len(palindrome) >= 7}