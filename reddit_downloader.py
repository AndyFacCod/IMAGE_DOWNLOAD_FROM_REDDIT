import praw  # Importă biblioteca PRAW, care permite interacțiunea cu API-ul Reddit (pip install praw)
import requests  # Importă biblioteca requests, care permite descărcarea imaginilor de pe internet (pip install requests)
import os  # importăm biblioteca os pentru a manipula căile de fișiere și directoare

# https://www.reddit.com/prefs/apps

CLIENT_ID = 'XXXX' # personal use script
CLIENT_SECRET = 'xx-xx' # secret
USER_AGENT = 'AppName/1.0.0 by autor (https://www.reddit.com)' #'AppName/1.0.0 by autor (link autor)'


# Numarul de poze care doresti sa fie descarcate
NUMBER_OF_DOWNLOADS = 5

# Subredditul de unde vei descarca
SUBREDDIT_SELECT = 'memes'


# Creează o instanță a obiectului Reddit, care se autentifică cu credențialele specificate
reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)

# Selectează subreddit-ul "SUBREDDIT_SELECT" pentru a descărca imagini de acolo
subreddit = reddit.subreddit(SUBREDDIT_SELECT)

# Pentru a putea numerota pozele descarcate
numerotare = 1

# Pentru primele "NUMBER_OF_DOWNLOADS" imagini cele mai populare din subreddit, face următoarele lucruri
for submission in subreddit.hot(limit=NUMBER_OF_DOWNLOADS):

    # Verificăm dacă postarea este o imagine
    if submission.post_hint == "image":

        # Obține numele utilizatorului care a postat imagini
        author_name = submission.author.name
            
        # Creează numele fișierului prin concatenarea numelui utilizatorului și numărului aleatoriu
        file_name = f"{numerotare}_{author_name}.jpg"
        
        # Obține URL-ul imaginii din "SUBREDDIT_SELECT"
        image_url = submission.url
        
        # Descarcă conținutul imaginii de la URL-ul specificat
        image_content = requests.get(image_url).content

        # Salvează conținutul imaginii într-un fișier cu numele specificat
        with open(file_name, 'wb') as handler:
            handler.write(image_content)
        
        # Crestem numerotartea imaginilor
        numerotare = numerotare+1
        
# Verifică dacă există deja un director numit SUBREDDIT_SELECT în locul unde rulezi acest script
if not os.path.exists(SUBREDDIT_SELECT):
    os.makedirs(SUBREDDIT_SELECT)

# Mută toate imaginile salvate în directorul SUBREDDIT_SELECT
for file_name in os.listdir():
    if file_name.endswith('.jpg'):
        os.rename(file_name, f"{SUBREDDIT_SELECT}/{file_name}")  
