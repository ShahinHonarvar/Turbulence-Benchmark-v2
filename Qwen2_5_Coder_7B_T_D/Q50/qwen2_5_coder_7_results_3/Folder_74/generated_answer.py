def if_contains_anagrams(arr):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if len(arr[i]) >= 3 and len(arr[j]) >= 3 and is_anagram(arr[i], arr[j]):
                anagram_pairs += 1
    return anagram_pairs >= 17