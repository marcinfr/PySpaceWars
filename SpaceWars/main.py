import screen
import background
import events

screen = screen.Screen(1024, 768)
background = background.Background(screen)
events = events.Events()
running = True

while not events.quit:
    events.collect()
    background.move()
    background.draw()
    screen.display()
    if events.is_key_pressed(events.escKey):
         print("esc")
    if events.is_key_pressed("a"):
        print("a")
