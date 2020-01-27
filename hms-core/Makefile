# Makefile for the HMS Core (hms-core) project

main: test setup
	# Doesn't (yet) do anything other than running the test and 
	# setup targets

setup:
	# Calls the main setup.py to build a source-distribution
	# python setup.py sdist

test:
	# Executes the unit-tests for the package, allowing the build-
	# process to die and stop the build if a test fails
	# /media/eg/Seagate Expansion Drive/APPS/hms_sys/hosewp/hms-core/venv/bin
	~/py_envs/hms/core/bin/python setup.py test
