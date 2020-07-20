# Coins Sum

```python
coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
dp = [[1] + [0]*target for i in range(len(coins)+1)]

for i in range(1, len(dp)):
    for j in range(1, target+1):
        dp[i][j] += dp[i-1][j]
        if (j-coins[i-1] >= 0):
            dp[i][j] += dp[i][j-coins[i-1]]

dp[len(coins)][target]
```

OUTPUT

```txt
73682
```

Recursive solution

```python
coins = [1, 2, 5, 10, 20, 50, 100, 200]

def count_ways(coins, coins_available, target_amt):
    if target_amt == 0:
        return 1
    if target_amt < 0 or coins_available <= 0:
        return 0

    # either don't use the coin, the target_amt remains same
    # or use the coin, so the target_amt reduces by coin amount
    return count_ways(coins, coins_available-1, target_amt) + count_ways(coins, coins_available, target_amt - coins[coins_available-1])

count_ways(coins, len(coins), 200)
```

