from keys import KeyLocations
import pyautogui as p 

p.PAUSE = 0.5
class key_test(KeyLocations):
    def __init__(self):
        super().__init__()
        
    def test_keyboard(self, row='all'):
        if row is 'q' or row is 'Q' or row is 'all':
            p.moveTo(self.Q)
            p.moveTo(self.W)
            p.moveTo(self.E)
            p.moveTo(self.R)
            p.moveTo(self.T)
            p.moveTo(self.Y)
            p.moveTo(self.U)
            p.moveTo(self.I)
            p.moveTo(self.O)
            p.moveTo(self.P)
        if row is 'a' or row is 'A' or row is 'all':
            p.moveTo(self.A)
            p.moveTo(self.S)
            p.moveTo(self.D)
            p.moveTo(self.F)
            p.moveTo(self.G)
            p.moveTo(self.H)
            p.moveTo(self.J)
            p.moveTo(self.K)
            p.moveTo(self.L)
        if row is 'z' or row is 'Z' or row is 'all':
            p.moveTo(self.Z)
            p.moveTo(self.X)
            p.moveTo(self.C)
            p.moveTo(self.V)
            p.moveTo(self.B)
            p.moveTo(self.N)
            p.moveTo(self.M)
        if row is 'misc' or row is 'tab' or row is 'all':
            p.moveTo(self.TAB)
            p.moveTo(self.CAPS)
            p.moveTo(self.SHIFT)
            p.moveTo(self.CTRL)
            p.moveTo(self.ALT)
        if row is 'arrows' or row is 'all':
            p.moveTo(self.LEFT)
            p.moveTo(self.RIGHT)
            p.moveTo(self.UP)
            p.moveTo(self.DOWN)
        if row is 'ESC' or row is 'numbers' or row is 'all':
            p.moveTo(self.ESC)
            p.moveTo(self.TILDA)
            p.moveTo(self.ONE)
            p.moveTo(self.TWO)
            p.moveTo(self.THREE)
            p.moveTo(self.FOUR)
            p.moveTo(self.FIVE)
            p.moveTo(self.SIX)
            p.moveTo(self.SEVEN)
            p.moveTo(self.EIGHT)
            p.moveTo(self.NINE)
            p.moveTo(self.ZERO)
    