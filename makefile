open:
	picocom /dev/tty.wchusbserial1410 -b 115200

deploy:
	mpfshell -n -c "open tty.wchusbserial1410; put temphumi.py"
