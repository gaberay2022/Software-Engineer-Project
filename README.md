# Laser Tag Project 

A simulation of the original Photon lasertag system developed in 1984 by George A. Carter III. All source code, as well as the two background image files, is available via this repository. The mp3 files used during gameplay are located on a [seperate repository](https://github.com/Abraham-Mitchell/Abraham-Mitchell.github.io) and do not need to be downloaded in order to play during simulation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

List of required software to be able to run this application:
* Flask==2.2.2
* Jinja2==3.0
* Werkzeug==2.2.2
* gunicorn==20.1.0
* psycopg2==2.9.5


### Installing

A step by step series of examples that tell you how to get a development env running:

To install flask:`pip3 install Flask==2.2.2`

To install psycopg2:`pip3 install psycopg2==2.9.5`

  >If an error such as "Error: pg_config executable not found" is given,
  >the environment is missing necessary elements for successful installation.
  >> try instead: pip3 install psycopg2-binary

## Run Code/Configure Browser

To open repository on VScode: Follow [this guide](https://www.geeksforgeeks.org/how-to-open-a-github-repository-in-vs-code-online/)

To run code: `python3 main.py` or `flask --app main run`

Make sure to enable autoplay on your web browser so that audio can play during game play screen. 
 >[Enable on Safari](https://testgenius.com/help/safari-enable-auto-play-settings.pdf)


 >[Enable on Firefox](https://support.mozilla.org/en-US/kb/block-autoplay)


 >[Enable on Chrome](https://www.iheartradio.ca/100-3-the-bear/how-to-fix-autoplay-in-google-chrome-1.8728261)


 >>There may be some variation based on your browser version.

> Note, poor internet connection may cause audio files to not play. If this happens refresh brower or get better connection.

# How Website Functions
## Player Entry Screen
  ![Alt Text](/Readme_pictures/PlayerEntryScreen.png)
  Here in the Player Entry Screen, You would input the first, last, and code name for the individual. Then you will push the "Enter All Players" button to submit the people enterted to the database.

  Then, click on the "Lobby Creation Screen" button to go to the screen where you can set up lobbys or start games.

## Lobby Screen
  ![Alt Text](/Readme_pictures/LobbyScreen.png)
  Here in the lobby Screen, You will make up a key that you would like for you lobby, and then enter the codenames of the people that you would like to correspond with this lobby key. If you enter them into the Red border box, then they are on the Red team. If you enter them into the Green border box, then they will be on the green team.You would then push the "Enter All Players" button to store the lobby key with the players entered. 

  One thing to note: If you create a lobby with the same lobby key but different players, they will also appear in your game. This makes it so you can have an infinite number of players in your game, but be careful not to use a already created lobby key if you don't want to include those players in your game.

  Then you can enter you lobby key into the "Enter Lobby ID:" area and push start game to load your lobby. This lobby key will be saved to the players, and allows for people to come back and use the same lobby key to jump right back into a game, if they would like to.

  If you start the game without a lobby key, then it will load a game with everyone that is currently stored in the database. This is good if you want to make sure the system is working, and functions kind of as a default.

## Game play Screen
  ![Alt Text](/Readme_pictures/GamePlayScreenStartUp.png)
  Here we can see the people loaded into your game with your lobby key, and the 30 second warmup time before the game starts. At the 15 second mark, music starts to play with a countdown to when the game starts.

  ![Alt Text](/Readme_pictures/GamePlayScreenActive.png)
  Here we can see the game running. The team that is in the lead has their score flashing on screen. We also keep track of each individuals points for the game so that they can see the game running. If you hit someone you get 10 points, however, if you get hit you lose 10 points.

  You can see the feed of who shot who in the Play-by-Play box in the bottom right of the screen.

  For this implementation, we are using a traffick generator to randomly send information on who shot who.

  ![Alt Text](/Readme_pictures/GamePlayScreenOver.png)
  Here we can see that the team who won has their score flashing. A "Go to Lobby" button appears sending you back to the player entry screen to start the game again.

## Warning
  If you are hosting this on a website service, (we used heroku), The traffic generator will not work if more than one person is on the website. This happens due to the ports that the traffic generator is set up with, sending on the same port at all times, not randomly assigned ports for each instance.
# Authors

* **Gabriel Garcia** - *Team Lead* - *Full-stack* - [Gabriel-Garcia---Testing-Branch](https://github.com/gaberay2022/Software-Engineer-Project/tree/Gabriel-Garcia---Testing-Branch)
* **Ryan Cazares** - *Full-stack* - [RyanCazares](https://github.com/gaberay2022/Software-Engineer-Project/tree/main)
* **Abraham Mitchell** - *Front-end/UI* - [ATM-Test](https://github.com/gaberay2022/Software-Engineer-Project/tree/ATM-Test)
* **Lizbet Rivera** - *Front-end/UI* - [LizbetRivera](https://github.com/gaberay2022/Software-Engineer-Project/tree/main)
* **Marvin Violantes** - *Back-end/Database* - [MarvinBranch](https://github.com/gaberay2022/Software-Engineer-Project/tree/MarvinBranch)
* **Santiago Dorado** - *Back-end/Database* - [santiago-test](https://github.com/gaberay2022/Software-Engineer-Project/tree/santiago-test)
