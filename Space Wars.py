
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
matrix_of_asteroids=[]
matrix_of_rows=[]
Time = 0
score = 0
is_it_over = True
position_of_spaceship = 0
if x ==0:
    print("YOU WON!")
for counter_row in range(x):
    for counter_column in range(y):
        matrix_of_rows.append("*")
    matrix_of_asteroids.append(matrix_of_rows.copy())
    matrix_of_rows.clear()
for i in range(g):
        for m in range(y):
            matrix_of_rows.append(" ")
        matrix_of_asteroids.append(matrix_of_rows.copy())
        matrix_of_rows.clear()
if y%2 ==0:
    position_of_spaceship = int((y/2)-1)
    for k in range(position_of_spaceship):
        matrix_of_rows.append(" ")
    matrix_of_rows.append("@")
    for o in range(y-len(matrix_of_rows)):
        matrix_of_rows.append(" ")
    matrix_of_asteroids.append(matrix_of_rows.copy())
    matrix_of_rows.clear()
else:
    position_of_spaceship = int(((y-1)/2))
    for k in range(position_of_spaceship):
        matrix_of_rows.append(" ")
    matrix_of_rows.append("@")
    matrix_of_rows = matrix_of_rows + matrix_of_rows[:len(matrix_of_rows) - 1]
    matrix_of_asteroids.append(matrix_of_rows.copy())
    matrix_of_rows.clear()
for i in range(x + g + 1):
    for n in range(y):
        print(matrix_of_asteroids[i][n], end="")
    print("")
print("-" * 72)
if x ==0:
    print("YOUR SCORE:",score)
#Printing the first Panel of the Game
while x !=0:
    is_it_over = False
    did_it_end = True
    command = input("Choose your action!\n")
    command = command.lower()
    if command == "exit":
        will_print = True
        is_it_over = True
    elif command == "left":
        Time += 1
        if position_of_spaceship == 0:
            will_print = True
        else:
           matrix_of_asteroids[x+g][position_of_spaceship]=" "
           position_of_spaceship -= 1
           matrix_of_asteroids[x+g][position_of_spaceship]="@"
           will_print = True
    elif command =="right":
        Time += 1
        if position_of_spaceship == y-1:
            will_print = True
        else:
          matrix_of_asteroids[x+g][position_of_spaceship]=" "
          position_of_spaceship += 1
          matrix_of_asteroids[x+g][position_of_spaceship]="@"
          will_print = True
    elif command == "fire":
        Time += 1
        position_of_shoot_row = x+g-1
        is_hitting = False
        if matrix_of_asteroids[position_of_shoot_row][position_of_spaceship]=="*":
           matrix_of_asteroids[position_of_shoot_row][position_of_spaceship]=" "
           score +=1
           is_hitting = True
           will_print = True
        while is_hitting == False:
            matrix_of_asteroids[position_of_shoot_row][position_of_spaceship] = "|"
            for m in range(x + g + 1):
                for n in range(y):
                    print(matrix_of_asteroids[m][n], end="")
                print("")
            print("-" * 72)
            if matrix_of_asteroids[position_of_shoot_row-1][position_of_spaceship]=="*":
                matrix_of_asteroids[position_of_shoot_row - 1][position_of_spaceship] = " "
                matrix_of_asteroids[position_of_shoot_row][position_of_spaceship] = " "
                score +=1
                is_hitting=True
                will_print = True
            else:
                if position_of_shoot_row == 0:
                    matrix_of_asteroids[position_of_shoot_row][position_of_spaceship] = " "
                    will_print = True
                    is_hitting = True
                else:
                   matrix_of_asteroids[position_of_shoot_row][position_of_spaceship] = " "
                   position_of_shoot_row-=1
    else:
        Time += 1
        will_print = True
    if Time%5 == 0 and Time !=0:
        if "*" in matrix_of_asteroids[x+g-1]:
            print("GAME OVER")
            is_it_over=True
        else:
            matrix_of_asteroids.insert(0,[])
            for l in range(y):
                matrix_of_asteroids[0].append(" ")
            matrix_of_asteroids.pop(-2)
            will_print = True
    for j in matrix_of_asteroids:
        for i in j:
            if i== "*":
               did_it_end = False
               break
    if did_it_end == True:
        print("YOU WON!")
    if will_print == True:
        for i in range(x + g + 1):
            for n in range(y):
                print(matrix_of_asteroids[i][n], end="")
            print("")
        print("-" * 72)
        if is_it_over == True:
           print("YOUR SCORE:", score)
           break
        if command =="exit":
            print("YOUR SCORE:", score)
            break
        if did_it_end == True:
            print("YOUR SCORE:", score)
            break
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
