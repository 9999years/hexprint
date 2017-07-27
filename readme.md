# hexprint

Text to bytes!

    $ hexprint 40 20 41 42 43 60 50
    @ ABC`P

Or, identically:

    $ hexprint 40204142436050
    @ ABC`P

An actual use case, to reset an ESC/POS printer:

    $ hexprint 1B40 | lpr -l
