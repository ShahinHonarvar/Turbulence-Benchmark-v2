def if_contains_anagrams(arr):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if len(arr[i]) >= 3 and len(arr[j]) >= 3 and (normalize(arr[i]) == normalize(arr[j])):
                anagram_pairs.add((normalize(arr[i]), normalize(arr[j])))
    return len(anagram_pairs) <= 19