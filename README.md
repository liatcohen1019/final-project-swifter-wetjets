:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Covid detector
## CS 110 Final Project
### spring, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

https://replit.com/join/jumymivwzd-liatcohen1019)

<< [link to demo presentation slides](#) >>

### Team:  Swifter WetJets 
####  Liat Cohen, Nick Bell, Ben Uline 

***

## Project Description *(Software Lead)*

Our project takes a list of symptoms and depending on which symptoms are inputted by the user, it will flash red or green depending if the symptoms indicate you should get tested for covid and take further procausions. 
***    

## User Interface Design *(Front End Specialist)*
#####PICTURE OF OUR LOADING/START SCREEN#####
 - This is the start menu
####FIRST CONCEPT MAP####
- This is the first design concept of the map
####SCREENS THROUGHOUT PROGRAM + EXPLANATION FOR EACH#####
#####FI
The first screen in the program will be a list of symptoms
The second screen will be flashing red or green depending on if thr results look positive or negative. 
The last screen will be instructions on how to get further care depending on your results. 
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design *(Backend Specialist)*

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. >>
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
         * https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/Interface%20Photo.png
* Classes
   * https://replit.com/@Liatcohen1019/final-project-swifter-wetjets#assets/Structue%20Photo.png

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:

* main.py
* src
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*

   * You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Ben Uline 
worked on the code and decoding any bugs as well as making it more advanced.

### Front End Specialist - Nick Bell
Did research on the medical part of the project in figuring out what symptoms we wanted to encorperate in the program and what the recommendations are at the end. 

### Back End Specialist - Liat Cohen 
Made sure everything was organized and submitted on time. Was in charge of organizing group meeting as well as creating the idea for the program. 

## Testing *(Software Lead)*

* << Describe your testing strategy for your project. >>
    * << Example >>

## ATP
Step number
A:Procedure
B:Expected Results
C:Actual Result

1a. press run 
1b. game should start
1c. no results yet 

2a. press c for c4 
2b. Location will change to dunkin, NO COVID
2c. no results yet 

3a. If dunkin is selected, press l key to go to library 
3b. Location will change to c4, NO COVID
3c. no results yet 

4a. If dunkin is selected, press u key to go to undergrounds
4b. Location will change to library, NO COVID
4c. no results yet 

5a. If c4 is selected, press g to go to gym 
5b. Location will change to undergrounds, NO COVID
5c. no results yet 

6a. If c4 is selected, press t to go to track
6b. Location will change to gym, 50% chance of COVID, game will end if covid is caught
6c. no results yet 

7a. If library is selected, press a to go to academic A 
7b. Location will change to track, NO COVID
7c. no results yet 

8a. If library is selected, press l to go to lake taco
8b. Location will change to Academic A, COVID, game is lost
8c. no results yet 

9a. If undergrounds is selected, press h to go to lecture hall 
9b. Location will change to lake taco, NO COVID, game is won
9c. no results yet 

10a. If undergrounds is selected, press n to go to nature preserve 
10b. Location will change to lecture hall, COVID, game is lost
10c. no results yet

11a. If gym is selected and no covid was caught, press j to go to Jazzmans  
11b. Location will change to nature preserve, NO COVID, game is won
11c. no results yet 

12a. If gym is selected and no covid was caught, press s to go to Starbucks  
12b. Location will change to Jazzmans, NO COVID, game is won
12c. no results yet 

13a. If track is selected, press e to go to the events center 
13b. Location will change to Starbucks, COVID, game is lost
13c. no results yet 

14a. If track is selected, press h to go to the hinman
14b. Location will change to Events Center, NO COVID, game is won
14c. no results yet 

15a. If track is selected, press h to go to the hinman
15b. Location will change to Hinman, COVID, game is lost
15c. no results yet 