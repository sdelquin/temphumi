import sys
import os
import config

if sys.argv[1] == "open":
    os.system("picocom /dev/{} -b 115200".format(config.TTY_HANDLER))
elif sys.argv[1] == "deploy":
    print("""
        mpfs [/]> open {}
        mpfs [/]> put config.py
        mpfs [/]> put main.py
        mpfs [/]> exit
    """.format(config.TTY_HANDLER))
    os.system("mpfshell")
else:
    print("⚠️  Unkown option!")
