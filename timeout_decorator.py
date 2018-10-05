import time
import timeout_decorator
from exceptions import Exception

TIMEOUTSECS = 5

def a(): 
	time.sleep(1)

def b():
	time.sleep(2)

def c():
	time.sleep(3)

@timeout_decorator.timeout(5, timeout_exception=StopIteration)
def test1():
	a()
	b()

@timeout_decorator.timeout(5, timeout_exception=StopIteration)
def test2():
	a()
	b()
	c()

def main():

	print "executing test1 and waiting " + str(TIMEOUTSECS) + " secs"

	try:
		test1()
	except StopIteration:
		print "failed after " + str(TIMEOUTSECS) + " seconds"

	print "DONE!!!"

	print "executing test1 and waiting " + str(TIMEOUTSECS) + " secs"
	try:
		test2()
	except StopIteration, e:
		print "failed after " + str(TIMEOUTSECS) + " seconds"

	print "DONE!!!"

class StopIteration(Exception):
	def __init__(self, message):
		super(StopIteration, self).__init__(message)

if __name__ == '__main__':
    main()