
# CS110 Project Proposal
# Covid detector
## CS 110 Final Project
### spring, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

https://replit.com/join/jumymivwzd-liatcohen1019)

(https://docs.google.com/presentation/d/1vwqP2-0hIBFreUQL4tdRT4s9ETI6xdBjCFeCY3cmcqU/edit?usp=sharing)

### Team:  Swifter WetJets 
####  Liat Cohen, Nick Bell, Ben Uline 

***

## Project Description *(Software Lead)*

Our project takes you on a tour of the amazing Binghamton campus, while covid 19 is at its peak. while going through campus, you must decide which places to go and try and avoid contracting covid on your way. If you get covid, the game is over and you must start from the begining. 
***    

## User Interface Design *(Front End Specialist)*
https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/start_screen.jpg
* This is the start menu

https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/web.png
* This is the first design concept of the map. Showing the web of choices. 

https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/game_screen.jpg
* This is the screen of game in progress after succussfully reaching to next round.

https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/no_covid.jpg
* This is the screen of the game after selecting correct location without covid.

https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/yes_covid.jpg
* This is the screen of the game after selecting the incorrect location, thus receiving covid.

https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/game_over.jpg
* This is the screen displayed after playing game and receiving covid, stating that the game is over.

https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/game_win.jpg
* This is the screen displayed after playing game and not receiving covid, stating player won game.

#####
The first screen in the program will be blue with the choice of where you want to go when you leave your dorm. 
As the game prgressses from here, it takes you along different blue slides with locations and either green or red slides with information whether you dodged covid or not. 
Once you hit a red screen, that means that you have contracted covid and the game is over. 


## Program Design *(Backend Specialist)*

* Non-Standard libraries

  * Pygame
  * [https://www.pygame.org/docs/]
  * Pygame is a set of module which is designed for creating controllable and operational video games in python.

* Class Interference Design
  * This is the older class interface
  * https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/class_diagram.jpg
  * This is the newer class interface
  * <<link

  
* Class Interface Design
         * https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/Interface%20Photo.png
* Classes
   * https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/Structue%20Photo.png

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:

* main.py
* src
    * negcovid.py
    * poscovid.py
    * sample_controller.py
* assets
    * class_diagram.jpg
    * image.png
    * InterfacePhoto.png
    * negcovid.png
    * poscovid.png
    * StructurePhoto.png
    * web.png
* etc
    * foldercontexts.txt

***

## Tasks and Responsibilities *(Software Lead)*

### Software Lead - Ben Uline 
Worked on ensuring both Frontend and Backend work when put together, ensuring code was done swiftly (pun intended). Fixed bugs and issues with code. 

### Front End Specialist - Nick Bell
Worked on GUI and visuals of project, such as rough draft outcomes-web. Conducted research on possible medical situations. 

### Back End Specialist - Liat Cohen 
Responsible for bulk of initial code, as well as initiating the original idea. Set up meeting times for the group, ensuring work was submitted on time. 

## Testing *(Software Lead)*

* We made sure that our code works by first, making sure no unexpected errors were occurring. We then made sure each component of the code worked together. As we tested the code, we recorded each step in the ATP, checking to see if we got the results we expected. 
    * For example, we played the game until we "beat" the game, getting through it without receiving covid, as well as playing the game until we got covid. We made sure the apropriate sceens popped up for each scenario. 

## ATP
Step | Procedure | Expected Results | Anticipated Results
--- | --- | --- | ---
1 | Press run | game should start | no results yet 
2 | press c for c4 | Location will change to dunkin, NO COVID | no results yet 
3 | If dunkin is selected, press l key to go to library | Location will change to c4, NO COVID | no results yet 
4 | If dunkin is selected, press u key to go to undergrounds | Location will change to library, NO COVID | no results yet 
5 | If c4 is selected, press g to go to gym | Location will change to undergrounds, NO COVID | no results yet 
6 | If c4 is selected, press t to go to track | Location will change to gym, 50% chance of COVID, game will end if covid is caught | no results yet 
7 | If library is selected, press a to go to academic A | Location will change to track, NO COVID | no results yet 
8 | If library is selected, press o to go to lake taco | Location will change to Academic A, COVID, game is lost | no results yet 
9 | If undergrounds is selected, press l to go to lecture hall | Location will change to lake taco, NO COVID, game is won | no results yet 
10 | If undergrounds is selected, press n to go to nature preserve | Location will change to lecture hall, COVID, game is lost | no results yet
11 | If gym is selected and no covid was caught, press j to go to Jazzmans | Location will change to nature preserve, NO COVID, game is won | no results yet 
12 | If gym is selected and no covid was caught, press s to go to Starbucks | Location will change to Jazzmans, NO COVID, game is won | no results yet 
13 | If track is selected, press e to go to the events center | Location will change to Starbucks, COVID, game is lost | no results yet 
14 | If track is selected, press e to go to the events center | Location will change to Events Center, NO COVID, game is won | no results yet 
15 | If track is selected, press h to go to the hinman | Location will change to Hinman, COVID, game is lost | no results yet 