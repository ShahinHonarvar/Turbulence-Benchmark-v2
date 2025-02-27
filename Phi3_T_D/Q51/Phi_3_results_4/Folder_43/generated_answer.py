from collections import defaultdict

def if_contains_anagrams(words):

    def get_signature(s):
        return ''.join(sorted(s.lower()))
    signature_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            signature = get_signature(word)
            signature_count[signature] += 1
    return sum((count >= 2 for count in signature_count.values())) <= 3