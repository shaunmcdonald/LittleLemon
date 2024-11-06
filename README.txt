# LittleLemon

This is the Capstone project for the Meta Back-End Developer Professional Certification.

This certification included a lot of front-end tech, particularly JavaScript since it intersects with Django Template Language (the T in MVT).

Also, the Capstone only required one index.html template to prove integration skills.

However, I decided to include all the front-end templates here, since I had built them in previous assignments. In hindsight, I see why the Capston left them out.

The assignment asked for API endpoints on the path "restautant/*", which would conflict with the browsable paths to each template subpage.

This meant I had an out-of-scope learning experience getting the API to work with browse, not to mention authentication requirements to provision public and private access for each group.

In the end, it was worth it. I ultimately decided to prefix API endpoints with "api/*", which I think was the right choice regardless. 


# Python
Be sure to edit the PipFile to match your prederred Python Version or install your venv and import Pipfile packages separately.
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



