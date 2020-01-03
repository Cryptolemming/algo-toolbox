#python3
# max ad revenue

import sys

def max_ad_revenue(entries, profit_seq, avg_click_seq):
    result = 0
    profits = sorted(profit_seq)
    avg_clicks = sorted(avg_click_seq)

    for i in range(entries):
        result += profits[i] * avg_clicks[i]

    return result

if __name__ == "__main__":
    input = list(map(int, sys.stdin.read().split()))
    avg_click_seq_start = round(len(input)/2)
    print(max_ad_revenue(input[0], input[1:avg_click_seq_start], input[avg_click_seq_start:]))
