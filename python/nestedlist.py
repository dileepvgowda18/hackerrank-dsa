if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest score
    scores = sorted(set(score for name, score in students))
    second_lowest = scores[1]

    # Get and sort the names with the second lowest score
    names = sorted(name for name, score in students if score == second_lowest)

    # Print each name
    for name in names:
        print(name)