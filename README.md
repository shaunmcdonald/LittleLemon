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

# API
If using new Insomnia (or maybe latest Djoser) be sure to see below section [Insomnia](#Insomnia)

## GET
127.0.0.1:8000/restaurant/menu
127.0.0.1:8000/restaurant/menu/1
127.0.0.1:8000/restaurant/booking/tables
127.0.0.1:8000/restaurant/booking/tables/2024-11-01

## POST
127.0.0.1:8000/restaurant/menu/
BODY =  {
            "id": 3,
            "title": "Salad",
            "price": "7.00",
            "inventory": 25
        }

## PUT
127.0.0.1:8000/restaurant/menu/3/
BODY =  {
            "id": 3,
            "title": "Salad",
            "price": "8.00",
            "inventory": 25
        }

# Insomnia
Several hours spent on this as Insomnia application features seem to be ahead of its documentation.

It doesn't seem to work anymore as it's explained in the Coursera videos and readings. There is no Debug tab that I can find.
And just sending a Get request without any Headers is impossible. It defaults to at least sending Host. Along with Accept = "*/*".

I had to add a Cookie to get a token-authenticated response from GET. It may be that Django or Djoser have updated in Python3.13.

EDIT: So the Cookie was just letting me in via Session Auth, which means it was still not properly configured. There was nothing
wrong with my Django setup or Views. The problem is that Auth - Bearer Token no longer works with Djoser.

FIX - In the latest Insomnia...
1) Remove Auth tab's Bearer Token
2) On Headers tab, add
   1) Content-Type : application/json
   2) Authorization : Token you_token_value

Step 2,2 is the change. The header key is "Authorization". The value is "Token your_auth_token" (Yes, separated by a space!)

