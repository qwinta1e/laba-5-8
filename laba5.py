import math
import random

# Нахождение наибольшей общей префиксной подстроки.
# O(nlogm), n - кол-во строк, m - длина самой длинной
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    min_len = min(len(s) for s in strs)
    low, high = 0, min_len - 1
    
    while low <= high:
        mid = (low + high) // 2
        prefix = strs[0][:mid + 1]
        if all(s.startswith(prefix) for s in strs):
            low = mid + 1
        else:
            high = mid - 1
    
    return strs[0][:(low + high) // 2 + 1]

# Найти удалённое число
# O(n)
def findMissingNumber(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Перевод из римской в арабскую
# O(n), n - длина входной строки
def romanToInteger(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for char in s:
        curr_value = roman_map[char]
        result += curr_value
        if curr_value > prev_value:
            result -= 2 * prev_value
        prev_value = curr_value
    
    return result

# Определение анаграмм
# O(nm), n - кол-во слов, m - макс длина слова
def areAnagrams(*words):
    def count_letters(word):
        letter_count = {}
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        return letter_count

    if len(words) < 2:
        return False

    first_word_count = count_letters(words[0].lower())
    for word in words[1:]:
        if len(word) != len(words[0]):
            return False
        word_count = count_letters(word.lower())
        if word_count != first_word_count:
            return False
    return True

# Поиск Фибоначчи по порядковому номеру
# O(1)
def fibonacciNumber(n):
    if n < 1:
        return "Порядковый номер должен быть положительным"
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (1 - phi)**n) / math.sqrt(5))

if __name__ == "__main__":
# Выбор программы
    print("1. Нахождение наибольшей общей префиксной подстроки")
    print("2. Найти удалённое число")
    print("3. Перевод из римской в арабскую")
    print("4. Определение анаграмм")
    print("5. Поиск Фибоначчи по порядковому номеру")

    x = str(input("Выберите программу...  "))

    match x:
        case "1":
            strs = ["Home", "Homie", "Hoe", "Homrad"]
            print(longestCommonPrefix(strs))
        case "2":
            n = 10
            nums = [x for x in range(1,n+1)]
            print(nums)
            nums.remove(random.randint(1,n))
            print(nums)
            random.shuffle(nums)
            print(findMissingNumber(nums, n))
        case "3":
            s = input("Введите число в римской системе: ")
            print(romanToInteger(s))
        case "4":
            print("Вводите слова (Через пробел).")
            buf = str(input()).split()
            print(areAnagrams(*buf))
        case "5":
            fib=int(input("Введите порядковый номер числа фибоначчи: "))
            print(fibonacciNumber(fib))