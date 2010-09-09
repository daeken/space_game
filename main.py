import renderer

import sys

try:
    import psyco
    psyco.full()
except ImportError:
    print 'Psyco not loaded'

def main(args):
    ren = renderer.Renderer()

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))
