##hangman!!!
import os 
import random

picture = list(" "*10)
picture[0] = """
   __________
   |	    |
   |       
   |     
   |    
   |    
   |       
   |       
   |       
   |      
___|___

"""

picture[1] = """
   __________
   |	    |
   |       ( )
   |
   |
   |
   |         
   |       
   |    
   |      
___|___

"""
picture[2] = """
   __________
   |	    |
   |       ( )
   |        |-=\\
   |           |
   |
   |          
   |    
   |       
   |      
___|___

"""
picture[3] = """
   __________
   |	    |
   |       ( )
   |     /=-|-=\\
   |     |     |
   |        
   |
   |       
   |       
   |    
___|___

"""
picture[4] = """
   __________
   |	    |
   |       ( )
   |     /=-|-=\\
   |     |  |  |
   |        |
   |          
   |       
   |       
   |      
___|___

"""
picture[5] = """
   __________
   |	    |
   |       ( )
   |     /=-|-=\\
   |     |  |  |
   |        |
   |         ]   
   |         |
   |         |
   |          --
___|___

"""
picture[6] = """
   __________
   |	    |
   |       ( )
   |     /=-|-=\\
   |     |  |  |
   |        |
   |       [ ]   
   |       | |
   |       | |
   |      -- --
___|___

"""
picture[7] = """
    _________
   |	    |
   |       (**)
   |     /=-|-=\\
   |     |  |  |
   |        |
   |       [ ]   
   |       | |
   |       | |
   |      -- --
___|___

"""



print (picture[0])





print('welcom to HANGMAN!!!')
country_list = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Deps', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 
     'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia Herzegovina'
     , 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Rep', 'Chad'
     , 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 
     'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 
     'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 
     'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 
     'Kazakhstan', 'Kenya', 'Kiribati', 'North Korea', 'South Korea', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 
     'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 
     'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar,  {Burma}', 'Namibia', 'Nauru', 'Nepal', 
     'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 
     'Poland', 'Portugal', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'St Kitts and Nevis', 'St Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 
     'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 
     'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 
     'Tunisia', 'Turkey', 'Turkmenistan', 
     'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'United Collection of Federated States of Democratic Peoples Republic of North Republic of Nathanville', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 
     'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

pick = random.randint(1,len(country_list))
#print(country_list[pick])

letters = list(country_list[pick])
#print(letters)
num_letters = len(letters)
#print(num_letters)
guess = list("_"*num_letters)



def print_guess() :
    global guess
    string_guess = ' '.join(guess)
    print (string_guess)


print_guess()
miscounter = 0
solved = 0
try_counter = 0

while not solved :
    choice = input ("enter a letter : ")
    found = 0
    for index, ss in enumerate(letters) :
        if choice.lower() == ss.lower() :
            guess[index] = ss
            found = 1
        
    if found != 1 :
        miscounter += 1
        print (picture[miscounter])
        if miscounter >= 7 :
            break
        

    solved = 1
    for gg in guess:
        if gg == "_" :  solved = 0

    print_guess()

    try_counter += 1


if (solved==0) :
    print ("you loose")
    print ("your word was ..... ")
    print (country_list[pick])
    input('press enter to exit')
else :
    print("you won!!!!!!!!!!!!!")
    input('press enter to exit')


