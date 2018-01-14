# Script:  caesar.py
# Desc:    encrypt and decrypt text with a Caesar cipher
#          using defined character set with index
# Author:  Oliver Thornewill von Essen (40210534)
# Created: 26/9/16
# 

charset="ABCDEFGHIJKLMNOPQRSTUVWXYZ" # characters to be encrypted
numchars=len(charset) # number of characters, for wrapping round

def caesar_encrypt(plaintext,key):
    """This will encrypt your message."""
    print '[*] ENCRYPTING - key: %d; plaintext: %s' % (key,plaintext)
       
    plaintext= plaintext.upper().replace(' ','')     # convert plaintext to upper case and removes spaces
    ciphertext='' # initialise ciphertext as empty string   

    for ch in plaintext:
        if ch in charset:
            new = charset[(charset.find(ch) + key) % numchars] #changes from plaintext to the encrypted letter
        ciphertext=ciphertext+new # continually adds result to the ciphertext
    print '[*] Ciphertext: ' + ciphertext # prints the ciphertext
    return ciphertext # returns ciphertext so it can be reused

def caesar_decrypt(ciphertext,key):
    """This will decrypt the message."""
    
    plaintext='' 
    ciphertext = ciphertext.upper() # convert ciphertext to upper case
    for ch in ciphertext:
        if ch in charset: 
            new = charset[(charset.find(ch) - key) % numchars] # changes from ciphertext to the plaintext letter
        plaintext=plaintext+new # continually adds result to the plaintext
        
    print '[*] DECRYPTING using key of %d; plaintext: %s' % (key,plaintext)
    return plaintext # returns plaintext so it can be reused

def caesar_crack(ciphertext):
    """Brute forceing a ciphertext """
    for lenx in range(numchars): # Starts a for loop for the key 
        crack=caesar_decrypt(ciphertext,lenx) # attempts crack
    
def main():
    key=2
    plain1 = 'Hello Suzanne'
    cipher1 = 'IQQfOQtpKpIGXGtaQPG'
    crackme = 'PBATENGHYNGVBAFLBHUNIRPENPXRQGURPBQRNAQGURFUVSGJNFGUVEGRRA' 

    print '   Question 1: Encrypt the message'
    print
    caesar_encrypt(plain1, key)
    print
    print '   Question 2: Decrypt the message: ' +cipher1
    print
    caesar_decrypt(cipher1,key)
    print
    print '   Question 3: Brute force decrypt the message'
    print
    caesar_crack(crackme)  # remove comment to test cracking

# boilerplate
if __name__ == '__main__':
    main()
