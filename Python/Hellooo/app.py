# 输入输出
print('Hello World!')

name = input('What is your name?')
favorite_color = input('What is your favoriye color?')
print(name + ' like ' + favorite_color)

# 切片操作
course = 'Python'
print(course[1:-1])

# 字符串格式化输出
first = 'Pan'
last = 'Colen'
message = first + '[' + last + '] is good'
msg = f'{first}[{last}] is ohhhhhhhhhhh'
print(message)
print(msg.replace('Pan', 'Adobe'))

# 数组，循环
for item in ['Mosh', 'John', 'Sarah']:
    print(item)

numbers = [5, 2, 5, 3]
for x_count in numbers:
    print("x" * x_count)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)


# 方法和字典对象
def replace_emoji(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😂"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


xx = input(">")
print(replace_emoji(xx))

# 异常处理
try:
    age = int(input('Age:'))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid value')


# 类
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 20)
print(point1.x)
point1.draw()

