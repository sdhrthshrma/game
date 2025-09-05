import random
import turtle

def gamewin(computer, you):
    if computer == you:
        return None
    elif computer == "Snake":
        return you == "Gun"
    elif computer == "Water":
        return you == "Snake"
    elif computer == "Gun":
        return you == "Water"

while True:
    print("\nComputer turn: Snake Water Gun")
    randno = random.randint(1, 3)
    if randno == 1:
        computer = "Snake"
    elif randno == 2:
        computer = "Water"
    else:
        computer = "Gun"

    you = input("Your turn: Snake Water Gun (or type 'exit' to quit): ").capitalize()

    if you.lower() == "exit":
        print("Game exited. Thanks for playing!")
        break

    if you not in ["Snake", "Water", "Gun"]:
        print("Invalid choice! Please enter Snake, Water, or Gun.")
        continue

    a = gamewin(computer, you)

    print(f"\nComputer chose: {computer}")
    print(f"You chose: {you}")

    if a is None:
        print('''Tie , Maybe aapne kuch glt chose kra ho 
************   **********     *       *           **********    *********   *********   ***********   *       *
     *         *        *     *       *           *        *    *           *       *        *        * *     *
     *         *********      *********           **********    *           *********        *        *   *   *
     *         *   *                  *           *        *    *  ******   *       *        *        *    *  *
     *         *     *                *           *        *    *       *   *       *        *        *     * *
     *         *        *     *********           *        *    *********   *       *   ***********   *       *
                ''')
        t = turtle.Turtle()
        turtle.bgcolor("skyblue")
        t.penup()
        t.goto(-120, 3)
        t.color("red")
        t.pendown()
        t.write(''' 🤜🤛\n 🤝''', font=("Arial", 90))
        turtle.done()

    elif a is True:
        print('''*               *          * * * * * * * * *   *         *
*               *                 *            * *       *          *            
*        *      *                 *            *   *     *         ***        
*     *    *    *                 *            *     *   *        *****             
*  *         *  *                 *            *       * *       *******      
*               *          * * * * * * * * *   *         *          |        
                                                                    |
          ''')
        t = turtle.Turtle()
        turtle.bgcolor("skyblue")
        t.penup()
        t.goto(-140, -90)
        t.color("red")
        t.pendown()
        t.write(''' 
 🎊🎊
🏆
🎉🎉''', font=("Arial", 90))
        turtle.done()

    else:
        print('''
*         ********  ********  ********
*         *      *   *        *
*         *      *     *      *****
*         *      *        *   *
********  ********  ********  ********
                                 ''')
        t = turtle.Turtle()
        turtle.bgcolor("skyblue")
        t.penup()
        t.goto(-120, 3)
        t.color("red")
        t.pendown()
        t.write(''' 😭😭\n💔💔''', font=("Arial", 90))
        turtle.done()

