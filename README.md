# Python mouse click automation

## Scope

- Automate clicks
- Input through a file
- Random deviation to click coordinates
- Files have a "setup" line at start
- Coordinate, random deviation
- Wait for color on cursor
- Wait a certain time
- Run action once, x times or until stopped

## Data files

### About

Data files (not final prefix) are used to store actions to be repeated.
These files start with a setup that set parameters and possibly runs commands, but only once.

### Syntax

Every command starts with the command name, and follows with parameters.
If command takes no parameters they are ignored. If command is not recognized the user is notified
and prompted if the program should continue or to stop.

Lines starting with `#` symbol are ignored.

Random deviation is always between `-random` and `random`. Random variation is calculated
separately for both x and y, but the range for both is always the same.

Implemented commands:

- `MOVE`
- `CLICK`
- `SLEEP`
- `ALERT`
- `WAIT COLOR`
- `EXECUTE`
- `KEY`

### `MOVE`

Moves mouse cursor to specified x, y coordinates. Possible to add random deviation
to coordinates.

#### Format

`MOVE`,`x`,`y`,`random`

### `CLICK`

Clicks mouse at specified x, y coordinates or at current position. Possible to add
random deviation to both actions.

#### Format

To click at current position
`CLICK`,`random`,`mouse`

To click at x, y coordinates
`CLICK`,`x`,`y`,`random`

To click at x, y coordinates with specified mouse button
`CLICK`,`x`,`y`,`random`,`mouse`

`mouse` specifies the mouse button to press. Possibilities:

- `left`
- `right`

### `SLEEP`

Delays the next action by specified amount. Amount is in milliseconds (1000 is 1 second).
Possible to add random deviation to delay, also in milliseconds.

#### Format

`SLEEP`,`delay`,`random`

### `ALERT`

Pauses the program and prompts the user whether to continue or stop.
Prompt is through a popup window and two buttons. Text of these buttons must be specified.

#### Format

`CONFIRM`,`continue`,`exit`

### `WAIT COLOR`

Waits until specified color is detected at coordinates. The time between checks
and color tolerance can be specified.

#### Format

`WAIT COLOR`,`x`,`y`,`r`,`g`,`b`,`tolerance`,`delay`

- `tolerance` specifies how close the RGB values have to be to the real one.
- `delay` is time in milliseconds between check of the coordinate.

`WAIT COLOR AT` has same syntax without `x` and `y`.
Command checks the color at current mouse location.

### `EXECUTE`

Starts the execution of specified script. Optional parameter for times the script is executed.

#### Format

`EXECUTE`,`filename`,`times`

### `KEY`

Presses specified keys in succession.

#### Format

`KEY`,`key`,`key`...
