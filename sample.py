import fileinput
import sys
from shutil import copyfile

copyfile('haproxy-template-org.cfg', 'haproxy-template.cfg')

web01ip = sys.argv[1]
web01port = sys.argv[2]
web02ip = sys.argv[3]
web02port = sys.argv[4]

for line in fileinput.FileInput("haproxy-template.cfg",inplace=1):
    line = line.replace("web01ip",web01ip).replace("web01port",web01port).replace("web02ip",web02ip).replace("web02port",web02port)
    print line

