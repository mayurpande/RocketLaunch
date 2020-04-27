# Did the rocket launch yet?

> A telegram bot that shows image frames of a video to a user to determine if the rocket has launched yet

Using the Telegram Bot the user is prompted with images from the FrameX API.

The user is asked to reply "y" or "n" depending on if the rocket has been launched yet. 

The bot should be able to determine the frame that occurred first using a bisection algorithm

In order to see live working version go to download telegram bot from https://desktop.telegram.org/ and search for
@rocket_launcher. Or if you prefer to run locally follow below.
  
## Development setup 

First download Telegram bot from https://desktop.telegram.org/ and save API token into config.cfg file

Create a `config.cfg` file with:
```
[creds]
token = <your token here from api>
```

In order to clone repo and run locally:

Create a virtual environment within the repo and then install `requirements.txt`: 

``` 

user@pc~RocketLaunch/$ python3 -m venv env 

user@pc~RocketLaunch/$ source env/bin/activate 

(env) user@pc~RocketLaunch/$ pip install -r requirements.txt 

(env) user@pc~RocketLaunch/$ python app.py

``` 

Windows: 


Create a virtual environment within the repo and then install `requirements.txt`: 

``` 

C:\Users\your_user\Documents\RocketLaunch\>py -m venv env 

C:\Users\your_user\Documents\RocketLaunch\>env\Scripts\activate.bat 

(env) C:\Users\your_user\Documents\RocketLaunch\> pip install -r requirements.txt 

(env) C:\Users\your_user\Documents\RocketLaunch\> python app.py

``` 

Then open up telegram bot and run the bot.


## Release History 

* 0.0.2




