import sys
import os
import config
from fabulous.color import green, red, fg256

if sys.argv[1] == "open":
    os.system("picocom /dev/{} -b 115200".format(config.TTY_HANDLER))
elif sys.argv[1] == "deploy":
    print(fg256("#e67e22", """
        If it hangs on 'Connected to esp8266':
        - Be sure you are not connected in other session to TTY. If so,
        disconnect and try it again!
        - Otherwise, press CTRL-C, reset the NodeMCU
        by pressing the button on the board and try it again!
    """))
    files = ";".join(f"put {file}" for file in config.FILES_TO_DEPLOY)
    error = os.system("mpfshell -n -c 'open {}; {}'".format(
            config.TTY_HANDLER, files)
        )
    if error:
        print(red("Deploy failed!"))
    else:
        print(green("All files were deployed successfully!!"))
else:
    print("⚠️  Unknown option!")
