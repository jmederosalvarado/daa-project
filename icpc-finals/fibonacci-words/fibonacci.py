def compute_prefix_func(pattern):
    prefix_func = [0]

    for i in range(1, len(pattern)):
        j = prefix_func[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix_func[j - 1]
        if pattern[j] == pattern[i]:
            prefix_func.append(j+1)
        else:
            prefix_func.append(j)

    return prefix_func


def kmp(text, pattern):
    prefix_func = compute_prefix_func(pattern)
    matches, j = 0, 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_func[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches += 1
            j = prefix_func[j - 1]

    return matches


def fibonacci_words(n, p):
    dp = [0]*(n+2)

    dp[0] = 1 if p == '0' else 0
    dp[1] = 1 if p == '1' else 0

    prefix = ['0', '1']
    suffix = ['0', '1']

    m = len(p) - 1

    for i in range(2, n+1):
        center = kmp(suffix[i-1][-m:] + prefix[i-2][:m], p) if m > 0 else 0
        dp[i] = dp[i-1] + dp[i-2] + center

        if len(prefix[i-1]) >= len(p) - 1:
            prefix.append(prefix[i-1])
        else:
            prefix.append(prefix[i-1] + prefix[i-2])

        if len(suffix[i-2]) >= len(p) - 1:
            suffix.append(suffix[i-2])
        else:
            suffix.append(suffix[i-1] + suffix[i-2])

    return dp[n]


def main():
    test_num = 1
    while True:
        try:
            n, p = int(input()), input()
        except EOFError:
            break
        print(f'Case {test_num}: {fibonacci_words(n, p)}')
        test_num += 1


if __name__ == "__main__":
    main()
