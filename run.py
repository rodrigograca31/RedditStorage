import praw
from reddit import *
import getpass

from crypt import AESCipher
import hashlib
import os
from key import *
import base64

from Crypto.Cipher import AES
from Crypto import Random

from redditglobals import * 

def _login():
    USERNAME = raw_input("Username: ")
    #PASSWORD = getpass.getpass()
    PASSWORD = raw_input("Password: ")
    r.login(USERNAME, PASSWORD)

def checkForMod(user, subreddit):
        
    subr = r.get_subreddit(subreddit)
    mods = subr.get_moderators()

    for mod in mods: 
        if mod == user:
            return True
    return False 


trying = True

while trying:
    try:
        _login()
        trying = False
    except praw.errors.InvalidUserPass:
        print "Invalid user/pass. Please try again."


SUBREDDIT = raw_input("Subreddit: ")

while checkForMod(USERNAME, SUBREDDIT):
    print "Enter a different subreddit."
    SUBREDDIT = raw_input("Subreddit: ")

    
while True:

    filename = raw_input("enter file: ")
    selection = raw_input("post or get: ")
    cipher = AESCipher(KEYPASS)
    
    if selection == "post":
        comment = cipher.encrypt_file(filename)
        post_encryption(filename, comment)
    else:
        comment = get_decryption(filename)
        cipher.decrypt_file(comment, filename)
    print "done"

    


