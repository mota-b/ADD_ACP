import sys,tty,termios

class Getch:
    def __call__(self, nb_char):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(nb_char)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
    key = ""

    getch = Getch()
    while(True):
        k = getch(1)
        print k[0]
        if k[0] =='\x1b': # Arrow prefix
            # Is Arrow
            k += getch(2)
            if k=='\x1b[A':
                key = "up"
            elif k=='\x1b[B':
                key = "down"
            elif k=='\x1b[D':
                key = "left"
            elif k=='\x1b[C':
                key = "right"
        else:
            # Is not Arrow
            key = ord(k)
        if k!='': break
        
    return key



''' getch = Getch()
k = getch(3)
for e in k :
    print ord(e), e
    if e == '\n':
        
        print "enter ?" '''


def wait():
    getch = Getch()
    k = getch(1)
    return ord(k)