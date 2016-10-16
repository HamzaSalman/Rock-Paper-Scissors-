# coding: utf-8

import ui
import random

box = ['rock_button', 'paper_button', 'scissors_button']

def rock_paper_scissors_touch_up_inside(sender):
	
	random_number = random.randint(0, 2)
	print(box[random_number])
	view['computer_answer'].text = 'The computer picked ' + str(box[random_number])
	if sender.name == 'rock_button' and box[random_number] == 'scissors_button' or sender.name == 'paper_button' and box[random_number] == 'rock_button' or sender.name == 'scissors_button' and box[random_number] == 'paper_button':
		
		view['answer_label'].text = "You win this round!" 
		pl
		p
	
	
	elif sender.name == box[random_number]:
		
		view['answer_label'].text = "Its a tie!"
	else:
		
		view['answer_label'].text = "You lost this round!"
	



view = ui.load_view()
view.present('full_screen')
