import random
import math
import re
from unittest import result
a1 = i1 = 5.4
i2 = int(a1 * i1)
i3 = math.ceil(a1 * i1)
a2 = a1 ** i1
# print(i1, i2, i3, a1, a2)


def HowManyNumber():
    number = int(input('please supply the number of items to average:'))
    return number

# def SumNumbers(num):
#  total = 0
#  for n in range(num):


# print(range(70, 1, 100))
values = []


# def generateRange(start, stop):
#     for n in range(start, stop):
#         values.append(n)
#     return values


# generateRange(40, 45)
# set 3: question 6
gradeA = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
          85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
gradeB = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
gradeC = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
gradeD = [45, 46, 47, 48, 49]
gradeE = [40, 41, 42, 43, 44]


def gradeScore(score):
    if score < 40:
        print('The grade is F')
    elif score in gradeA:
        print('The grade is A')
    elif score in gradeB:
        print('The grade is B')
    elif score in gradeC:
        print('The grade is C')
    elif score in gradeD:
        print('The grade is D')
    elif score in gradeE:
        print('The grade is E')


# gradeScore(40)

# set 3: question 12

def baterial_productivity():
    intervalA = 60
    intervalB = 90
    hours_to_mins = 180
    total_hours = 1440
    loop_length = math.floor(1440/180)

    for i in range(loop_length):
        temp_mins = math.floor(hours_to_mins * (i + 1))
        temp_a_produce = math.floor(temp_mins/intervalA)
        temp_b_produce = math.floor(temp_mins/intervalB)

        print('%d: [A: %s, B: %s] ' % (i, temp_a_produce, temp_b_produce))

        if temp_mins == total_hours:
            break

        i += 1


# baterial_productivity()


# set 3: question 15
def harmonic_mean(array):
    n = len(array)
    denominator_sum = 0

    for i in range(n):
        denominator_sum += (1/array[i])
        result = n/denominator_sum

    print(result)


# harmonic_mean([1, 2, 3, 4, 5])

# set 4: question 5
def tuple_to_string(tuple):
    result = "".join(tuple)
    print(result)


# tuple_to_string(('c', 's', 'c', '2', '0', '1'))

def get_third_and_fifth(tuple):
    print('third element: %s fifth element: %s ' % (tuple[2], tuple[4]))

# get_third_and_fifth(('c', 's', 'c', '2', '0', '1'))


def find_item_in_dictionary(dictionary, key):
    dic = dictionary
    key_value = dic.get(key)
    if key_value != None:
        print(key_value)
    else:
        print('key not found')

# print(values)


# find_item_in_dictionary({"first": 1, "second": 2}, "second")

# if 72 in values:
#     print("true")

def nums_and_squares_dic():
    nums = 15
    dic_result = {}
    for n in range(nums):
        dic_result[n+1] = (n+1)**2
    print(dic_result)


# nums_and_squares_dic()

cordinate = 4
photoshop = 6
coreldraw = 3
figma = 1
dell = 2
adobe = 7
getresponse = 5
email = 9
freelance = 8
programming = 10

opts = ('cordinate', 'photoshop', 'coreldraw', 'figma', 'dell', 'adobe', 'getresponse',
        'email', 'freelance', 'programming', '4', '6', '3', '1', '2', '7', '5', '9', '8', '10')

# user_input = input('enter field...')
# if user_input in opts:
#     print(user_input, 'is present')
# elif user_input not in opts:
#     print(user_input, 'not present')


def solving_for_yt():
    t = random.randint(-9, 91)
    y = 0
    if t < 0:
        y = -(3 * t**2) + (3 * t) - 5
    elif t > 0:
        y = (3 * t**2) - (3 * t) - 5
    else:
        y = (3 * t**2) - (3 * t) + 5
    print(y)


solving_for_yt()


def swap(a, b):
    print('A = %d, B = %d' % (b, a))


# swap(2, 3)


def min6(array):
    for i in range(len(array)):
        temp = min(array)
    print(temp)


# min6([89, 3, 4, 5, 7])


def check_triangle(x, y, z):
    if (x + y <= z) or (x + z <= y) or (y + z <= x):
        return print('not a valid triangle')
    else:
        return print('valid triangle')


check_triangle(2, 3, 8)


class Triangle:
    def proper_triangle(self):
        print('proper triangle')

    def isoceles(self):
        print('isoceles triangle')


tri = Triangle()
tri.proper_triangle()