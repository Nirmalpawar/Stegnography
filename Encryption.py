from PIL import Image
import stepic


   #Encryption

original_img = Image.open('img.jpg')

encoded_img = stepic.encode(original_img,b'You have been hackeds HAHAHAHAHAHAHAHAH')

encoded_img.save('hack.png')
encoded_img=Image.open('hack.png')
original_img.show()




#Decryption

decoded_img = stepic.decode(encoded_img)

print(decoded_img)
   