import threading
import time
import random

"""
Program that shows the concept of a timer
run it several times and you will see how
timers trigger or get cancelled depending
upon the random sleeping time
"""


def hello_t3():
    print ">>>>>> Triggered Timer 3"

def hello_t5():
    print ">>>>>> Triggered Timer 5"


if __name__ == '__main__':

	print "Starting 3s"	
	t3 = threading.Timer(3.0, hello_t3)
	t3.start()

	print "Starting 3s"	
	t5 = threading.Timer(5.0, hello_t5)
	t5.start()

	# Waiting random time
	sleep_time = random.randint(1,5)
	print "Sleeping for " + str(sleep_time)
	time.sleep(sleep_time)
	
	# Canceling timer after random time if 
	# it has not triggered
	if t3.is_alive():
		print "Cancelling t3"
		t3.cancel()

	# Waiting random time
	sleep_time = random.randint(1,5)
	print "Sleeping for " + str(sleep_time)
	time.sleep(sleep_time)
	
	# Canceling timer after random time if 
	# it has not triggered
	if t5.is_alive():
		print "Cancelling t5"
		t5.cancel()

