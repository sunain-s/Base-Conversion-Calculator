# Base-Conversion-Calculator
A base conversion calculator between binary, denary, hexadecimal, octal and BCD - made using Python3

## Requirements
- convert binary <==> denary and negative binary <==> denary
- convert hexadecimal <==> binary and hexadecimal <==> denary (negative hex not required)
- negative binary to be represented in user's choice between sign magnitude and two's complement binary
- negative binary could be displayed in one's complement
- conversions between denary, binary, hexadecimal, octal and BCD (binary coded decimal)
- denary, binary and hexadecimal addition and subtraction
- create a GUI for the calculator

## How to run and use
Run 'gui.py' and the window will appear, ESC can be used to return to main menu

**To Convert**
 - click the side button of the base you are converting from
 - then click the white strip next to the convert button
 - enter the digit and click convert

**To Add/Subtract**
 - click add/subtract button
 - select addition/subtraction type e.g. denary - hexadecimal
 - click input boxe on right and enter appropriate values
 - click calculate button


## What I learnt
 - how to convert binary, denary and hexadecimal <==>
 - how to represent and convert to and from negative binary using two's complement
 - how to represent and convert to and from octal
 - how to represent and convert to and from binary coded decimal (BCD)
 - how to add denary, binary and hexadecimal
 - how to subtract denary, binary and hexadecimal
 - how to create a clean GUI
 - using functional help() comment documentation
 - using comments to divide code into separate overall blocks

## Improvements
- Add a window that shows the process of working out results
- Currently has no input validation e.g. denary values can be entered for binary
- Slight error in Two's Complement conversion
  
  ==> 100 = -4, -0 is outputted
