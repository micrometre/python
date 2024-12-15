# main.py -- put your code here!
import sys
import time

def main():
    print("{} File Name isn't".format(sys.copyright))
    time.sleep(0.5)

if __name__=="__main__":
  print("{} initialized".format(sys.platform))
  while(1):
    try:
      main()
    except KeyboardInterrupt:
      print("Program stopped")
      sys.exit(0)