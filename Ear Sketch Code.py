
# EarSketch project - Amira Abou Ali
# Informal comments by me (Amira) describing my thought process and where I adapted ideas.
# External ideas acknowledged inline (EarSketch guide, Hijaz maqam resources, makeBeat tutorials, etc.)

from earsketch import *

init()
setTempo(125)

# Track assignments 
# padTrack: background pads / makeBeat calls
# drumsTrack: core drum loops
# bassTrack: bass/sub
# synthTrack: melodic leads (Hijaz scale stuff)
# effectTrack: fills, cymbals, chords
# ethnic1/2/3: ethnic strings/percussion layers (kept on separate tracks so they can overlap)
# Layering technique inspired by EarSketch educational materials on track layering 
# and sound design (EarSketch Teachers, 2024; Georgia Tech Center for Music Technology, 2024).
# ambientTrack: ambient pad/long textures
# vocalTrack: vocal harmony clips
padTrack = 1
drumsTrack = 2
bassTrack = 3
synthTrack = 4
effectTrack = 5
ethnic1 = 6
ethnic2 = 7
ethnic3 = 8
ambientTrack = 9
vocalTrack = 10

# Beat / rhythms (makeBeat idea adapted from Music Tech / EarSketch tutorials) 
# Reference: Music Tech (2022) makeBeat pattern ideas + EarSketch how-to guide (EarSketch, 2025)
RNB_SYNTH = DUBSTEP_PAD_001
OS_CLAP = OS_CLAP01

beat_intro = "-0-0--00--0-00--0-00-0--00-"
beat_drive = "--00-0000-00--00-000--00-000"
beat_fill = "0-0-0-0-0-0000--0--0-0-000--"

# pad background as a rhythmic bed (keeps it on padTrack so it doesn't conflict with drums)
makeBeat(RNB_SYNTH, padTrack, 1, beat_intro)   # idea: padding the intro - (EarSketch how-to)
makeBeat(RNB_SYNTH, padTrack, 3, beat_fill)    # re-use pad for fills

# Groove Foundation (use dedicated tracks; no overlaps) 
fitMedia(HIPHOP_TRAP_BEAT_PART_013, drumsTrack, 2, 6)   # drums
fitMedia(HIPHOP_BASSSUB_001, bassTrack, 1, 9)          # bass/sub

setEffect(drumsTrack, VOLUME, GAIN, -2)   # soft drums
setEffect(bassTrack, VOLUME, GAIN, -3)    # lower bass level (mixing)

# Arabic-inspired Melody (Hijaz scale)
# My melodic idea (original): using small 1/4 measure steps to create ornamentation
# Reference/background on Hijaz maqam: MaqamWorld (2024), AMAR Foundation (2015), Ableton maqam notes
hijaz_scale = [0, 1, 4, 5, 7, 8, 11, 12]

# Main melodic movement (measures 1->5 area)
# I wrote this part — by playing around different combinations; ended up combining the scale forward 
# + reversed felt right for tension/release (my original)
for i, pitch in enumerate(hijaz_scale + hijaz_scale[::-1]):
    measure = 1 + i * 0.25
    fitMedia(RD_TRAP_BELLLEAD_1, synthTrack, measure, measure + 0.25)
    # Pitch shifting applied to the synth lead — use simple setEffect call (EarSketch syntax)
    setEffect(synthTrack, PITCHSHIFT, PITCHSHIFT_SHIFT, pitch)

# Harmonic layer (my addition to thicken the Hijaz feel)
for i, pitch in enumerate(hijaz_scale[::2]):
    measure = 5 + i * 0.5
    fitMedia(RD_CINEMATIC_SCORE_HARP_1, synthTrack, measure, measure + 0.25)
    setEffect(synthTrack, PITCHSHIFT, PITCHSHIFT_SHIFT, pitch - 12)

# Percussion Fill (transition to later sections)
# short repeated fills on effectTrack (keeps drums/synth separate)
for i in range(8):
    measure = 8 + i * 0.125
    fitMedia(YG_ALT_POP_MELODY_5, effectTrack, measure, measure + 0.125)
# Add reverb to the fill
setEffect(effectTrack, REVERB, REVERB_TIME, 80)

# Ethnic strings/percussion: play throughout late section (keeps Arabian vibe alive) 
# I decided to have them from measure 6 onwards so they underpin the entire build + ending.
# NOTE: they need distinct tracks to overlap freely (ethnic1/2/3) because you can't skip in EarSketch,
# found this out by playing around with how many lines of this i need to sound how i want it. 
# Reference: RD_WORLD_PERCUSSION_ETHNICSTRING_x loops discovered in EarSketch library (found these myself)
fitMedia("RD_WORLD_PERCUSSION_ETHNICSTRING_1", ethnic1, 6, 15)      # long layer 6->15
fitMedia("RD_WORLD_PERCUSSION_ETHNICSTRING_2", ethnic2, 6.25, 15.25) # slightly offset for texture
fitMedia("RD_WORLD_PERCUSSION_ETHNICSTRING_3", ethnic3, 6.5, 15.5)   # further offset
# Blend and space them out
setEffect(ethnic1, DELAY, DELAY_TIME, 0.3)
setEffect(ethnic2, DELAY, DELAY_TIME, 0.35)
setEffect(ethnic3, DELAY, DELAY_TIME, 0.4)
setEffect(ethnic1, REVERB, REVERB_TIME, 120)
setEffect(ethnic2, REVERB, REVERB_TIME, 130)
setEffect(ethnic3, REVERB, REVERB_TIME, 140)
# Slightly lower ethnic layers in the mix so they support rather than drown
setEffect(ethnic1, VOLUME, GAIN, -6)
setEffect(ethnic2, VOLUME, GAIN, -7)
setEffect(ethnic3, VOLUME, GAIN, -8)

