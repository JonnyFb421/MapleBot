import os
import platform
import logging
import pyautogui

"""
Author: JonathonCarlyon (JonathonCarlyon@gmail.com)

KeyLocations maps out the position of they keys on the On-Screen Keyboard (OSK)
Currently OSK's height must be minimized for all keys to be detected.
"""

class KeyLocations():
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
        logging.info('Starting key matching')
        os_version = platform.platform().split('-')[:2]
        os_version = ' '.join(os_version)
        osk_filepath = os.path.abspath(r'assets\osk\{}'.format(os_version))
        logging.info("Looking for On-Sreen Keyboard")
        osk_icon = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'OSK.png'))
        if not osk_icon:
            sys.exit("Unable to detect On-Screen Keyboard")
        logging.info("On-Screen keyboard detected.")
        OSK_LOCATION = (osk_icon[0] - 25, osk_icon[1], 500, 500)
        self.Q = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'Q.png'), region=OSK_LOCATION, grayscale=True)
        self.W = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'W.png'), region=OSK_LOCATION, grayscale=True)
        #Space between keys
        pixel_space = (self.W[0] - self.Q[0])
        self.E = (self.W[0] + pixel_space, self.Q[1])
        self.R = (self.E[0] + pixel_space, self.Q[1])
        self.T = (self.R[0] + pixel_space, self.Q[1])
        self.Y = (self.T[0] + pixel_space, self.Q[1])
        self.U = (self.Y[0] + pixel_space, self.Q[1])
        self.I = (self.U[0] + pixel_space, self.Q[1])
        self.O = (self.I[0] + pixel_space, self.Q[1])
        self.P = (self.O[0] + pixel_space, self.Q[1])
        #
        self.A = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'A.png'), region=OSK_LOCATION, grayscale=True)
        self.S = (self.A[0] + pixel_space, self.A[1])
        self.D = (self.S[0] + pixel_space, self.A[1])
        self.F = (self.D[0] + pixel_space, self.A[1])
        self.G = (self.F[0] + pixel_space, self.A[1])
        self.H = (self.G[0] + pixel_space, self.A[1])
        self.J = (self.H[0] + pixel_space, self.A[1])
        self.K = (self.J[0] + pixel_space, self.A[1])
        self.L = (self.K[0] + pixel_space, self.A[1])
        #
        self.Z = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'Z.png'), region=OSK_LOCATION, grayscale=True)
        self.X = (self.Z[0] + pixel_space, self.Z[1])
        self.C = (self.X[0] + pixel_space, self.Z[1])
        self.V = (self.C[0] + pixel_space, self.Z[1])
        self.B = (self.V[0] + pixel_space, self.Z[1])
        self.N = (self.B[0] + pixel_space, self.Z[1])
        self.M = (self.N[0] + pixel_space, self.Z[1])
        #
        self.ESC = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'ESC.png'), region=OSK_LOCATION, grayscale=True)
        self.TILDA = (self.ESC[0] + pixel_space, self.ESC[1])
        self.ONE = (self.TILDA[0] + pixel_space, self.ESC[1])
        self.TWO = (self.ONE[0] + pixel_space, self.ESC[1])
        self.THREE = (self.TWO[0] + pixel_space, self.ESC[1])
        self.FOUR = (self.THREE[0] + pixel_space, self.ESC[1])
        self.FIVE = (self.FOUR[0] + pixel_space, self.ESC[1])
        self.SIX = (self.FIVE[0] + pixel_space, self.ESC[1])
        self.SEVEN = (self.SIX[0] + pixel_space, self.ESC[1])
        self.EIGHT = (self.SEVEN[0] + pixel_space, self.ESC[1])
        self.NINE = (self.EIGHT[0] + pixel_space, self.ESC[1])
        self.ZERO = (self.NINE[0] + pixel_space, self.ESC[1])
        #
        self.ALT = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'ALT.png'), region=OSK_LOCATION, grayscale=True)
        self.CTRL = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'CTRL.png'), region=OSK_LOCATION, grayscale=True)
        self.SHIFT = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'SHIFT.png'), region=OSK_LOCATION, grayscale=True)
        self.CAPS = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'CAPS.png'), region=OSK_LOCATION, grayscale=True)
        self.TAB = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'TAB.png'), region=OSK_LOCATION, grayscale=True)
        self.ALT = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'ALT.png'), region=OSK_LOCATION, grayscale=True)
        #
        self.LEFT = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'LEFT.png'), region=OSK_LOCATION, grayscale=True)
        self.RIGHT = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'RIGHT.png'), region=OSK_LOCATION, grayscale=True)
        self.UP = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'UP.png'), region=OSK_LOCATION, grayscale=True)
        self.DOWN = pyautogui.locateCenterOnScreen(os.path.join(osk_filepath, 'DOWN.png'), region=OSK_LOCATION, grayscale=True)
        logging.info('Done matching')