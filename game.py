import random
import turtle
def gamewin(computer,you):
    if computer==you:
        return None
    elif computer==("Snake"):
        if you==("Water"):
            return False
        elif you==("Gun"):
            return True
    elif computer==("Water"):
        if you==("Gun"):
            return False
        elif you==("Snake"):
            return True
    elif computer==("Gun"):
        if you==("Snake"):
            return False
        elif you==("Water"):
            return True
    # else:
    #      return 1
            
print("Computer turn: Snake Water Gun")
randno=random.randint(1,3)
if randno==1:
    computer="Snake"
elif randno==2:
    computer="Water"
elif randno==3:
    computer="Gun"


you=input("Your turn: Snake Water  Gun:  ")
a=gamewin(computer,you)

print(f"computer chose= {computer}")
print(f"you chose= {you}")

if a==None:
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
    t.write(''' 🤜🤛
 🤝''', font=("Arial", 90))
    turtle.done()

    
elif a==True:
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


elif a==False:
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
    t.write(''' 😭😭
💔💔''', font=("Arial", 90))
    turtle.done()
    




    
