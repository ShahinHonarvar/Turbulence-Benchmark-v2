from collections import defaultdict

def if_contains_anagrams(str_list):

    def build_signature(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    signatures = defaultdict(int)
    for word in str_list:
        word_len = len(word)
        if word_len >= 3:
            signature = build_signature(word)
            signatures[signature] += 1
    anagram_count = sum((count * (count - 1) // 2 for count in signatures.values()))
    return anagram_count <= 55