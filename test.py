import pygame
# 参考文档 https://www.pygame.org/docs/ref/joystick.html?highlight=gamepad

import json

with open("config.json",'r') as f:
    config  = json.load(f)
    print(config)

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
print(joystick_count)
stick = pygame.joystick.Joystick(0)
stick.init()

from pynput.keyboard import Key, Controller
keyboard = Controller()

# clock = pygame.time.Clock()
done = False
while not done:
    try:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button >= len(config['button']):
                    continue
                k = config['button'][event.button]
                if k != "":
                    keyboard.press(k)
            if event.type == pygame.JOYBUTTONUP:
                if event.button >= len(config['button']):
                    continue
                k = config['button'][event.button]
                if k != "":
                    keyboard.release(k)
            if event.type == pygame.JOYAXISMOTION:
                if event.axis >= len(config['axis']):
                    continue
                if event.value < -0.3:
                    k = config['axis'][event.axis][0]
                    k1 = config['axis'][event.axis][1]
                    keyboard.press(k)
                    keyboard.release(k1)
                if event.value > 0.3:
                    k = config['axis'][event.axis][1]
                    k1 = config['axis'][event.axis][0]
                    keyboard.press(k)
                    keyboard.release(k1)
                if event.value == 0:
                    for k in config['axis'][event.axis]:
                        keyboard.release(k)
                
                
    except KeyboardInterrupt:
        done = True
pygame.quit()

