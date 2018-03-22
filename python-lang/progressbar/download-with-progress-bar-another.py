import sys
import requests

toolbar_width = 40

sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['                                                                      


data = requests.get("http://www.beautifulwork.org/plan/beautifulwork-algorithms.pdf", stream=True)
sys.stdout.write("-")
sys.stdout.flush()
tbw = data.read()
file = open("document.pdf", 'w')
file.write(tbw)
file.close
sys.stdout.write("\n")
