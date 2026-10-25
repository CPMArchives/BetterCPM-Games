# Snake

Snake game for CP/M and VT100/ANSI terminal

* First version (C) 2018, Karl A. Brokstad (www.z80.no)

* Turbo Pascal conversion and other mods with permission (C) 2018, linker3000 (linker3000-at-gmail-dot-com)

Version history:

* V1.2acn: 25-Jun-2020
  Changed keys to 2/4/6/8 and H/J/K/L and clear ANSI attributes on exit

* V1.2T: 21-Jul-2019
  Corrected Y boundary max in putFood.

* V1.1T: 14-Oct-2018
  Command line switch -m (monochrome) suppresses all colour codes
  Version numbering detached from Karl A. Brokstad's original

* V23N: 24-Sep-2018 First public release
  Game map used for collision detection and food position
  generation - this takes out several long loops.

Original GitHub repository: https://github.com/linker3000/Z80-Board
The first version can be found here: https://z80.no/projects/Pascal.html
 
## License

GPL v2, see the file COPYING

## Instructions

## Compiling

To compile SNAKE, just use Turbo Pascal from the ``TP/`` directory.
It's TP 3.0A for CP/M-80, only without the demo source code.

* Copy the TP files together with the SNAKE.PAS files to one disk
* The terminal definition is already set to ANSI and the speed is set to 8 MHz (for a
  standard RC2014), so running TINST is not needed
* Run Turbo Pascal using TURBO
* Set the compiler options to "compile -> Com-file" (press O, C, Q)
* Compile ``SNAKE.PAS``: press C (Compile), then enter ``snake`` as Work file name.

This should result in a ``SNAKE.COM`` file.


