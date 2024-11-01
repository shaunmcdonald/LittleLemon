# LittleLemon

# Admin Account
- Username: admin
- Email: admin@littlelemon.com
- Password: lemon@789!
- Token: 5756c74007a1852263f4e5001affc780d468be9b

# MySQL
I have commented the MySQL Conf in settings.py so that I can use a local db.cnf file.

To use your MySQL instance, just uncomment the key/value pairs in the DATABASES setting and add your DB details.

It will override the OPTIONS settings. At least, it does on my machine :).

# My User
Username: black_panther
Email: chadwick@littlelemon.com
Password: avengers24
Token: f737ca2b5dd76c7de163a7704f707a40459401d4

# Insomnia
Several hours spent on this as Insomnia application features seem to be ahead of its documentation.

It doesn't seem to work anymore as it's explained in the Coursera videos and readings. There is no Debug tab that I can find.
And just sending a Get request without any Headers is impossible. It defaults to at least sending Host. Along with Accept = "*/*".

I had to add a Cookie to get a token-authenticated response from GET. It may be that Django or Djoser have updated in Python3.13.

