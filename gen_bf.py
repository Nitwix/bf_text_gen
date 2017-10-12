import sys, math

def last_div(n):
	d = n - 1
	while d > 1:
		if n/d - int(n/d) == 0:
			return d
		d -= 1
	return 0

def to_nums(bf_code):
	n_str = ""
	for l in bf_code:
		if l == ">":
			n_str += "0"
		elif l == "<":
			n_str += "1"
		elif l == "+":
			n_str += "2"
		elif l == "-":
			n_str += "3"
		elif l == ".":
			n_str += "4"
		elif l == ",":
			n_str += "5"
		elif l == "[":
			n_str += "6"
		elif l == "]":
			n_str += "7"
	return n_str

def cut_print(text, size):
	parts = math.ceil(len(text)/size)
	for i in range(parts):
		print("\n"+text[i*size:(i+1)*size])


o_str = ""
with open(sys.argv[1], "r") as f:
	data = f.read()
	for char in data:
		ch_code = ord(char)
		div = last_div(ch_code)
		if div == 0:
			o_str += ">" + ch_code*"+" + "."
		else:
			mult = int(ch_code / div)
			o_str += ">" + mult*"+" + "[>" + div*"+" + "<-]>."

print(o_str)
print("cut : \n")
cut_print(o_str, 321)

