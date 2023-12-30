import turtle

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

def plot_list_into_turtle() -> None:
    turtle.title("Collatz Conjecture")
    turtle.bgcolor("#1f1f1f")
    s = turtle.getscreen()

    #TODO: Get starting number through tkinter GUI with more info on the conjecture / problem
    #      and maybe a clickable hyperlink to the Wikipedia.
    #      Only start turtle plotting when the input got checked.
    starting_number_string = s.textinput(
        "Collatz Conjecture Input", 
        "Please input a starting number for the conjecture. \n" +
        "The number should be an integer between 1 and 10^15.")
    
    try:
        starting_number = int(starting_number_string)
    except:
        raise ValueError("Input must be an integer between 1 and 10^15.")
    
    coordinates = collatz_conjecture(starting_number)
    s.setworldcoordinates(0, 0, len(coordinates), 1.1 * max(coordinates))
    t = turtle.getturtle()
    t.hideturtle()
    t.up()

    for i in range(len(coordinates)):
        t.pencolor("#9cdcfe")
        t.goto(i, coordinates[i])
        t.dot(5)
        t.pencolor("white")
        t.write(arg=coordinates[i], align="center")
        t.down()

    s.mainloop()

plot_list_into_turtle()