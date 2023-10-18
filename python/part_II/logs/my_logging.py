import logging
import os
cwd = os.getcwd()
logPath = os.path.join(cwd, "python","part_II","logs", "sample.log")
# add filemode="w" to overwrite
logging.basicConfig(filename=logPath, level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")