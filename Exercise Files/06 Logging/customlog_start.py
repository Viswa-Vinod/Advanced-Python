# Demonstrate how to customize logging output

import logging

extraData = {
    "user": "vinod@example.com"
}
# TODO: add another function to log from
def anotherFunc():
    logging.debug("This is a debug level message", extra=extraData)

def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d %(message)s"
    datestr = "%d/%m/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=fmtstr,
                        datefmt = datestr)

    logging.info("This is an info-level log message", extra=extraData)
    logging.warning("This is a warning-level message", extra=extraData)
    anotherFunc()

if __name__ == "__main__":
    main()
