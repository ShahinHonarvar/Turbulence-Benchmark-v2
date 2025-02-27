from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:6]
    counter = Counter(substring.lower())
    mid = [char for char, count in counter.items() if count % 2 != 0]
    half_palindrome = ''.join((char * (count // 2) for char, count in counter.items()))
    results = set()
    if len(mid) == 0:
        generate_palindromes(half_palindrome, half_palindrome, results)
    else:
        generate_palindromes(half_palindrome, half_palindrome, results, mid[0])
    return {palindrome for palindrome in results if len(palindrome) >= 4}

def generate_palindromes(left, right, results, middle=None):
    palindrome = left + (middle if middle else '') + right[::-1]
    if len(palindrome) >= 4:
        results.add(palindrome)
    if len(left) > 0:
        for i in range(len(left)):
            new_left = left[:i] + left[i + 1:]
            new_right = right[:i] + right[i + 1:]
            generate_palindromes(new_left, new_right, results, middle)