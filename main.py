import sys
import PIL.ImageGrab as IG
from PIL import Image
import os
import csv
import cv2
import multiprocessing

import mouse, time
from pynput.keyboard import Listener, KeyCode

cookie_pix = [(217,190,94),(140,148,87),(140,148,87),(115,74,43),(92,57,34),(68,41,25),(115,74,43),(115,74,43),(115,74,43),(115,74,43)]
start_x = -3840
stop_x = -1900
start_y = 420
stop_y = 1360
def main():
    processes = []
    p = multiprocessing.Process(target=run_clicks)
    p.start()
    #processes.append(p)
    q = multiprocessing.Process(target=check_cookie)
    q.start()
    #processes.append(q)
    p.join()
    q.join()





def run_clicks():
    active = True
    while active:
        mouse.move(-3600, 800)
        start_mouse = mouse.get_position()
        for i in range(10):
            time.sleep(.001)
            mouse.click()
            end_mouse = mouse.get_position()
        if end_mouse != start_mouse:
            active = False

def check_cookie():

    #cookie = Cookie_Box(x,y)
    #box = (cookie.start_x,cookie.start_y,cookie.end_x, cookie.end_y)

    active = True
    while active:
        box = (start_x,start_y,stop_x,stop_y)
        im = IG.grab(box, include_layered_windows=False, all_screens=True)
        im.save(os.getcwd() + "\\cookie.png", 'PNG')
        cookie_im = Image.open("cookie.png", 'r')
        pix_list = list(cookie_im.getdata())
        n = 1940
        two_dim_pix = [pix_list[i * n:(i+1)*n] for i in range((len(pix_list)+ n - 1)//n)]

        y_index = 1
        for row in two_dim_pix:

            x_index = contains(row, cookie_pix)
            if x_index != -1:
                print("Cookie found!")

                get_cookie(x_index,y_index)
            y_index += 1
                #mouse.move(start_mouse[0], start_mouse[1])
            start_mouse = mouse.get_position()
        print("No cookie.")


        end_mouse = mouse.get_position()
        if end_mouse != start_mouse:
            print("Exiting.")
            active = False

def contains(big_list, small_list):
    for i in range(len(big_list)):
        if big_list[i:i+len(small_list)] == small_list:
            return i
    return -1


def get_cookie(x,y):
    print(x, y)
    mouse.move(x-3840, y + 420)
    print(mouse.get_position())
    mouse.click()
    mouse.move(-3600, 800)


'''
    for i in range(80):
        mouse.move(-2000, 1150 - i*5)
        time.sleep(.001)
        mouse.click()
        mouse.move(-3600, 800)
        time.sleep(.001)
        mouse.click()
'''
class Cookie_Box:
    def __init__(self,x,y):
        self.start_x = x
        self.end_x = x + 95
        self.start_y = y
        self.end_y = y + 95
        self.center_x = self.end_x - 47
        self.center_y = self.end_y - 47


if __name__ == '__main__':
    main()