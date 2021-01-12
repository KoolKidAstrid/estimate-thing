import pygame
import math

#   list of requested n values
steplist = [10, 50, 100, 200, 1000, 10000]

#   function
def f(xfunc):
    yfunc = math.sqrt(4 - (xfunc * xfunc))
    return yfunc


#   create printout file
save = open("printout.txt", "w+")
save.write("printout")

#   setup window
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Area Estimation")
pygame.init()
running = True

#   will calculate the upper and lower rectangles for each value of the steplist[] we mentioned earlier
for steps in steplist:
    above = []
    below = []
    stepsize = 2/steps

#   figures out where the above and below rectangles reach the circle, marked a and b
    for a in range(steps):
        x = a*stepsize
        y = f(x)
        above.append((x, y))
    for b in range(steps):
        x = (b+1)*stepsize
        y = f(x)
        below.append((x, y))

#   draw background and curve
    pygame.draw.rect(screen, (255, 255, 255), ((0, 0), (800, 800)))
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 800), 30)
    pygame.draw.line(screen, (0, 0, 0), (0, 800), (800, 800), 30)
    pygame.draw.circle(screen, (255, 0, 0), (0, 800), 800, 5)

#   some variable stuff for later
    mult = height/2
    chunk = height/steps
    atotal = 0
    btotal = 0

#   draws above and below rectangles, and adds their x and y values to the atotal and btotal values
    for a in above:
        x = a[0]
        y = a[1]
        pygame.draw.rect(screen, (0, 255, 0), ((x*mult-1, -1), (chunk+1, (2-y)*mult+1)))
        pygame.display.update()
        pygame.time.delay(int(1000/steps))
        atotal += y*stepsize
    for b in below:
        x = b[0]
        y = b[1]
        pygame.draw.rect(screen, (0, 0, 255), (((x-stepsize)*mult-1, height-(mult*y)-1), (chunk+1, mult*y+1)))
        pygame.display.update()
        pygame.time.delay(int(1000/steps))
        btotal += y*stepsize

#   save graph as screenshot, and save output to file
    image = "screenshots\\graph-" + str(steps) + ".png"
    pygame.image.save(screen, str(image))
    save.write("\n" + str(steps) + " boxes:\n   above boxes: " + str(atotal) + "\n   below boxes: " + str(btotal))

pygame.draw.rect(screen, (255, 255, 255), ((0, 0), (800, 800)))
pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 800), 30)
pygame.draw.line(screen, (0, 0, 0), (0, 800), (800, 800), 30)
pygame.draw.circle(screen, (255, 0, 0), (0, 800), 800, 5)
pygame.display.update()

save.close()

font = pygame.font.SysFont(None, 30)
img = font.render('done!', True, (0, 0, 0))
screen.blit(img, (350, 375))
pygame.display.update()

# waits until you quit the program
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(100)

pygame.quit()
