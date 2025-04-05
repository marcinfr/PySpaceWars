import screen
import background

screen = screen.Screen(1024, 768)
background = background.Background(screen)

while True:
    background.move()
    background.draw()
    screen.display()
