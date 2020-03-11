class colors:
    def __init__(self, color=None):
        if not color:
            print('Colors in between: 0-7')
        else:
            self.text       = '\033[%sm' % (int(color) + 30)
            self.background = '\033[%sm' % (int(color) + 40)

black       = colors(0)
red         = colors(1)
green       = colors(2)
yellow      = colors(3)
blue        = colors(4)
purple      = colors(5)
turquoise   = colors(6)
white       = colors(7)