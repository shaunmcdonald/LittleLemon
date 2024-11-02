# LittleLemon

FYI, I had a terrible realization just before turning this project in, when I discovered that the only template I had was the index.html.

I wasn't sure if that was enough to satisfy the requirement "Does the web application use Django to serve static HTML content?"

So, I decided to add the templating for the entire site using previous work. Ha ha! This ended up requiring new TestCases, refactors of the ViewSets,
Routing, Project Config, a new Form etc. I broke the app many, many, many times.

I say all this as an apology to my reviewers, because I'd wanted to write some nice documentation. I'm a little tired now, so you get MVP docs :).

I'm going to keep this project as a base for other stuff, so if you find something that isn't working, please message me via GitHub.
Or, feel free to Pull Request.

# Python
Be sure to edit the PipFile to match your prederred Python Version!
[requires]
python_version = "3.13"

# MySQL
I have commented the MySQL Conf in settings.py so that I can use a local db.cnf file.

To use your MySQL instance, just uncomment the key/value pairs in the DATABASES setting and add your DB details.

It will override the OPTIONS settings. At least, it does on my machine :).

## Menu Items
To make the dynamic image calls work, add these items exactly as they appear here to restaurant_menu table...
- Greek salad
- Grilled fish
- Bruschetta
- Lemon dessert

Note: there are no descriptions, and the prices can be whatever you want.

## Adding Items to the Menu
You can add anything you want.

Just note that all items displayed on Menu Items page, when you click an item link from the Menu page, show images from path static/img/menu_items/.

I have added images for three additional items if you want to see them on the website. Just add the title values as they appear here:).
- Kebab
- Pasta
- Salad

# API
If using new Insomnia (or maybe latest Djoser) be sure to see below section [Insomnia](#Insomnia)

Endpoints moved to 'api/' to avoid clashing with  template routing.

## GET
127.0.0.1:8000/api/restaurant/menu
127.0.0.1:8000/api/restaurant/menu/1
127.0.0.1:8000/api/restaurant/booking/tables
127.0.0.1:8000/api/restaurant/booking/tables/2024-11-01

## POST
127.0.0.1:8000/api/restaurant/menu/
BODY =  {
            "id": 1,
            "title": "Greek salad",
            "price": "7.00",
            "inventory": 25
        }

## PUT
127.0.0.1:8000/api/restaurant/menu/3/
BODY =  {
            "id": 1,
            "title": "Greek salad",
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

My Stuff
- Username: admin
- Email: admin@littlelemon.com
- Password: lemon@789!
- Token: 5756c74007a1852263f4e5001affc780d468be9b
  
Authenticated
Username: black_panther
Email: chadwick@littlelemon.com
Password: avengers24
Token: f737ca2b5dd76c7de163a7704f707a40459401d4

Customer CRUDs
Username: Bill
Password: myLemon@777



