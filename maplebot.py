from keys import KeyLocations
import pyautogui
import os
import time
import random

"""
Author: Jonathon Carlyon (JonathonCarlyon@gmail.com)

MapleChar is a base class containing the essential 
abilities and checks most classes will need.
"""

class MapleChar(KeyLocations):
    def __init__(self):
        super().__init__()
        self.start_time = time.time()
        self.direction = 'right'
        self.health_img = os.path.abspath('assets\health.png')
        self.potion_count = 0
        
    #Character movement
    def run(self, direction, duration):
        """Character runs for duration heading toward direction"""
        if direction is 'right':
            pyautogui.mouseDown(self.RIGHT)
            self.direction = 'right'
        elif direction is 'left':
            pyautogui.mouseDown(self.LEFT)
            self.direction = 'left'
        elif direction is 'opposite':
            if self.direction is 'left':
                self.run('right', duration)
            elif self.direction is 'right':
                self.run('left', duration)
        elif direction is 'forward':
            self.run(self.direction, duration)
        time.sleep(duration)
        pyautogui.mouseUp()
        
    def turn(self):
        """Turn Character opposite direction"""
        if self.direction is 'right':
            self.run('left', 0.1)
        elif self.direction is 'left':
            self.run('right', 0.1)
        
    def loot(self):
        """Auto loots the area"""
        loot_directions = [self.LEFT, self.RIGHT]
        for direction in loot_directions:
            for x in range(5):
                pyautogui.mouseDown(direction)
                time.sleep(0.1)
                pyautogui.mouseUp()
                pyautogui.mouseDown(self.Z)
                time.sleep(1)
                pyautogui.mouseUp()
            if direction is self.LEFT:
                self.run('right', 1)
            elif direction is self.RIGHT:
                self.run('left', 1)
                
    def loot_corner(self, direction):
        """Auto loots corner of area which you are facing"""
        for x in range(2):
            pyautogui.mouseDown(self.Z)
            time.sleep(0.5)
            pyautogui.mouseUp()
            if direction is 'left':
                pyautogui.mouseDown(self.LEFT)
            elif direction is 'right':
                pyautogui.mouseDown(self.RIGHT)
            time.sleep(0.2)
            pyautogui.mouseUp()
            pyautogui.mouseDown(self.Z)
            time.sleep(2.5)
            pyautogui.mouseUp()
            self.heal()
        self.turn()
        pyautogui.mouseDown(self.Z)
        time.sleep(2)
        pyautogui.mouseUp()
        
    def loot_ahead(self):
        """Walk short distance ahead looting on the way"""
        pyautogui.mouseDown(self.Z)
        time.sleep(1)
        for x in range(3):
            pyautogui.mouseDown(self.Z)
            time.sleep(random.uniform(0.5, 1.3))
            self.run('forward', random.uniform(0.1, 0.5))
        pyautogui.mouseUp()
        
    def heal(self):
        potions_to_chug = 2
        logging.info('Checking health.')
        while not pyautogui.locateOnScreen(self.health_img):
            for x in range(potions_to_chug):
                pyautogui.click(self.T)
                time.sleep(0.3)
            self.potion_count += potions_to_chug
            logging.info('Used %d potions.', self.potion_count)
        logging.info('Done healing.')
    #add def mana
    