
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

#  Binghamton Trail 
## CS110 B1 Final Project  Fall, 2024

## Team Members

Joshua Yoon

***

## Project Description

This Project is a life simulator representing Binghamton University. To succeed in the game, one must balance, eathing, studying and resting. The events that one goes through during their day will force students to adapt their behavior. 

## GUI Design

### Initial Design

![initial gui](assets/gui_init.png)

### Final Design

![final gui](assets/gui_final.png)

## Program Design

### Features

1. Study - this raises the stat for Grade but lowers hunger.
2. Eat - this raises the stat for hunger but lowers grade
3. rest - increases hunger but to a lesser extent than eat, provides a versitile option for when hunger and grade a both low.
4. Failed out of bing, this screen appears when the player's grade reaches 0 ending the game
5. Starved to death, this screen appears when the player's hunger reaches 0 ending the game.

### Classes

- 
State - locates what level(checkpoint) the player is on and applies damage to hugner or grade. This increases the difficulty of the game. Calculates whether bonus should be applied when debating whether the level should harm or benefit player.
GameIn - Set up variables of the GUI, interactions and concequenes.
LevelAt - applies set damages or benefits that occur at each level.
Player - holds the information for the player's stats, can also end the game depending on those stats. Also connects stats with actions that the player can take.
Key - manages the interaction of GUI actions and Play stats affecting the game.


## ATP

| Step                 | Procedure                                    | Expected Results                                   |
|----------------------|:--------------------------------------------:|-------------------------------------------------:|
| 1   Start the game   | Run the pygame.                                     | GUI window appears with "Binghamton Trail".      |
| 2   Click start      | Click the "Start Game" button.              | Transitions to the player name input screen.     |
| 3   Enter name       | Enter your name into the text box (e.g., "John"). | Name appears in the text box as typed.          |
| 4   Confirm name     | Press the "Enter" key.                      | Transitions to the main game screen.             |
| 5   Verify name      | Check if the player name is displayed.       | Name ("John") is visible on the main screen.     |


| Step                 | Procedure                                    | Expected Results                                   |
|----------------------|:--------------------------------------------:|-------------------------------------------------:|
| 1   Open stats       | Start the game and proceed to the main screen. | Player stats (Hunger: 100, Grade: 100) are displayed. |
| 2   Study            | Select "Study" at the first checkpoint.     | Hunger decreases by 20, grade increases by 30.   |
| 3   Eat              | Select "Eat" at the next checkpoint.        | Hunger increases by 30, grade decreases by 20.   |
| 4   Rest             | Select "Rest" at the next checkpoint.       | Hunger increases by 20, grade decreases by 10.   |
| 5   Verify stats     | Check if the updated stats are displayed.    | Updated hunger and grade stats appear correctly. |


| Step                 | Procedure                                    | Expected Results                                   |
|----------------------|:--------------------------------------------:|-------------------------------------------------:|
| 1   Open stats       | Start the game and proceed to the main screen. | Player stats (Hunger: 100, Grade: 100) are displayed. |
| 2   Deplete hunger   | Continuously select "Study" until hunger = 0.| Hunger decreases with each action.               |
| 3   Verify hunger    | Observe the stats as hunger approaches 0.    | Hunger decreases to 0.                           |
| 4   Game over        | Check if the game ends when hunger = 0.      | "Game Over" screen appears with "You starved!".  |
| 5   Restart game     | Restart the game.                            | Returns to the title screen.                     |


| Step                 | Procedure                                    | Expected Results                                   |
|----------------------|:--------------------------------------------:|-------------------------------------------------:|
| 1   Open event       | Start the game and proceed to the "9AM Gym Session" checkpoint. | Description of the checkpoint is displayed.      |
| 2   Take action      | Select an action (e.g., "Rest").             | Hunger decreases by 20.                          |
| 3   Replay           | Replay the checkpoint multiple times.        | Occasionally, grade decreases by 20 with an additional hunger loss of 20. |
| 4   Verify chance    | Check if probabilities align (20% chance).   | Outcomes match the described probabilities.      |
| 5   Next checkpoint  | Proceed to the next checkpoint.              | Transition to the next event successfully.       |


| Step                 | Procedure                                    | Expected Results                                   |
|----------------------|:--------------------------------------------:|-------------------------------------------------:|
| 1   Open checkpoints | Start the game and proceed through each checkpoint. | Hunger and grade stats update at each checkpoint. |
| 2   Make choices     | Make strategic choices to keep hunger and grade above 0. | No "Game Over" condition occurs.                |
| 3   Complete game    | Finish all checkpoints successfully.         | Stats are displayed at the end of the game.      |
| 4   Victory screen   | Check if the victory message appears.        | "You Graduated!" screen appears.                |
| 5   Restart game     | Restart the game.                            | Returns to the title screen.                     |

