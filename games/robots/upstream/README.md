# Robots

Robots is a turn-based game for CP/M.

It's based on ROBOTS, a BSD game (but no source code was taken from it).

The objetive of the robots is only one: to kill you.

The only thing you can do, is to try to escape from them. But use the teletransportation with care: you have only a few teletransport tickets!

The robots will die if they collide between them or crash against something.

That's your only opportunity to win the robots.

Good luck!

Copyright (c) 2015 Miguel García / FloppySoftware

A 'clear screen' function (VT100) has been added by me (Anna Christina Naß <acn@acn.wtf>.

Original Repository: https://github.com/MiguelVis/RetroProjects
Website: http://www.floppysoftware.es/robots.html?path=cpm_projects|robots

The file ``ROBOTS.COM`` is the compiled game file.

## Commands

Move the player ``.P.`` using the numpad numbers as shown on the screen.
Press T for teletransportation and Q for quit.

## Compile:

To compile, use MESCC, "Mike's Enhanced Small C Compiler".
See: http://www.floppysoftware.es/mescc.html?path=cpm_projects|mescc

In the directory ``mescc``, I provide the files neccessary to compile Robots, using:

    CC ROBOTS
    CCOPT ROBOTS
    ZSM ROBOTS
    HEXTOCOM ROBOTS

Note that only the really neccessary files are provided - see the link above for the full MESCC compiler and source code!

## License:

GPL Version 2, see copying.txt - valid for MESCC and Robots.

