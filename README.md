# myawesomerpoject

# Arabian Soundscape
> A creative Python-coded musical composition that merges the Arabic Hijaz maqam with modern trap and R&B rhythms.  

Table of Contents

[General Info](#general-information)

[Technologies Used](#technologies-used)

[Features](#features)

[Screenshots](#screenshots)

[Setup](#setup)

[Usage](#usage)

[Project Status](#project-status)

[Room for Improvement](#room-for-improvement)

[Acknowledgements](#acknowledgements)

[Contact](#contact)

## General Information
Arabian Soundscape is an audio-coding project developed using EarSketch (Python).  
It explores whether code can express cultural emotion, specifically tarab which is the feeling of musical ecstasy found in Arabic performances by artists such as Fairouz and Umm Kulthum.

The composition merges:
- Hijaz maqam scale structures, coded algorithmically through Python lists and pitch shifts.  
- Trap and R&B rhythmic design, built using the `makeBeat()` function.  
- Cultural storytelling through sound, using logic, loops, and conditionals to evoke emotion.  

This project was created for the UTS Creative Coding (52685) subject to demonstrate code literacy through culturally grounded composition.

## Technologies Used
- EarSketch - v3.0 (GA Tech Center for Music Technology, 2025)
- Python – v3.x (Python Software Foundation, 2025)
- Nuevo Foundation Workshops – 2024 (effects & tempo automation)
- Music Tech Tutorial – 2022 (`makeBeat()` sequencing)
- Ableton Maqam Presets – 2024 (by Sami Abu Shumays)
- MaqamWorld & AMAR Foundation – for Hijaz scale theory and tarab context

## Features
- Coded Rhythm Bed: Text-based beat patterns using `0 = hit` and `– = rest`.
- Algorithmic Melody: Hijaz scale implemented as ascending + descending lists with `enumerate()` and `[::-1]`.
- Offset Ethnic Layers: Three overlapping string tracks at 6 / 6.25 / 6.5 measures to simulate ensemble timing.
- Spatial Effects:`setEffect()` reverb (120–140) and delay (0.3–0.4) values for atmospheric depth.
- Automated Fade-Out:** A final loop gradually reduces volume across all tracks for a seamless outro.

## Screenshots

## Setup
Requirements 
- Browser access to [EarSketch](https://earsketch.gatech.edu/)
- No installation required

Steps:
1. Open EarSketch and select Python mode.
2. Copy the code from 'AMIRAS WEIRD SOUND .py' into the editor.
3. Click Run to render and hear the composition.

## Usage
The project demonstrates how Python logic produces music.

```python
makeBeat(RNB_SYNTH, padTrack, 1, beat_intro)
for i, pitch in enumerate(hijaz_scale + hijaz_scale[::-1]):
    measure = 1 + i * 0.25
    fitMedia(RD_TRAP_BELLLEAD_1, synthTrack, measure, measure + 0.25)
    setEffect(synthTrack, PITCHSHIFT, PITCHSHIFT_SHIFT, pitch)
```

- The `makeBeat()` function builds rhythmic foundations using text-based symbols.  
- The `for` loop iterates through the Hijaz scale, spacing notes every 0.25 measure.  
- `setEffect(...PITCHSHIFT...)` transposes each note, following Hijaz tonal intervals.

This layering technique lets the music rise, fall, and return like Arabic phrasing, showing how sound logic can recreate emotion.

## Project Status
Project is: ✅ Complete

The composition meets its original goal: to test whether Arabic musical emotion (*tarab*) can be achieved through algorithmic code inside EarSketch.

## Room for Improvement
Future enhancements:
- Add custom audio samples recorded by Middle Eastern musicians.
- Use conditional statements for dynamic transitions between sections.
- Experiment with MIDI integration and live input recording.

To do:
- Explore maqam variations beyond Hijaz (e.g., Bayati or Nahawand).
- Extend the project into a visual sound installation.

## Acknowledgements
This project was inspired by Arabic musical traditions and the idea that **code can carry emotion.**  
It draws on both technical and cultural sources, including:
- EarSketch Teachers (2024) – layering and sound design guidance
- Nuevo Foundation (2025) – automation tutorials
- Music Tech (2022) – rhythm and sequencing concepts
- MaqamWorld (2024) and AMAR Foundation (2015) – maqam theory and performance insights

Special thanks to my peers Keshia M. and Sophia L. for constructive feedback throughout the process.

## Contact
Created by Amira Abou Ali
[amira.abouali@student.uts.edu.au](mailto:amira.abouali@student.uts.edu.au)  
Bachelor of Communication (Social & Political Science / Digital Media), UTS  

References (APA 7th Edition)
Ableton. (2024).
Maqam tuning presets for Live 12 (by Sami Abu Shumays) [Software preset]. https://tuning.ableton.com/arabic-maqam/maqam-guide/  
AMAR Foundation. (2015). The Hijaz maqam. https://www.amar-foundation.org/098-the-hijaz-maqam/  
EarSketch. (2025). EarSketch [Computer software]. Georgia Institute of Technology. https://earsketch.gatech.edu/  
EarSketch Teachers. (2024). About us. EarSketch Educator Community. https://teachers.earsketch.org/about-us  
Georgia Tech Center for Music Technology. (2024). EarSketch: Teaching coding through music. https://gtcmt.gatech.edu/earsketch  
MaqamWorld. (2024). Maqam Hijaz. https://maqamworld.com/en/maqam/hijaz.php  
Music Tech. (2022). Pattern sequencing with makeBeat in EarSketch (Part I) [Video]. YouTube. https://www.youtube.com/watch?v=fQRlVfSq3Uo  
Nuevo Foundation. (2025). Set tempo & add sounds (Python EarSketch). https://workshops.nuevofoundation.org/python-earsketch/activity-1-set-tempo-add-sounds/  
Python Software Foundation. (2025). Python (Version 3.x) [Computer software]. https://www.python.org/  
Danielson, V. (1997). The voice of Egypt: Umm Kulthūm, Arabic song, and Egyptian society in the twentieth century. University of Chicago Press.  

## Credit
This README structure and formatting are based on:  
Łyczywek, R. (2018, October 15). How to write a good README for your GitHub project? Bulldogjob. https://bulldogjob.com/readme/how-to-write-a-good-readme-for-your-github-project  
ritaly. (2018). GitHub – ritaly/README-cheatsheet: Template for a clear GitHub README (markdown). GitHub. https://github.com/ritaly/README-cheatsheet

