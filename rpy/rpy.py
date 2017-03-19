import RpyManager 
import sys

def main():
    print("main")
    rpyManager = RpyManager.RpyManager()
    rpyManager.do(sys.argv)

if __name__ == "__main__":
    main();
