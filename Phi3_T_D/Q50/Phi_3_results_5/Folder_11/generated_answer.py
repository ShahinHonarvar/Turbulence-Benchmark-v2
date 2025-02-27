def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for s in string_list:
        if len(s) >= 3:
            norm_s = normalize(s)
            if norm_s in anagrams:
                anagrams[norm_s].append(s)
            else:
                anagrams[norm_s] = [s]
    count = 0
    for key in anagrams:
        count += combination(len(anagrams[key]), 2)
    return count >= 28

def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)