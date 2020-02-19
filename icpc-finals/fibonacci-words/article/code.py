# Nota: Este codigo solo cumple función ilustrativa
# en el artículo, para ver una versión
# completamente funcional, vea la carpeta solutions


def kmp(text, pattern):
    pass


def fibonacci_words(n, p):
    dp = [0]*(n+2)

    dp[0] = 1 if p == '0' else 0
    dp[1] = 1 if p == '1' else 0

    prefix, suffix = ['0', '1'], ['0', '1']

    m = len(p) - 1

    for i in range(2, n+1):
        center = (suffix[i-1][-m:] + prefix[i-2][:m]
                  if m > 0 else '')

        dp[i] = dp[i-1] + dp[i-2] + kmp(center, p)

        if len(prefix[i-1]) >= len(p) - 1:
            prefix.append(prefix[i-1])
        else:
            prefix.append(prefix[i-1] + prefix[i-2])

        if len(suffix[i-2]) >= len(p) - 1:
            suffix.append(suffix[i-2])
        else:
            suffix.append(suffix[i-1] + suffix[i-2])

    return dp[n]
