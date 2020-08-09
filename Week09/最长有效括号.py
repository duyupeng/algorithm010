class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        n = len(s)
        if not n:
            return 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == '(':
                dp[i] = 0
            else:
                if s[i - 1] == '(':
                    if i - 2 >= 0:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2

                else:

                    if i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                        if s[i - dp[i - 1] - 2]:
                            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                        else:
                            dp[i] = dp[i - 1] + 2
                    else:
                        dp[i] = 0

            # print('111',i)
            # print(dp[i])
            maxlen = max(maxlen, dp[i])
        return maxlen