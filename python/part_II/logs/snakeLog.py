import logging
import otherMod
import os
cwd = os.getcwd()
logPath = os.path.join(cwd, "python","part_II","logs", "mySnake.log")
def main():
    """
    The main entry point of the application
    """
    logging.basicConfig(filename=logPath, level=logging.INFO)
    logging.info("Program started")
    result = otherMod.add(7, 8)
    logging.info("Done!")

if __name__ == "__main__":
    main()