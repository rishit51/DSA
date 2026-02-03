from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        ans = 0
        center = False

        for w in list(cnt.keys()):
            rev = w[::-1]

            if w == rev:
                pairs = cnt[w] // 2
                ans += pairs * 4
                cnt[w] -= pairs * 2
                if cnt[w] > 0:
                    center = True
            elif w < rev:   # avoid double counting
                pairs = min(cnt[w], cnt[rev])
                ans += pairs * 4

        if center:
            ans += 2

        return ans

