from inputs import inputGrade, inputName
from functions import filterStudents


def main():
    students = []
    
    for i in range(1, 4):
        students.append(
            {
                'name': inputName('Digite o nome do aluno [%d]: ' % (i)),
                'grades': [inputGrade('Digite a nota [%d]: ' % (i)) for i in range(1, 5)]
            }
        )

    print(students)

    # updated 14/04 - worked!
    filteredStudents = filterStudents(lambda x: sum(x['grades']) / len(x['grades']) >= 6, students)
    print(filteredStudents)
    
main()