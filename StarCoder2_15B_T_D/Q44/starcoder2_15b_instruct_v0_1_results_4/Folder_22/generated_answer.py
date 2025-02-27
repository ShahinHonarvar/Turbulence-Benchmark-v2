def composite_nums_between_indices(nums):
    prime = [True] * (max(nums) + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(max(nums) ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, max(nums) + 1, i):
                prime[j] = False
    composite = set()
    for i, num in enumerate(nums):
        if not prime[num] and 50 <= i <= 200:
            composite.add(num)
    return composite