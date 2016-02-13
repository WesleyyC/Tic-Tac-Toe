Tic-Tac-Toe
===========

_We are currently working on a raspberry pi intergration to bring this virtual board game to an actual board game._

A perfect Tic Tac Toe player using the strategy in Newell and Simon's 1972 tic-tac-toe program (http://en.wikipedia.org/wiki/Tic-tac-toe#Strategy).

Feel free to play around with the code and let me know if there are any bugs.

Software Setup
--------------
### Python Version
Please make sure you are running Python 2 instead of Python 3.

### Run the standalone game without a Raspberry Pi

```shell
python <project>\original_code\tic_tac_toe.py
```shell

### Run the game on Raspberry Pi
	1. Open up terminal in Raspbian
	2. Start Python 2 shell with IDLE as Root so that you can access GPIO on the board

```shell
sudo idle &
```shell	

	3. Open up the project in an editer: File -> Open -> <project>\pi_interface.py
	4. Inside the editer, hit F5 to run!


Hardware Setup
--------------
We are currently setting up and connecting the game board using a breadboard and jumper wires. After we are done debugging, we will see if we can get a PCB and solder the components in!

### Circuit Components
|Component|Count|
|---|---|
|Bi-color LEDs|9|
|push buttons|3|
|Resisotr ~330 Ohm|1|
|Jumper wires|At least 19|

### Circuit Schematics
_Coming soon..._



Most of the code is finished in less than three hours, so there are a lot of if/else statment and not perfectly structured. So pardon me for the mess and feel free to fork/modify the code.
