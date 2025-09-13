# Cryptographically-secure-password-generator
I was tired of web browser password generators. Half the time, they don't even present the option to create a new password in the html input field on the website. You would think it wouldn't be hard for a web browser to read for a <input type='password"> and present users an option to run their password generator. Alas, many web browsers fall short. 
I didn't want to use an online password generator that records your IP address. 
For obvious reasons, that seems like a security risk.
So I created a python script that will run all the most important password requirements for the user to choose on a cmd line. This password generator is cryptographically secure. 

You can choose the password length, lowercase letters, uppercase letters, numericals and symbols. The last option for ambiguous characters helps people avoid transcribing the incorrect password in case they ever need to write it down or don't have the password generator available

The best password are at least 14-16 characters long; include a mix of letters, special characters, and numbers, all of which is possible with this script. The longer and more complex your password, the more computational power must be devoted to cracking it. Ultimately, however, the choice is yours and this script makes it easier to satisfy the annoying requirements of websites that inisist on various default before they'll allow you to generate one.
