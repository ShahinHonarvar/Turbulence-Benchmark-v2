def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = 0
    for k in anagrams:
        n = len(anagrams[k])
        if n > 1:
            count += n * (n - 1) // 2
    return count >= 16