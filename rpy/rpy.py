import RpyManager 
import sys

def main():
    print("main")
    rpyManager = RpyManager.RpyManager()
    rpyManager.init(sys.argv)

    rpyManager.do()

if __name__ == "__main__":
    main();
