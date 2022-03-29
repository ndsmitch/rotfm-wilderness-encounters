This provides a simple command for generating the day of wilderness encounters
from Rime of the Frostmaiden Chapter 2 (pg. 105)

# SETUP - run before generating and encounter
make bootstrap

# USAGE - generates an encounter
make encounter

# CLEANUP - delete the venv
make clean

## WITHOUT make - just run the commands yourself
```bash
python3.10 -m venv encounter.venv
encounter.venv/bin/python -m pip install --upgrade pip
encounter.venv/bin/python -m pip install dice==3.1.2
encounter.venv/bin/python encounter.py
```

## TIMING NOTE
The book provides these random encounter times
- morning = dawn to noon
- afternoon = noon to dusk
- evening = dusk to midnight
- night = midnight to dawn

I use the times from the day/night cycle instead:
- morning   -> morning  ->  1am to 10am
- afternoon -> twilight -> 10am to  2pm
- evening   -> night    ->  2pm to 11pm
- night     -> aurora   -> 11pm to  1am
