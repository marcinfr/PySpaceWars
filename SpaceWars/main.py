import screen
import background
import events
import menu

screen = screen.Screen(1024, 768)
events = events.Events()
background = background.Background(screen)
menu = menu.Menu(screen, events)
running = True

while not events.quit:
    events.collect()

    if not menu.display:
        background.move()

    background.draw()
    screen.display()
    if events.is_key_just_pressed(events.escKey):
        menu.display = not menu.display

    if events.is_key_pressed("a"):
        print("a")
