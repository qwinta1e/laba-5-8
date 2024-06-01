import math
def count_ways(step):
    if step == 0 or step == 1:
        return 1
    
    dp = [0] * (step + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, step + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[step]

#доделать кратность
def max_substring(word):
    max_count = 0
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            substring = word[i:j]
            count = word.count(substring)
            if count > max_count:
                max_count = count
    return max_count

def all_paths(n, m):
    dp = [[0] * m for _ in range(n)]
    
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    
    return dp[n-1][m-1]

def levenshtein_alg(string1, string2):
    m, n = len(string1), len(string2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]
if __name__ == "__main__":
    x = input()
    match x:
        case "1":    
            step = int(input())
            count = count_ways(step)
            print(f"Количество различных способов подняться на {step} ступеней: {count}")
        case "2":
            string = str(input())
            res = max_substring(string)
            print(f"Максимальная кратность подстроки в запросе '{string}': {res}")
        case "3":
            n = int(input("Введите n: "))
            m = int(input("Введите m: "))
            num_paths = all_paths(n, m)
            print(f"Количество возможных маршрутов: {num_paths}")
        case "4":
            string1 = str(input("Введите преобразуемую строку: "))
            string2 = str(input("Введите преобразованную строку: "))
            distance = levenshtein_alg(string1, string2)
            print(f"Минимальное количество операций для превращения '{string1}' в '{string2}': {distance}")