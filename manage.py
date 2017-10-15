import sys
import os
import config

if sys.argv[1] == "open":
    os.system("picocom /dev/{} -b 115200".format(config.TTY_HANDLER))
elif sys.argv[1] == "deploy":
    os.system(
        "mpfshell -n -c 'open {}; put temphumi.py; put config.py'".format(
            config.TTY_HANDLER
        )
    )
else:
    print("⚠️  Unkown option!")
