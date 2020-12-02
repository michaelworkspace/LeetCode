""" LeetCode 5454. Least Number of Unique Integers after K Removals

Given an array of integers A and an integer K, find the least number of unique integers
after removing exactly K elements.

Example 1:
Input: A = [5, 5, 3], K = 1
Output: 1
Explanation: Remove the single 4 then only the 5 is left.
"""


from typing import List


def foo(A: List[int], k) -> int:
    count = {}
    for num in A:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    sfreqs = sorted(count.values())
    ans = len(sfreqs)

    for freq in sfreqs:
        if k >= freq:
            k -= freq
            ans -= 1
    return ans


print(foo([4, 3, 1, 1, 3, 3, 2], 3))
