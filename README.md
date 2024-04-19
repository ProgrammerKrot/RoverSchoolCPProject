### Rover - School C&P Project

This repository contains my school project on Chemistry and Physics. Though not overly complex, it was quite engaging.

#### Installation Instructions:
1. Open or download the `main.py` file.
2. Manually retype or transfer the file to a compatible calculator via the [Texas Instruments website](https://www.ti.com/). **IMPORTANT!** Ensure the calculator supports Python.
3. Launch the program by navigating to Menu -> Execute -> Execute.

#### Program Instructions:
Upon launch, you'll encounter a menu where you can select from the following options:
- **1** - Labyrinth
- **2** - Shapes
- **3** - Avoider
- **4** - Drift

Let's explore each option:

**LABYRINTH**
Input movement commands from the following list:
- `f` - forward
- `r` - right
- `l` - left
- `b` - backwards

Commands can be combined (e.g., `fffrlb`) or entered individually. Press Enter after entering commands to start the robot's movement.

**SHAPES**
Start by entering the first letters of one of the three shapes:
- For a square: input height followed by width
- For a triangle: input the length of one side
- For a circle: try it yourself 😉

**AVOIDER**
Run the program and initiate the robot's movement by placing your hand approximately 10-15 cm in front of the sensors. Press `7` to stop the robot and exit the program. Note: On some calculators, use `ESC` to interrupt the program.

**DRIFT**
Simply run the program! Exit by holding down `ESC`.

**OTHER**
From any program except Avoider and Drift, you can return to the menu by entering "back."
To terminate the program, hold down `ESC` or enter `exit`.


Read license!

## Required Libraries

The following libraries are required to run the project:

- `ti_rover` embedded
- `ti_plotlib` embedded 
- `math` must be called manually
- `ti_system` embedded
- `time` must be called manually
- `random` must be called manually
