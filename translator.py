# Konstantinos Kapsimalis 4698
# Romanos Kotsis 4714

import sys

family = []
string = []
line = []
word_counter = 0
path = sys.argv[1]
keywords = ["main", "def", "#def", "#int", "global", "if", "elif","else", "while", "print", "return","input","int","and", "or", "not"]

def lex(path):
	temp = ""
	line_counter = 1
	counter = 1
	try :
		file = open(path,'r')
		s = file.read(1)
		state = 0
		while s != "" :
			flag = 0
			if state == 0 and (s == " " or s == "\t") : 
				state = 0
			elif state == 0 and s == "\n" :
				state = 0 
				line_counter = line_counter + 1
			elif state == 0 and s.isalpha() : 
				state = 1
				temp = temp + s
			elif state == 0 and s.isdigit() : 
				state = 2
				temp = temp + s
			elif state == 0 and s == '/' : 
				state = 3
				temp = temp + s 
			elif state == 0 and s == '=' : 
				state = 4
				temp = temp + s
			elif state == 0 and s == '<' : 
				state = 5
				temp = temp + s
			elif state == 0 and s == '>' : 
				state = 6
				temp = temp + s
			elif state == 0 and s == '!' : 
				state = 7
				temp = temp + s
			elif state == 0 and s == '#' : 
				state = 8
				temp = temp + s
			elif state == 0 and (s == '+' or s == '-' or s == '*' or s == '%' or s == ',' or s == ':' or s == '(' or s == ')') : 
				state = 0 
				temp = temp + s
				string.append(temp)
				if temp == '+' or temp == '-' :
					family.append("ADD_OP")
				elif temp == '*' or temp == '%' :
					family.append("MUL_OP")
				else : 
					family.append("OPERATOR")
				line.append(line_counter)
				temp = ""
			elif state == 0 : 
				raise Exception("Invalid character " + s + " at line " + str(line_counter))
			elif state == 1 and (s.isalpha() or s.isdigit()) :
				counter = counter + 1 
				if counter <= 30 : temp = temp + s
				else : temp = temp 
				state = 1
			elif state == 1 : 
				state = 0 
				counter = 1
				string.append(temp)
				if temp in keywords : family.append("KEYWORD")
				else : family.append("ID")
				line.append(line_counter)
				temp = ""
				flag = 1
			elif state == 2 and s.isdigit() :
				state = 2
				temp = temp + s
				if int(temp) > 32767 : 
					raise Exception("Out of Bounds number " + temp + " at line " + str(line_counter))
			elif state == 2 and s.isalpha() :
				raise Exception("Invalid number " + s + " at line " + str(line_counter))
			elif state == 2 :
				state = 0 
				string.append(temp)
				family.append("INTEGER")
				line.append(line_counter)
				temp = ""
				flag = 1
			elif state == 3 and s == '/' :
				state = 0 
				temp = temp + s
				string.append(temp)
				family.append("MUL_OP")
				line.append(line_counter)
				temp = ""
			elif state == 3 :
				raise Exception("Expected '/' but instead got "+ s + " at line " + str(line_counter))
			elif state == 4 and s =='=' :
				state = 0 
				temp = temp + s
				string.append(temp)
				family.append("REL_OP")
				line.append(line_counter)
				temp = ""
			elif state == 4 :
				state = 0 
				#temp = temp + s
				string.append(temp)
				family.append("ASSIGNMENT")
				line.append(line_counter)
				temp = ""
				flag = 1
			elif state == 5 and s =='=' :
				state = 0 
				temp = temp + s
				string.append(temp)
				family.append("REL_OP")
				line.append(line_counter)
				temp = ""
			elif state == 5 :
				state = 0 
				string.append(temp)
				family.append("REL_OP")
				line.append(line_counter)
				temp = ""
				flag = 1 
			elif state == 6 and s == '=' :
				state = 0 
				temp = temp + s
				string.append(temp)
				family.append("REL_OP")
				line.append(line_counter)
				temp = ""
			elif state == 6 :
				state = 0 
				string.append(temp)
				family.append("REL_OP")
				line.append(line_counter)
				temp = ""
				flag = 1 
			elif state == 7 and s == '=' :
				state = 0 
				temp = temp + s
				string.append(temp)
				family.append("REL_OP")
				line.append(line_counter)
				temp = ""
			elif state == 7 :
				raise Exception("Expected '=' but instead got "+ s + " at line " + str(line_counter))
			elif state == 8 and s == '{' :
				state = 0 
				temp = temp + s
				string.append(temp)
				family.append("GROUP_SYMBOL")
				line.append(line_counter)
				temp = ""
			elif state == 8 and s == '}' :
				state = 0 
				temp = temp + s
				string.append(temp)
				family.append("GROUP_SYMBOL")
				line.append(line_counter)
				temp = ""
			elif state == 8 and s == '#' :
				'''state = 0 
				temp = temp + s
				string.append(temp)
				family.append("COMMENTS")
				line.append(line_counter)'''
				temp = ""
				s = file.read(1)
				while s != '#' :
					s = file.read(1)
					if s == '#' :
						s = file.read(1)
						if  s == '#' :
							state = 0

			elif state == 8 and s.isalpha() :
				state = 9
				temp = temp + s
			elif state == 9 and (s.isalpha() or s.isdigit()) :
				state = 9
				temp = temp + s
			elif state == 9 :
				if temp in keywords :
					state = 0 
					#temp = temp + s
					string.append(temp)
					family.append("KEYWORD")
					line.append(line_counter)
					temp = ""
					flag = 1 
				else :
					raise Exception("Expected '#int' or '#def' but instead got "+ temp + " at line " + str(line_counter))
			if flag == 0 :
				s = file.read(1)

		#print(*string, sep = "\n")
		file.close()

	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def program() :
	global word_counter 
	while string[word_counter] == "#int" :
		hashtagIntStat()
	while string[word_counter] == "def" : 
		defStat()
	hashtagDefStat()

def block(x) :
	try: 
		global word_counter
		if x == 0 : 
			if string[word_counter] == "#{" : 
				word_counter += 1
				while string[word_counter] != "#}" :
					statement()
				if string[word_counter] == "#}" :
					word_counter += 1
				else : 
					raise Exception("Expected '#}' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
			else :
				raise Exception("Expected '#{' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
		elif x == 1 :
			while word_counter < len(string) - 1 :
				statement()
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def statement() : 
	try :
		global word_counter
		if string[word_counter] == "def" :
			defStat()
		elif string[word_counter] == "#int" :
			hashtagIntStat()
		elif string[word_counter] == "global" :
			word_counter += 1
			globalStat()
		elif string[word_counter] == "if" :
			word_counter += 1
			ifStat()
		elif string[word_counter] == "while" :
			word_counter += 1
			whileStat()
		elif string[word_counter] == "print" :
			word_counter += 1
			printStat()
		elif string[word_counter] == "return" :
			word_counter += 1
			returnStat()
		elif family[word_counter] == "ID" :
			word_counter += 1
			assignmentStat()
		else :
			raise Exception("Expected 'statement' but instead got "+ family[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def hashtagDefStat() :
	try : 
		global word_counter
		if string[word_counter] == "#def" :
			word_counter += 1
			if string[word_counter] == "main" :
				word_counter += 1
				block(1)
			else : 
				raise Exception("Expected 'main' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
		else : 
			raise Exception("Expected '#def' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def defStat() :
	try :
		global word_counter
		if string[word_counter] == "def" :
			word_counter += 1 
			if family[word_counter] == "ID" :
				word_counter += 1 
				if string[word_counter] == "(" :
					word_counter += 1
					parameters() 
					if string[word_counter] == ")" :
						word_counter += 1
						if string[word_counter] == ":" :
							word_counter += 1
							block(0)
						else : 
							raise Exception("Expected ':' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
					else : 
						raise Exception("Expected ')' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
				else : 
					raise Exception("Expected '(' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
			else : 
				raise Exception("Expected 'ID' but instead got "+ family[word_counter] +" at line "+ str(line[word_counter]))
		else : 
			raise Exception("Expected 'def' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def hashtagIntStat() :
	try :
		global word_counter
		if string[word_counter] == "#int" :
			word_counter += 1
			if family[word_counter] == "ID" :
				word_counter += 1
				while (string[word_counter] == ","):
					word_counter += 1
					if family[word_counter] == "ID" :
						word_counter += 1
					else : 
						raise Exception("Expected 'ID' but instead got "+ family[word_counter] +" at line "+ str(line[word_counter]))
			else : 
				raise Exception("Expected 'ID' but instead got "+ family[word_counter] +" at line "+ str(line[word_counter]))
		else : 
			raise Exception("Expected '#int' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def globalStat() :
	try :
		global word_counter
		if family[word_counter] == "ID" :
			word_counter += 1
		else : 
			raise Exception("Expected 'ID' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def ifStat() :
	try : 
		global word_counter
		condition()
		if string[word_counter] == ":" :
			word_counter += 1
			if string[word_counter] == "#{" : 
				block(0)
			else :
				statement()
			while string[word_counter] == "elif" :
				word_counter += 1
				elifPart()
			if string[word_counter] == "else" :
				word_counter += 1 
				elsePart()
		else : 
			raise Exception("Expected ':' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def elifPart() :
	try :
		global word_counter
		condition()
		if string[word_counter] == ":" :
			word_counter += 1
			if string[word_counter] == "#{" : 
				block(0)
			else :
				statement()
		else : 
			raise Exception("Expected ':' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def elsePart() :
	try :
		global word_counter
		if string[word_counter] == ":" :
			word_counter += 1
			if string[word_counter] == "#{" : 
				block(0)
			else : 
				statement()
		else : 
			raise Exception("Expected ':' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def whileStat() :
	try :
		global word_counter
		condition()
		if string[word_counter] == ":" :
			word_counter += 1
			block(0)
		else : 
			raise Exception("Expected ':' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def printStat() :
	try :
		global word_counter
		if string[word_counter] == "(" :
			word_counter += 1
			expression()
			if string[word_counter] == ")" :
				word_counter += 1
			else : 
				raise Exception("Expected ')' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
		else : 
			raise Exception("Expected '(' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def returnStat() :
	expression() 

def assignmentStat() :
	try :
		global word_counter
		if string[word_counter] == "=" :
			word_counter += 1
			if string[word_counter] == "int" :
				intStat()
			else :
				expression()
		else : 
			raise Exception("Expected '=' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def intStat() : 
	try :
		global word_counter
		if string[word_counter] == "int" :
			word_counter += 1
			if string[word_counter] == "(" :
				word_counter += 1
				inputStat()
				if string[word_counter] == ")" :
					word_counter += 1
				else : 
					raise Exception("Expected ')' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
			else : 
				raise Exception("Expected '(' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
		else : 
			raise Exception("Expected 'int' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1) 

def inputStat() :
	try :
		global word_counter
		if string[word_counter] == "input" :
			word_counter += 1
			if string[word_counter] == "(" :
				word_counter += 1
				if family[word_counter] == "ID" :
					word_counter += 1 
					if string[word_counter] == ")" :
						word_counter += 1
					else : 
						raise Exception("Expected ')' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
				elif string[word_counter] == ")" :
					word_counter += 1 
				else : 
					raise Exception("Expected ')' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
			else : 
				raise Exception("Expected '(' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
		else : 
			raise Exception("Expected 'input' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1) 
		 	
def expression():
	global word_counter
	optionalSign()
	term()
	while family[word_counter] == "ADD_OP":
		word_counter += 1
		term()

def term():
	global word_counter
	factor()
	while family[word_counter] == "MUL_OP" :
		word_counter += 1
		factor()

def factor():
	try :
		global word_counter
		if family[word_counter] == "ID" and string[word_counter + 1] == "(" :
			word_counter += 1
			idtail()
		elif family[word_counter] == "INTEGER" or family[word_counter] == "ID" :
			word_counter += 1
		elif string[word_counter] == "(" :
			word_counter += 1
			expression()
			if string[word_counter] == ")" :
				word_counter += 1
			else : 
				raise Exception("Expected ')' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
		elif family[word_counter] == "ID" :
			word_counter += 1
			idtail()
		elif string[word_counter] == "," :
			parameters()
		else : 
			raise Exception("Expected 'factor' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def optionalSign():
	global word_counter
	if family[word_counter] == "ADD_OP" :
		word_counter += 1

def idtail():
	try : 
		global word_counter
		if string[word_counter] == "(" :
			word_counter += 1
			parameters()
			if string[word_counter] == ")" :
				word_counter += 1 
			else : 					
				raise Exception("Expected ')' but instead got "+ string[word_counter] +" at line "+ str(line[word_counter]))
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def parameters():
	try :
		global word_counter
		expression()
		while (string[word_counter] == ","):
			word_counter += 1
			expression()
	except Exception as e :
		print(f"An error occured : {e}")
		sys.exit(1)

def condition() :
	global word_counter
	boolTerm()
	while string[word_counter] == "or" :
		word_counter += 1
		boolTerm() 

def boolTerm() :
	global word_counter
	boolFactor()
	while string[word_counter] == "and" :
		word_counter += 1
		boolFactor()

def boolFactor():
	global word_counter
	if string[word_counter] == "not" :
		word_counter += 1
		expression()
		if family[word_counter] == "REL_OP" :
			word_counter += 1
			expression()
	else :
		expression()
		if family[word_counter] == "REL_OP" :
			word_counter += 1
			expression()

lex(path)
program()