from questions_data import questions as q, prize_list as p

cnt = 0

for i in q:
    print(i[0])
    print(f"a. {i[1]}")
    print(f"b. {i[2]}")
    print(f"a. {i[3]}")

    inp = int(input("Enter Your Answer. 1 for a, 2 for b, 3 for c\n"))

    if (inp == i[4]):
        print("Correct Answer\n")
    else:
        print(f"Incorrect Answer, the correct answer was {i[i[4]]}")
        print("Better Luck Next Time\n")
        break
    print(f"You Won {p[cnt]}\n")
    cnt += 1
