from maplebot import MapleChar
import pyautogui
import sys
import random
import time
import logging

"""
Author: Jonathon Carlyon (JonathonCarlyon@gmail.com)

DemonAvenger is a class containing unique abilities 
for the Maple Story class "Demon Avenger".  
"""


class DemonAvenger(MapleChar):
    """This class makes use of the specific skill
        set given to the Demon Avenger class, such
        as jumping up to platforms without ropes."""
    def __init__(self):
        super().__init__()
        logging.basicConfig(filename="maplebot.log", filemode='w', 
                            format='%(asctime)s.%(msecs).03d : %(message)s',  datefmt='%m/%d/%Y %I:%M:%S',
                            level = logging.INFO)
        logging.info('-' * 75)
        logging.info(' ' * 25 + 'Start of DemonAvenger Run')
        logging.info('-' * 75)
        self.buff_timer = -120
        self.scooby_bat_timer = -8
        self.nethershield_timer = -6
        self.gas_explosion_timer = -12
        self.level = 1
        
    def heal(self):
        """If red health bar not detected try R, if health still low 
        press T until it is.  This method overrides MapleChar.heal"""
        return
        potions_to_chug = 3
        logging.info("Checking health.")
        if not pyautogui.locateOnScreen(self.health_img):
            logging.info("Health low, attempting Overload Release")
            pyautogui.click(self.R)
            time.sleep(0.5)
            logging.info('Checking health again.')
            while not pyautogui.locateOnScreen(self.health_img):
                logging.info("Health didn't regenerate, drinking potions.")
                for x in range(potions_to_chug):
                    pyautogui.click(self.T)
                    time.sleep(0.3)
                self.potion_count += potions_to_chug
                logging.info("Used %d potions", self.potion_count)
            logging.info('Done healing.')
        else:
            logging.info('Health checked out')
    
    #Movement
    def level_navigation(self):
        """Keeps track of which vertical level character is on.
           After max_level is reached, player runs to side of map
           to return to bottom level. Level is then assigned 1 or 2"""
        self.max_levels = 4
        if self.level < self.max_levels:
            self.run('opposite', random.uniform(0.5, 2.25))
            self.up_a_level()
            self.turn()
            self.level += 1
        else:
            self.down_a_level()
            self.down_a_level()
            self.down_a_level()
            self.down_a_level()
            self.run('opposite', random.uniform(5.5, 7.5))
            self.turn()
            self.level = 0#random.randrange(0, 3)
        
    def up_a_level(self):
        """Presses ALT UP UP for a super vertical jump"""
        time.sleep(2)
        pyautogui.click(self.ALT)
        pyautogui.doubleClick(self.UP)
        pyautogui.mouseDown(self.UP) 
        time.sleep(2.5)
        pyautogui.mouseUp()

    def down_a_level(self):
        """Holds down and presses alt to jump down"""
        time.sleep(1)
        pyautogui.mouseDown(self.DOWN)
        time.sleep(2.5)
        pyautogui.click(self.ALT)
        pyautogui.mouseUp()
        #Todo: fly towards direction in case we got caught on ladder/rope?
        
    def across_platform(self):
        """Fly across to adjacent platform"""
        time.sleep(2)
        self.run('opposite', 1.2)
        self.turn()
        #Keep direction pressed down as we click alt
        if self.direction is 'left':
            pyautogui.mouseDown(self.LEFT)
        elif self.direction is 'right':
            pyautogui.mouseDown(self.RIGHT)
        time.sleep(1)
        pyautogui.click(self.ALT)
        pyautogui.mouseDown(self.ALT)
        time.sleep(1.5)
        pyautogui.mouseUp()

    #Abilities
    def buffs(self):
        """Applies buffs macroed to '2' and '3' keys"""
        if (time.time() - self.buff_timer) > 120:
            logging.info("Getting buff")
            self.buff_timer = time.time()
            pyautogui.click(self.TWO)
            time.sleep(3)
            pyautogui.click(self.THREE)
            time.sleep(3)
                
    def debuff_enemy(self, duration):
        """Break enemy defence, hits many enemies ahead of you"""
        duration = random.uniform(duration - .25, duration + 1.5)
        pyautogui.mouseDown(self.E)
        time.sleep(duration)
        pyautogui.mouseUp()
        self.heal()
        
    def shield_charge(self, duration):
        """Shield Charge moves player forward and knocks back the enemies"""
        duration = random.uniform(duration - 1.5, duration + 1.5)
        pyautogui.mouseDown(self.F)
        time.sleep(duration)
        pyautogui.mouseUp()
        self.heal()
        
    def scooby_bats(self):
        """Sends small horde of bats to obtain enemy agro"""
        cool_down = 8
        if (time.time() - self.scooby_bat_timer) > cool_down:
            pyautogui.mouseDown(self.D)
            time.sleep(0.35)
            pyautogui.mouseUp()
            cooldown_timer = time.time()
        
    def nether_shield(self):
        """Sends homing shields out to attack enemies"""
        cool_down = 6
        if (time.time() - self.nethershield_timer) > cool_down:
            self.nethershield_timer = time.time()
            pyautogui.mouseDown(self.A)
            time.sleep(0.55)
            pyautogui.mouseUp()
            self.heal()
            
    def gas_explosion(self, duration):
        """Gas storm damages enemies life steal with exploding AOE finale"""
        cool_down = 12
        if (time.time() - self.gas_explosion_timer) > cool_down:
            duration = random.uniform(duration - 1.5, duration + 1.5)
            pyautogui.mouseDown(self.S)
            time.sleep(duration)
            pyautogui.mouseUp()
            self.heal()


    def random_ability(self, duration):
        random_abilities = {1 : self.debuff_enemy,
                         2 : self.shield_charge,
                         3 : self.gas_explosion,
                         4 : self.scooby_bats,
                         5 : self.nether_shield}
        ability_selector = random.randrange(1, 5)
        if ability_selector == 4 or ability_selector == 5:
            random_abilities[ability_selector]()
        else:
            random_abilities[ability_selector](duration)
        
    #Tactics    
    def spam_attack(self, duration):
        """All action non-stop attack rampage super killer mode"""
        logging.info('Starting spam_attack.')
        tactic_timer = time.time()
        turn_timer = time.time()
        level = 0
        while (time.time() - tactic_timer) < duration:
            self.heal()
            self.buffs()
            self.nether_shield()
            self.shield_charge(random.randrange(9, 18))
            self.nether_shield()
            self.gas_explosion(random.randrange(3, 9))
            self.nether_shield()
            self.debuff_enemy(random.randrange(7, 16))
            self.heal()
            self.scooby_bats()
            spam_timer = time.time()
            while (time.time() - spam_timer) < random.randrange(3, 8):
                pyautogui.mouseDown(self.Q)
            pyautogui.mouseUp()
            self.loot_ahead()
            self.level_navigation()
        logging.info('Ending spam_attack.')
                
    def stormy_weather(self, duration):
        """Spams shield knock back and Gas_explosion
            Warning: This method does NOT use exceed!
                     This tactic may eat up more pots"""
        logging.info('Starting stormy_weather.')
        tactic_timer = time.time()
        level = 0
        while (time.time() - tactic_timer) < duration:
            #Pre-battle
            self.buffs()
            self.heal()
            #Set them up
            self.shield_charge(random.randrange(12, 19))
            self.debuff_enemy(random.uniform(7, 15))
            self.gas_explosion(random.uniform(5.5, 10.5))
            self.run('opposite', random.uniform(0.5, 1.25))
            self.turn()
            self.loot_corner(self.direction)
            self.run('forward', random.uniform(0.8, 2.50))
            self.level_navigation()
        logging.info('Ending stormy_weather.')
        
    def balls_to_the_wall(self, duration):
        """Pushes enemy to end of field with shield.
           Then launches every powerful attack that's not 
           currently cooling down. Loots corner afterwards."""
        logging.info('Starting balls_to_the_wall.')
        tactic_timer = time.time()
        level = 1
        while (time.time() - tactic_timer) < duration:
            self.buffs()
            self.heal()
            #Set them up
            self.shield_charge(random.randrange(10, 18))
            self.gas_explosion(random.randrange(6, 10))
            self.nether_shield()
            self.run('opposite', random.uniform(.5, 1.25))
            self.turn()
            #Knock them down
            attack_timer = time.time()
            self.debuff_enemy(random.uniform(.5, 3.5))
            while (time.time() - attack_timer) < random.randrange(8, 12):
                pyautogui.mouseDown(self.Q)
                self.heal()
                self.nether_shield()
                self.scooby_bats()
            pyautogui.mouseUp()
            #Pick up remains and reposition
            self.loot_corner(self.direction)
            self.run('forward', random.uniform(.5, 1.25))
            self.nether_shield()
            self.level_navigation()
        logging.info('Ending balls_to_the_wall.')
            
    def random_tactics(self):
        """Selects random tactic with random duration"""
        tactics = {1 : self.spam_attack,
                   2 : self.stormy_weather,
                   3 : self.balls_to_the_wall}
        tactic_selector = random.randrange(1, 3)
        tactic_duration = random.randrange(75, 225)
        logging.info('Preforming tactic %s for %d seconds.', tactic_selector, tactic_duration)
        tactics[tactic_selector](tactic_duration)
            
def main():
    #time.sleep(3.5)
    demonBot = DemonAvenger()
    while True:
        for x in range(4):
            demonBot.buffs()
            demonBot.heal()
            demonBot.random_ability(random.uniform(6, 25))
            #Loot 
            for x in range(10):
                if demonBot.direction is 'left':
                    pyautogui.mouseDown(demonBot.LEFT)
                elif demonBot.direction is 'right':
                    pyautogui.mouseDown(demonBot.RIGHT)
                time.sleep(0.1)
                pyautogui.click(demonBot.Z)
                pyautogui.mouseUp()
            #demonBot.run('forward', random.uniform(0.3, 1.75))
            #pyautogui.mouseDown(demonBot.Z)
            #time.sleep(random.uniform(1.0, 2.5))        #demonBot.random_tactics()
            #pyautogui.mouseUp()
        demonBot.level_navigation()
        demonBot.turn()
        logging.info('DemonAvenger main loop cycling')
if __name__ == '__main__': main()