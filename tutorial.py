# def fib(n):
#     result = []
#     a, b = 0, 1
#     while b < n:
#         result.append(b)
#         a, b = b, a+b
#     return result

# fib(50)

k = 1

# 1


class A:
    def __init__(self, test):
        self.test = 0


def main():
    count = A(0)
    k = 0

    for i in range(0, 25):
        add(count, k)
    print("count.test is", count.test)
    print("k is ", k)


main()


# solution 2
class Student:
    def __init__(self, name, age, score1, score2, score3, score4, score5, score6, unit1, unit2, unit3, unit4, unit5, unit6):
        self.name = name
        self.age = age
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.score4 = score4
        self.score5 = score5
        self.score6 = score6
        self.unit1 = unit1
        self.unit2 = unit2
        self.unit3 = unit3
        self.unit4 = unit4
        self.unit5 = unit5
        self.unit6 = unit6

    def score_grade(self, score):
        if score > 69:
            return 'A'
        elif score < 40:
            return 'F'
        elif 59 < score < 70:
            return 'B'
        elif 49 < score < 60:
            return 'C'
        elif 44 < score < 50:
            return 'D'
        elif 39 < score < 45:
            return 'E'
        else:
            return 'please ensure score provided is a valid integer'

    def score_point(self, score):
        if score > 69:
            return 5
        elif score < 40:
            return 0
        elif 59 < score < 70:
            return 4
        elif 49 < score < 60:
            return 3
        elif 44 < score < 50:
            return 2
        elif 39 < score < 45:
            return 1
        else:
            return 'please ensure score provided is a valid integer'

    def student_gpa(self):
        score1 = self.score_point(self.score1) * self.unit1
        score2 = self.score_point(self.score2) * self.unit2
        score3 = self.score_point(self.score3) * self.unit3
        score4 = self.score_point(self.score4) * self.unit4
        score5 = self.score_point(self.score5) * self.unit5
        score6 = self.score_point(self.score6) * self.unit6

        score1 = self.score_point(self.score1) * self.unit1
        result = (score1 + score2 + score3 + score3 + score4 + score5 + score6) / \
            (self.unit1 + self.unit2 + self.unit3 +
             self.unit4 + self.unit5 + self.unit6)
        return result

    def display_result(self):
        print("student's  name is ", self.name,
              "the student's age ", self.age)
        print("the grade for course1 is ", self.score_grade(self.score1),
              'and grade point is ', self.score_point(self.score1))
        print("the grade for course2 is ", self.score_grade(self.score2),
              'and grade point is ', self.score_point(self.score2))
        print("the grade for course3 is ", self.score_grade(self.score3),
              'and grade point is ', self.score_point(self.score3))
        print("the grade for course4 is ", self.score_grade(self.score4),
              'and grade point is ', self.score_point(self.score4))
        print("the grade for course5 is ", self.score_grade(self.score5),
              'and grade point is ', self.score_point(self.score5))
        print("the grade for course6 is ", self.score_grade(self.score6),
              'and grade point is ', self.score_point(self.score6))
        print("student's gpa is ", self.student_gpa())


new_student = Student('tolami', 30, 80, 60, 70, 49, 60, 51, 2, 2, 2, 2, 2, 2)

new_student.display_result()
