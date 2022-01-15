from inputs import inputGrade, inputName

def main():
    students = []
    
    for i in range(1, 3):
        students.append(
            {
                'name': inputName('Digite o nome do aluno [%d]: ' % (i)),
                'grades': [inputGrade('Digite a nota [%d]: ' % (i)) for i in range(1, 5)]
            }
        )

    print(students)
    print('updated')
    
main()