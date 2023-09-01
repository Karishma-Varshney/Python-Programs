# program based on function with inputs

logo = ''' ██████  █████  ███████ ███████  █████  ██████           ██████ ██ ██████  ██   ██ ███████ ██████  
██      ██   ██ ██      ██      ██   ██ ██   ██         ██      ██ ██   ██ ██   ██ ██      ██   ██ 
██      ███████ █████   ███████ ███████ ██████          ██      ██ ██████  ███████ █████   ██████  
██      ██   ██ ██           ██ ██   ██ ██   ██         ██      ██ ██      ██   ██ ██      ██   ██ 
 ██████ ██   ██ ███████ ███████ ██   ██ ██   ██          ██████ ██ ██      ██   ██ ███████ ██   ██   '''

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# if direction == "encode":
#         # to encode the message
#         def encrypt(plain_text,shift_num):
    
#             cipher_text = ""
#             for char in plain_text:
#                 pos = alphabet.index(char)
#                 new_pos = pos + shift_num
#                 new_letter = alphabet[new_pos]
#                 cipher_text += new_letter
         
#             print(f"The encoded text is {cipher_text}")

#         encrypt(plain_text = text, shift_num = shift)
     
# elif direction == "decode":

#     # to decode the message
#     def decrypt(plain_text,shift_num):
#         cipher_text = ""
#         for char in plain_text:
#             pos = alphabet.index(char)
#             new_pos = pos - shift_num
#             new_letter = alphabet[new_pos]
#             cipher_text += new_letter 
        
#         print(f"The decoded text is {cipher_text}")
#     decrypt(plain_text = text, shift_num = shift)

# else:
#      print("enter a valid choice \n")    
        

# another way for customized code
def caesar(start_text,shift_num,cipher_direction):
     if cipher_direction == "decode":
          shift_num *= -1
     end_text = ""
     for letter in start_text:
          
          if letter in alphabet:  
             pos = alphabet.index(letter)
             new_pos = pos + shift_num
             end_text += alphabet[new_pos]
          else:
               end_text += letter   
     print(f"the {direction}d is {end_text}")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("enter your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26     

    caesar(start_text = text, shift_num = shift, cipher_direction = direction)   

    n = input("if you want to continue type 'yes' or type 'no' to discontinue: \n").lower()
    if n=="no":
        should_continue = False
        print("ok bye")
          

