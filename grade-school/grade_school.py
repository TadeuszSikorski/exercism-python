from operator import itemgetter

class School:
    def __init__(self):
        self.students_roster = []

    def add_student(self, name, grade):
        self.students_roster.append((name, grade))

    def roster(self):
        self.students_roster.sort(key = itemgetter(0))
        self.students_roster.sort(key = itemgetter(1))

        return [student_roster[0] for student_roster in self.students_roster]

    def grade(self, grade_number):
        self.students_roster.sort(key = itemgetter(0))

        return [
            student_roster[0]
            for student_roster in self.students_roster
            if student_roster[1] == grade_number
        ]