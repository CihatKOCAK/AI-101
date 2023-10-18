# log_with_config.py
import logging
import logging.config
import otherMod2
import os
cwd = os.getcwd()
logPath = os.path.join(cwd, "python","part_II","logs", "config2.log")
def main():
    dictLogConfig = {
        "version":1,
        "handlers":{
                    "fileHandler":{
                        "class":"logging.FileHandler",
                        "formatter":"myFormatter",
                        "filename":logPath
                        }
                    },
        "loggers":{
            "exampleApp":{
                "handlers":["fileHandler"],
                "level":"INFO",
                }
            },

        "formatters":{
            "myFormatter":{
                "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                }
            }
        }

    logging.config.dictConfig(dictLogConfig)

    logger = logging.getLogger("exampleApp")

    logger.info("Program started")
    result = otherMod2.add(7, 8)
    logger.info("Done!")

if __name__ == "__main__":
    main()