def gradingStudents(grades):
    # Write your code here
    for i in range(0, len(grades)):
        s1 = int(grades[i]) + 1
        s2 = int(grades[i]) + 2
        # print(s1)

        if (s1 >= 40):

            if (s1 % 5 == 0):
                grades[i] = s1
                print(grades[i])

            elif (s2 % 5 == 0):
                grades[i] = s2
                print(grades[i])
            else:
                print(grades[i])

        elif (s2 >= 40):

            if (s2 % 5 == 0):
                grades[i] = s2
                print(grades[i])

            else:
                print(grades[i])

        else:
            print(grades[i])


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    # result = gradingStudents(grades)
    gradingStudents(grades)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
