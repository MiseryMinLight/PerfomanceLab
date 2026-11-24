import sys

if len(sys.argv) != 2:
    print("Укажи путь к файлу с массивом")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r", encoding="utf-8") as file:
    numbers = list(map(int, file.read().split()))

numbers.sort()

middle = len(numbers) // 2
median = numbers[middle]

moves = 0

for number in numbers:
    moves += abs(number - median)

if moves <= 20:
    print(moves)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному чилсу")

