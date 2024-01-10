import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():
    try:
        recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    koch_turtle = turtle.Turtle()
    koch_turtle.speed(2)

    koch_turtle.penup()
    koch_turtle.goto(-150, 90)
    koch_turtle.pendown()

    for _ in range(3):
        koch_snowflake(koch_turtle, recursion_level, 300)
        koch_turtle.right(120)

    window.exitonclick()

if __name__ == "__main__":
    main()