# Ambient pad throughout intro -> build (long texture)
fitMedia(AK_UNDOG_OOHS_3, ambientTrack, 1, 16)
setEffect(ambientTrack, VOLUME, GAIN, -5)
setEffect(ambientTrack, REVERB, REVERB_TIME, 150)
setEffect(ambientTrack, PAN, LEFT_RIGHT, -50, 1, 50, 9)  # gentle auto-pan in intro

# Original ending section (kept, but moved to play after ethnic layers so its not so chunky in sound)
# original ending_scale (this is your old ending that you wanted back)
ending_scale = [12, 11, 9, 7, 5, 4, 2, 0]
final_start = 14.5   # starts after ethnic layers are already filling the space

# Make the ending synth louder and clearer than before (fix faintness)
for i, pitch in enumerate(ending_scale):
    measure = final_start + i * 0.125
    fitMedia(RD_TRAP_BELLLEAD_1, synthTrack, measure, measure + 0.125)
    # boost volume for each ending fragment so it sits above the ethnic bed
    setEffect(synthTrack, VOLUME, GAIN, 0, measure, 8, measure + 0.125)  # +8dB just for these short bits
    # Apply pitchshift in the simple form so it follows the clip automatically (EarSketch syntax)
    setEffect(synthTrack, PITCHSHIFT, PITCHSHIFT_SHIFT, pitch)

# Cymbal / chord emphasis over the ending (kept on effectTrack)
for i in range(8):
    measure = final_start + i * 0.25
    fitMedia(YG_ALT_POP_CHORDS_2, effectTrack, measure, measure + 0.25)

# Descending overlay (gentle) to extend the tail a bit (placed so it doesn't overlap earlier clips wrongly)
for i, pitch in enumerate(ending_scale[::-1]):
    measure = final_start + 1 + i * 0.25
    fitMedia(RD_TRAP_BELLLEAD_1, synthTrack, measure, measure + 0.25)
    setEffect(synthTrack, PITCHSHIFT, PITCHSHIFT_SHIFT, pitch)

# Vocals: subtle harmony to blend the end and fill gaps (keeps it sounding less abrupt)
# I use the Khalid harmony clips sparingly and on a dedicated vocalTrack and 
# orignally had it play with no breaks- sounded too crowded but this meant more lines to write.
# Reference: EarSketch library vocal loops
fitMedia(KHALID_NORM_VOX_HARMONY_1, vocalTrack, 1, 2)
fitMedia(KHALID_NORM_VOX_HARMONY_1, vocalTrack, 3, 4)
fitMedia(KHALID_NORM_VOX_HARMONY_2, vocalTrack, 5, 6)
fitMedia(KHALID_NORM_VOX_HARMONY_3, vocalTrack, 6, 7)
fitMedia(KHALID_NORM_VOX_HARMONY_3, vocalTrack, 8, 9)
# gentle vocal tail near the ending (placed after main ending begins)
fitMedia(KHALID_NORM_VOX_HARMONY_1, vocalTrack, final_start + 0.25, final_start + 1.25)  

setEffect(vocalTrack, VOLUME, GAIN, -4)
setEffect(vocalTrack, REVERB, REVERB_TIME, 180)
setEffect(vocalTrack, DELAY, DELAY_TIME, 60)

# Mastering & other fx
setEffect(synthTrack, REVERB, REVERB_TIME, 120)
setEffect(effectTrack, DELAY, DELAY_TIME, 50)

# The use of setEffect() with startValue, endValue over time to fade volume is based on
# the EarSketch effects tutorial (Nuevo Foundation, 2025) and the CEISMC EarSketch sound-effects lesson.
# My implementation here adapts that technique and making it original for the ending of my composition.
# Clean Fade-out: starts after everything (ensures ending plays fully) 
# final_end is when all final ending clips have finished
# not the happiest with this part as it does not flow as nicely as i want it too but it still 
# gives the extended instrumental effect old arabic songs have which is what i wanted
final_end = final_start + 2.5   # buffer covering the ending sequences
fade_start = final_end
fade_end = fade_start + 2.0

for t in [padTrack, drumsTrack, bassTrack, synthTrack, effectTrack, ethnic1, ethnic2, ethnic3, ambientTrack, vocalTrack]:
    # long fade out so it feels smooth; no overlap conflicts because tracks are distinct
    setEffect(t, VOLUME, GAIN, 0, fade_start, -40, fade_end)

finish()
