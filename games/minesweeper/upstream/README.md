# Find That Mine!

A MineSweeper clone game for CP/M

VT100 color version by Anna Christina Naß <acn@acn.wtf>

Based on v2.0 - 07 April 2020.

Copyright (c) 2012-2020 Miguel Garcia / FloppySoftware, Spain.

The original repository can be found here:
https://github.com/MiguelVis/ftm

## Introduction

This is a clone (yes, one more!) of MineSweeper for CP/M with supported CRTs,
derived from the plain CP/M version (and itself from the Amstrad PCW
& Samaruc GUI version).

It should run in any version of the CP/M operating system and a Z80 CPU.

This version is patched to work with a VT100 terminal only and it uses
color ANSI codes.

## The game

The aim of the game is to find all the mines on the board, putting a flag on
them and uncovering the other squares.

If you uncover a mine, you lose the game.

There are three different levels:
* Level 1 : 08 x 08 squares, 08 mines
* Level 2 : 08 x 12 squares, 12 mines
* Level 3 : 08 x 16 squares, 16 mines


## How to play

In the board, a number on a square means the quantity of mines around it.

To uncover a square, you must enter a command telling its position as row and column - ie:
```
1C
```

To put or remove a flag on a square, you must append a F character to the command - ie:
```
3DF
```

## Technical notes

To compile, use MESCC, "Mike's Enhanced Small C Compiler".
All files neccessary (and only these) to compile the game are included.
The complete package of MESCC can be found in its repository:

https://github.com/MiguelVis/mescc

Compile it using:

    CC FTM
    CCOPT FTM
    ZSM FTM
    HEXTOCOM FTM

The game uses Codepage 437 border characters as default, if your terminal
cannot display these, remove ```#define CP437``` from FTM.C and recompile it.

## License

This software is copyright of Miguel Garcia / FloppySoftware, Spain. All rights
reserved.

This program is freeware, and it's licensed under the GNU General Public License.

See the license file for more details.

