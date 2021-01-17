class Garden:
    __students = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry",
    ]

    __plants = {
        "C": "Clover",
        "G": "Grass",
        "R": "Radishes",
        "V": "Violets",
    }

    def __init__(self, diagram, students=None):
        if students is None:
            students = self.__students

        students = sorted(students)
        rows = diagram.splitlines()
        __students_plants = []

        for index, name in enumerate(students):
            __rows = [
                [self.__plants[row[index * 2]], self.__plants[row[(index * 2) + 1]]]
                for row in rows
                if (index * 2) + 1 < len(rows[0])
            ]
            __students_plants.append((name, [plant for row in __rows for plant in row]))

        self.students_plants = {
            student_name: plants for (student_name, plants) in __students_plants
        }

    def plants(self, student):
        return self.students_plants[student]
