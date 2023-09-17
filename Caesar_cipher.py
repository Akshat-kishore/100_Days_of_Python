alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(user_text, shift_amt, direct):
  output_text = ""
  for letter in user_text:
    position = alphabet.index(letter)
    if direct == "encode":
      new_position = position + shift_amt
      output_text += alphabet[new_position]
    

    else:
      new_position = position - shift_amt
      output_text += alphabet[new_position]

  print(f"Here's the {direction}d result: {output_text}")
caesar(user_text=text, shift_amt=shift, direct=direction)
