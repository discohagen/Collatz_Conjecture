import turtle
import tkinter

def collatz_conjecture(number: int) -> [int]:
    if number <= 1:
        raise ValueError("Input must be a positive integer greater than one.")
    if number >= 10 ** 15:
        raise ValueError("Input should be less than 10^15.")
    
    conjecture = [number]
    while number > 1:
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = (3 * number) + 1
        conjecture.append(number)

    return conjecture

def plot_list_into_turtle(coordinates: [int], title = "", showNumbers = True) -> None:
    turtle.title(title)
    turtle.bgcolor("#1f1f1f")
    s = turtle.getscreen()
    s.setworldcoordinates(0, 0, len(coordinates), 1.1 * max(coordinates))
    t = turtle.getturtle()
    t.hideturtle()
    t.up()

    for i in range(len(coordinates)):
        t.pencolor("#9cdcfe")
        t.goto(i, coordinates[i])
        t.dot(5)
        if (showNumbers):
            t.pencolor("white")
            t.write(arg=coordinates[i], align="center")
        t.down()

def plot_collatz_conjecture() -> None:
    window = tkinter.Tk()
    window.title("Collatz Conjecture Input")
    tkinter.Label(window, text=
        "Please input a starting number for the conjecture. \n" +
        "The number should be an integer between 1 and 10^15.").pack()
    input = tkinter.Entry(window)
    input.pack()
    
    def on_click() -> None:
        try:
            starting_number = int(input.get())
        except:
            raise ValueError("Input must be an integer between 1 and 10^15.")
        window.destroy()
        plot_list_into_turtle(collatz_conjecture(starting_number), "Collatz Conjecture")
        return 
    
    tkinter.Button(window, text="OK", command=on_click).pack()

    window.mainloop()

plot_collatz_conjecture()