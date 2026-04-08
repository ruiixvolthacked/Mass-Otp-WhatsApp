mow:
	@clear
	pkg update -y && pkg upgrade -y
	pkg install python python3
	pip install requests pycryptodome

	@clear
	@python test.py
