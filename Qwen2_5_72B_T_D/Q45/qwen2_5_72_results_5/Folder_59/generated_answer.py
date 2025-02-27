from collections import Counter

def palindromes_between_indices(s):
    substring = s[8:10].lower()
    counter = Counter(substring)
    middle = [char for char, freq in counter.items() if freq % 2 != 0]
    half_palindrome = ''.join([char * (freq // 2) for char, freq in counter.items()])
    palindromes = set()
    if len(middle) <= 1 and len(half_palindrome) >= 1:
        for i in range(len(half_palindrome) + 1):
            for comb in set([''.join(p) for p in itertools.permutations(half_palindrome, i)]):
                if middle:
                    palindrome = comb + middle[0] + comb[::-1]
                else:
                    palindrome = comb + comb[::-1]
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes