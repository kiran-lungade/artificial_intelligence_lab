'''
	NAME:: LUNGADE KIRAN SANJAY
	TITLE:: EXPERT SYSTEM USING PYTHON
'''

while True:
	question=input('Enter the Question:')
	m=question.lower()
	if m in ['hello','hi']:
		print('Hello')
	elif m in ['what is your name ?', 'what is your name','your name?','your name']:
		print('abc')
	elif m in ['how are you ?']:
		print('Fine')
	elif m in ['where are you from ?','your native place ?']:
		print('Kopargaon')
	elif m in ['what are your hobbies ?','your interest']:
		print('Playing Cricket')
	elif m in ['who is your best friend ?']:
		print('xyz')
	elif m in ['what are your college name ?']:
		print('Sanjivani College of Engineering')
	elif m in ['what is your department name ?']:
		print('Information Technology')
	elif m in ['no']:
		print('Thank You for visiting!! ')
		break
	else:
		print('Cannot recognize the question!! ')
		print('Ask me valid question, if no press NO')

'''
***************     OUTPUT     ***************

Enter the Question:HI
Hello
Enter the Question:YOUR NAME
abc
Enter the Question:YOUR INTEREST
Playing Cricket
Enter the Question:what are your college name ?
Sanjivani College of Engineering
Enter the Question:HOW DO U DO
Cannot recognize the question!! 
Ask me valid question, if no press NO
Enter the Question:NO
Thank You for visiting!! 

'''
