from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser_cipher(direction,new_text,shift_num):
  coded_word = ""
  if direction == "decode":
     shift_num *= -1
  for letter in new_text:
    if letter in alphabet:
      position = alphabet.index(letter)        
      new_position = position + shift_num
      new_letter = alphabet[new_position]
      coded_word += new_letter
    else:
      coded_word += letter
  print(f"The coded text is {coded_word}\n")
      


should_end = False
while not should_end:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  
  caeser_cipher(direction,new_text=text,shift_num=shift)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")