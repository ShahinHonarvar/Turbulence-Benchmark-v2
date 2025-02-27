from collections import defaultdict

def if_contains_anagrams(str_list):

    def gen_signature(s):
        return ''.join(sorted(s.lower()))
    seen = defaultdict(int)
    anagrams = 0
    for word in str_list:
        sig = gen_signature(word)
        seen[sig] += 1
        anagrams += seen[sig] - 1
    return anagrams <= 18