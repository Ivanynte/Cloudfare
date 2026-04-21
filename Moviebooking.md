Greetings = 'Goodevening and welcome to the Cinema! Our showing movies are... Movie 1: PROJECT HAIL MARY(1), and Movie 2: Super Mario(2) Movie.'
print(Greetings)
Project_hail_mary = 320 
Super_Mario = 290
Student_discount = 0.20
Senior_discount = 0.30

Customer = input('What movie would you like to watch? (1 for Project Hail Mary, 2 for Super Mario): ')
if Customer == '1':
    movie = 'Project Hail Mary'
    price = Project_hail_mary
elif Customer == '2':
    movie = 'Super Mario'
    price = Super_Mario 
else:
    print('Invalid input. Please select either 1 or 2.')
    exit()
print(f'You have selected {movie}. The price is ${price}.')
customer_type = input('Are you a student or a senior? (Enter "student", "senior", or "none"): ').lower()
if customer_type == 'student':
    discount = price * Student_discount
    final_price = price - discount
    print(f'As a student, you get a 20% discount. Your final price is ${final_price:.2f}.')
elif customer_type == 'senior':
    discount = price * Senior_discount
    final_price = price - discount
    print(f'As a senior, you get a 30% discount. Your final price is ${final_price}.')
else:
    print('You are not eligible for any discounts.')
print('Thank you for booking with us! Enjoy your movie!')

