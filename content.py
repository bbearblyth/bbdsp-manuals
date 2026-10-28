# The words of the manual. build.py turns this into the pages in docs/.
#
# Each control row is (NAME, range, default, what it does).
# Names are written as they appear on the plugin's panel.

KINDS = {
    "fx":    "AUDIO FX",
    "inst":  "INSTRUMENT",
    "midi":  "MIDI FX",
    "mfx":   "MIDI-CONTROLLED FX",
}

PLUGINS = [
# ---------------------------------------------------------------------------
dict(
    slug="pipeline", name="PiPELiNE", accent="#F6AE28", kind="midi", motion="pipe",
    tagline="A modular MIDI chain. Stack cards, and every note flows through them in order.",
    intro=[
        "PiPELiNE is a chain of MIDI tools. Each tool is a card: an arpeggiator, a strummer, a harmoniser, "
        "an LFO that draws CC curves, a melody generator, and more. Notes enter at the top-left card, pass "
        "through each card in turn, and leave for your instrument.",
        "Because the order matters, the same cards can do very different jobs. A harmoniser before an "
        "arpeggiator arpeggiates the harmony; after it, every arpeggiated note gets its own harmony.",
    ],
    images=[("pipeline_cards.webp", "Every card open at once. Each card's colour marks what it is doing right now.")],
    quick=[
        "Put PiPELiNE in the MIDI FX slot of a software instrument track.",
        "Add cards and turn each one ON. Cards that are off pass notes straight through.",
        "Play. Each card's animation shows what it is doing to your notes.",
        "Press MIN on a card to fold it down to just its animation.",
    ],
    how=[
        ("Order is everything", "Notes are processed card by card, left to right, top to bottom. Re-order cards to change the result."),
        ("Locked to the host", "Anything rhythmic (repeats, arps, Euclidean patterns, sequencers, LFOs) follows the host's tempo and bar position, so it stays in time when you start playback mid-song."),
        ("Drag out MIDI", "Generators with a DRAG button (Brownian, Melodifier) let you drag what they made straight into your arrangement as a MIDI region."),
        ("CC output", "LFO, Envelope and Step Sequencer can send MIDI CC, pitch bend or channel pressure. In Logic these reach the instrument on the same track only."),
    ],
    groups=[
        ("NOTE CARDS", [
            ("INPUT", "C-2 to G8", "full", "Sets the key range PiPELiNE listens to. Notes inside the range go down the chain; notes outside skip it."),
            ("NOTE REPEATER", "1/1 to 1/64", "-", "Repeats each note at the chosen division. REPEATS, VEL RAMP and PITCH RAMP make the repeats fade, swell or climb."),
            ("RANDOMISER / TRANSPOSER", "0-100%", "-", "Remaps an input range to an output range and snaps the result to a key and scale. RANDOMISE AMOUNT adds controlled chaos."),
            ("CHORD TRIGGER", "-", "-", "One finger plays a whole chord in a key and style. Switch to PROGRESSION SEQUENCER to step through a progression."),
            ("HARMONIZER", "-", "-", "Adds up to two harmony voices (VOICE A / VOICE B) in key. ORIGINAL keeps or drops the note you played."),
            ("STRUMMER", "-", "-", "Spreads a chord out like a strum, UP, DOWN or RANDOM. NOTE GAP, ACCEL and VEL RAMP shape the strum."),
            ("ARPEGGIATOR", "-", "-", "Up, Down, Up-Down, Down-Up, As Played, Random or Chord patterns over 1-4 octaves, with GATE, SWING and HOLD."),
            ("QUANTIZER", "-", "-", "Pulls note timing towards a grid. STRENGTH sets how hard."),
            ("GLITCH", "-", "-", "Randomly stutters notes on a grid. CHANCE, RAMP, PITCH jumps and GATE set how wild it gets."),
        ]),
        ("GENERATORS", [
            ("BROWNIAN", "-", "-", "A random walk of notes in a key. BIAS leans it up or down, MAX STEP limits the leap, and LENGTH loops the walk every few bars."),
            ("MELODIFIER", "-", "-", "Draw or load a phrase in the piano-roll grid, then play it from held notes. EVOLVE and VARY change it a little every pass."),
            ("EUCLIDEAN", "-", "-", "Five lanes of evenly spread rhythms. Each lane has STEPS, HITS, ROTATE and its own note."),
        ]),
        ("EXPRESSION CARDS", [
            ("GLIDE", "-", "-", "Portamento between notes, as pitch BEND or RETRIGGER, with a curve and per-voice channels."),
            ("VIBRATO", "-", "-", "Per-note vibrato over MPE. DELAY and FADE let it creep in; HUMANIZE keeps the voices apart."),
            ("TUNER", "-", "-", "Plays in other tunings (just intonation and more) by bending each voice on its own channel."),
            ("LFO", "-", "-", "A free or synced wave sent as CC, pitch bend or pressure. LEARN maps it to a target."),
            ("ENVELOPE", "-", "-", "A drawn breakpoint shape fired by each note, sent as CC, pitch bend or pressure."),
            ("STEP SEQUENCER", "-", "-", "A bar of steps that gates velocity, notes or sends CC each step."),
        ]),
    ],
    tips=[
        "Strummer straight after Chord Trigger turns one finger into a strummed guitar part.",
        "Brownian into Quantizer into Harmonizer makes endless in-key counter-melodies.",
        "MPE cards (Glide, Vibrato, Tuner) need an instrument that accepts one note per channel.",
    ],
    specs=[("Type", "MIDI FX (AU MIDI processor), VST3, Standalone"), ("Input", "MIDI"), ("Output", "MIDI, CC, pitch bend, pressure")],
),
# ---------------------------------------------------------------------------
dict(
    slug="prism", name="PRiSM", accent="#3D86D9", kind="mfx", motion="prism", dark=True,
    tagline="Sing in. Play chords. Every held note re-sings your voice, hard-tuned and spread wide.",
    intro=[
        "PRiSM is a vocal harmoniser driven by MIDI. Your voice comes in on the side chain; the chords you play "
        "decide the notes. Each held key becomes a new copy of your voice, tuned exactly to that pitch and placed "
        "across the stereo field, so a single take turns into a choir that follows your hands.",
        "The CRYSTAL tone rebuilds each voice from pure harmonics shaped by your vowels, for a clean, glassy "
        "sound. GRAIN keeps more of the original recording's texture.",
    ],
    images=[("prism_expanded.webp", "The full panel. Each voice is a curtain of light in the prism below."),
            ("prism_light.webp", "A chord in flight: one colour per voice.")],
    quick=[
        "In Logic, create a Software Instrument track and load PRiSM in the INSTRUMENT slot (AU MIDI-controlled Effects).",
        "In the plug-in window's header bar, choose your vocal track from Logic's Side Chain menu.",
        "Play the vocal and hold chords on the instrument track.",
        "Use LEAD to keep your own voice (DRY or TUNED) on top of the chord, or OFF for chord voices only.",
    ],
    how=[
        ("Voice from the side chain", "PRiSM listens to the side-chain input, not the track it sits on. The track itself only supplies the MIDI."),
        ("Pure tuning", "TUNING JUST tunes the chord voices to pure intervals against each other, so they ring together without beating."),
        ("No dropouts", "The CRYSTAL voices follow the loudness of your voice rather than a pitch tracker, so breathy or quiet singing does not drop out."),
    ],
    groups=[
        ("TOP ROW", [
            ("LEAD", "OFF / DRY / TUNED", "TUNED", "Your own voice on top. DRY passes it untouched; TUNED snaps it to the nearest held note."),
            ("OCTAVE", "-2 to +2", "0", "Moves every chord voice up or down in octaves."),
            ("TONE", "CRYSTAL / GRAIN", "CRYSTAL", "How the voices are made: rebuilt from harmonics, or re-pitched from the recording."),
            ("TUNING", "JUST / EQUAL", "JUST", "Pure intervals between the voices, or standard equal temperament."),
            ("HOLD", "ON / OFF", "OFF", "Keeps the last chord sounding after you let go of the keys."),
        ]),
        ("KNOBS", [
            ("RETUNE", "0-200 ms", "0", "How fast each voice snaps to its note. 0 is the hard, robotic snap."),
            ("HUMAN", "0-100%", "0", "Lets a little of your natural pitch movement back in."),
            ("FORMANT", "-12 to +12 st", "0", "Shifts the vowel character without changing pitch."),
            ("GLIDE", "0-500 ms", "40", "Slides voices between notes when the chord changes."),
            ("DETUNE", "0-50 ct", "0", "Spreads the voices slightly out of tune for width."),
            ("SPREAD", "0-100%", "70", "How wide the voices are placed in stereo. The lowest voice stays centred."),
            ("LEAD VOL", "0-100%", "80", "Level of the lead voice."),
            ("CHORD VOL", "0-100%", "80", "Level of the chord voices."),
        ]),
    ],
    tips=[
        "Sing simple, sustained vowels: the clearer the vowel, the more crystalline the result.",
        "Close voicings with a JUST tuning sound the most like a glass choir.",
        "For a dry stem of just the harmonies, set LEAD to OFF.",
    ],
    specs=[("Type", "AU MIDI-controlled effect (aumf), VST3, Standalone"), ("Input", "Side-chain audio + MIDI"), ("Output", "Stereo")],
),
# ---------------------------------------------------------------------------
dict(
    slug="borealis", name="BOREALiS", accent="#7B5FB0", kind="inst", motion="borealis", spectrum=True,
    tagline="An additive synth you can see. Every frequency is a coloured light; draw drones with a click.",
    intro=[
        "BOREALiS builds sound from harmonics, and shows each one as a frosted light at a fixed place across the "
        "window: low notes on the left, high on the right, coloured red to violet like the spectrum. A light only "
        "shines while it is playing, and its brightness is its volume.",
        "Click anywhere in the window to place a constant drone tone there. MIDI notes play on top of the drones. "
        "Drop an audio file on the window and BOREALiS finds its strongest pitches and adds them to the drone.",
    ],
    images=[("borealis_playing.webp", "A chord playing: each harmonic is a light at its own pitch."),
            ("borealis_from_vocal.webp", "A drone built from a dropped vocal recording.")],
    quick=[
        "Load BOREALiS as a software instrument.",
        "Play a note and turn HARMONICS up to add more lights above it.",
        "Click in the light field to place drone tones. Higher clicks are louder.",
        "Drag an audio file onto the window to turn it into a drone.",
    ],
    how=[
        ("Fixed map", "Every pitch has its own place on screen, so chords and drones are readable at a glance."),
        ("Drawn tones snap", "Clicked tones snap to the nearest semitone between C1 and C10."),
        ("Audio to drone", "A dropped file is scanned for up to 12 prominent semitones; when a pitch is already in the drone, the louder level wins."),
    ],
    groups=[
        ("SOUND", [
            ("HARMONICS", "1-64", "16", "How many harmonics each note has."),
            ("TILT", "0-200%", "100", "Brightness: how quickly upper harmonics fade."),
            ("ODD/EVEN", "-100 to +100%", "0", "Favour odd harmonics (hollow) or even ones (full)."),
            ("STRETCH", "0-100%", "0", "Pulls harmonics out of tune with each other for bell-like tones."),
            ("SHIMMER", "0-100%", "30", "Slow movement in each harmonic's level."),
            ("WIDTH", "0-100%", "60", "Stereo spread of the harmonics."),
        ]),
        ("PLAYING", [
            ("ATTACK", "up to 4000 ms", "40", "Fade-in time of each note."),
            ("RELEASE", "up to 8000 ms", "800", "Fade-out time of each note."),
            ("OCTAVE", "-2 to +2", "0", "Shifts MIDI notes by octaves."),
            ("DRAW", "ON / OFF", "ON", "Lets clicks in the window place drone tones."),
            ("DRONE", "ON / OFF", "ON", "Turns the drawn drone on or off."),
            ("DRONE LEVEL", "0-100%", "60", "Volume of the drone."),
            ("NOTE LEVEL", "0-100%", "80", "Volume of MIDI-played notes."),
        ]),
    ],
    tips=["Few harmonics with high STRETCH gives glassy bells.", "Drop a vocal or a field recording to make a drone in its key."],
    specs=[("Type", "Instrument (AU aumu), VST3, Standalone"), ("Input", "MIDI, audio files by drag and drop"), ("Output", "Stereo")],
),
# ---------------------------------------------------------------------------
dict(
    slug="quiver", name="QUiVER", accent="#01AF55", kind="fx", motion="quiver",
    tagline="A tremolo that only wakes up when you play hard, with a full dynamics stage on the same threshold.",
    intro=[
        "QUiVER's tremolo follows your playing. Below the THRESHOLD the sound is untouched. Above it the wobble "
        "grows, and reaches MAX DEPTH once you are RANGE dB over. A soft KNEE eases it in, just like a "
        "compressor's. Soft passages stay still; accents shimmer.",
        "The same threshold drives a dynamics stage: squash your playing like a compressor, or lift it with "
        "upward expansion, plus swells, a gate and an EQ the tremolo can also move.",
    ],
    images=[("quiver_dyn_squash_trem.webp", "The main page. The jelly above the threshold line wobbles with the tremolo."),
            ("quiver_wobble.webp", "The jelly through one wobble: deeper the further over the line you play."),
            ("quiver_options.webp", "OPTIONS: the set-and-forget settings.")],
    quick=[
        "Insert QUiVER on a guitar, keys or vocal track.",
        "Play, and lower THRESHOLD until your loudest notes start to wobble.",
        "Use RANGE and MAX DEPTH to set how deep the strongest notes go.",
        "Drag the THRESHOLD and RANGE lines in the animation to set them by eye.",
    ],
    how=[
        ("Depth from level", "How far over the threshold you play sets the depth. The knee makes the change gradual."),
        ("Play with vs set and forget", "The main page holds the controls you play with. OPTIONS holds the ones you set once."),
        ("Safe output", "A limiter at -0.1 dBFS sits at the end, so squash and lift settings can't clip."),
    ],
    groups=[
        ("TREMOLO", [
            ("THRESHOLD", "-60 to 0 dB", "-24", "Level where the tremolo starts."),
            ("KNEE", "0-24 dB", "6", "How gently the tremolo eases in around the threshold."),
            ("RANGE", "1-48 dB", "12", "How far over the threshold you must go to reach full depth."),
            ("MAX DEPTH", "0-100%", "100", "Deepest the tremolo will ever go."),
            ("SHAPE", "SINE / TRIANGLE / SQUARE", "SINE", "The LFO wave. The square is rounded so it doesn't click."),
            ("RATE / SYNC", "Hz or note values", "4 Hz", "Free rate, or locked to the host beat."),
            ("STEREO", "0-180°", "0", "Phase offset between left and right for a moving stereo image."),
            ("TREMOLO MOVES", "VOLUME / SQUASH / EQ", "VOLUME", "What the LFO wobbles: the level, the compressor, or the EQ."),
        ]),
        ("DYNAMICS", [
            ("DYNAMICS", "-100 to +100%", "0", "Left: squash, up to limiting and sag. Right: lift quiet parts up (to +12 dB)."),
            ("SWELL", "OFF / AUTO / PER NOTE", "OFF", "Fades notes in. SWELL IN and SWELL OUT set the times."),
            ("GATE", "-90 to -20 dB", "-90 (off)", "Closes below this level, with its own GATE RELEASE."),
            ("EQ", "-100 to +100%", "0", "One-knob tone: darker to the left, brighter to the right."),
            ("MIX", "0-100%", "100", "Parallel blend of the dynamics stage."),
        ]),
        ("OPTIONS", [
            ("DETECT", "PEAK / RMS", "PEAK", "How level is measured, with its own ATTACK and RELEASE."),
            ("ENVELOPE", "ANALOG / ADAPTIVE / COMBO", "ANALOG", "How the dynamics react: fixed times, or times that follow your playing."),
            ("PHYSICS", "WOBBLY / STABLE / TWITCHY", "STABLE", "How springy the squash and the tremolo depth feel."),
            ("EQ MODE", "MANUAL / SHIFTY", "MANUAL", "SHIFTY makes the EQ move with your dynamics."),
            ("TILT", "-12 to +12 dB", "0", "Tilts what the detector hears, so bass or treble triggers it more."),
            ("SIDECHAIN", "INTERNAL / EXTERNAL", "INTERNAL", "Trigger from another track."),
            ("DUSTY", "ON / OFF", "OFF", "A touch of overdrive."),
            ("OUTPUT", "-24 to +12 dB", "0", "Final level."),
        ]),
    ],
    tips=["Sync to 1/8 with a SQUARE shape on picked chords for a stuttering accent effect.", "TREMOLO MOVES: EQ with a slow rate gives a gentle auto-wah on loud notes only."],
    specs=[("Type", "Audio effect (AU aufx), VST3, Standalone"), ("Input", "Mono or stereo, optional side chain"), ("Output", "Stereo")],
),
# ---------------------------------------------------------------------------
dict(
    slug="reverie", name="REVERiE", accent="#F28583", kind="fx", motion="reverie",
    tagline="A wet channel and an always-listening micro-looper, both running on one shared clock.",
    intro=[
        "REVERiE has three cards. WET is a reverb, a delay, or SLIP (a pitch-stepped echo). LOOP is a tiny "
        "looper that is always recording, so pressing ON catches what you just played. CLOCK sits between "
        "them and sets the sample rate both run at: lower it and everything gets longer, darker and grittier.",
        "ROUTING decides whether the wet channel hears your input, the loop, or both, so the two can feed each "
        "other.",
    ],
    images=[("reverie_reverb_listening.webp", "WET, CLOCK and LOOP side by side."),
            ("reverie_options.webp", "OPTIONS: sync, spread, trails, tone and more."),
            ("reverie_motion.webp", "How each card's shape moves as it plays.")],
    quick=[
        "Insert REVERiE on any track and play.",
        "Pick a WET mode and set its TIME and MODIFY.",
        "Tap the LOOP footswitch to catch the last couple of seconds as a loop.",
        "Lower CLOCK for longer, lo-fi time.",
    ],
    how=[
        ("Footswitches", "Each card's ON button is a footswitch: tap to toggle, hold for a moment to FREEZE (WET) or DUB (LOOP) only while held."),
        ("Touch pads", "Each animation is an XY pad. Drag to move two controls at once; hold SHIFT for fine moves; double-click to reset."),
        ("Everything smoothed", "Mode changes, freezes, overdubs and routing changes crossfade, so nothing clicks."),
    ],
    groups=[
        ("WET", [
            ("MODE", "REVERB / DELAY / SLIP", "REVERB", "Reverb goes from multi-tap echoes to a smeared wash; delay changes time without bending pitch; slip echoes in semitone steps."),
            ("TIME", "0-100", "50", "Size or delay time."),
            ("MODIFY", "0-100", "50", "Mode-dependent: smear, feedback or pitch step."),
            ("WET MIX", "0-100%", "100", "Level of the wet channel."),
            ("FREEZE", "ON / OFF", "OFF", "Holds the current wet sound."),
        ]),
        ("CLOCK", [
            ("CLOCK", "0-100", "100", "Shared sample rate in semitone steps. Lower = longer and grittier."),
            ("ROUTING", "IN / IN + LOOP / LOOP", "IN + LOOP", "What the wet channel hears."),
            ("MIX", "0-100%", "50", "Dry against effect."),
        ]),
        ("LOOP", [
            ("MODE", "ENV / TAPE / STRETCH", "TAPE", "Env slice-repeats; tape plays at octave speeds; stretch slows time without pitch (noon holds)."),
            ("LENGTH", "0-100", "100", "Loop length."),
            ("MODIFY", "0-100", "69", "Mode-dependent: slices, speed or stretch."),
            ("LOOP MIX", "0-100%", "100", "Level of the loop."),
            ("OVERDUB", "ON / OFF", "OFF", "Layers new playing over the loop."),
        ]),
        ("OPTIONS", [
            ("SYNC", "free or note values", "free", "Lock wet and loop times to the host tempo."),
            ("SPREAD / WIDTH", "-", "-", "Stereo spread of each channel and the overall width."),
            ("TRAILS", "ON / OFF", "ON", "Let the wet tail ring out when bypassed."),
            ("TONE / FADE", "0-100%", "100", "Darkens the wet channel; fades each loop pass."),
            ("BOUNCE", "OFF or a target", "OFF", "Automatically ramps one control with a chosen shape and depth."),
            ("SMOOTH CLOCK, DRY KILL, DIRECT", "-", "-", "Glide the clock, remove the dry signal, or send dry straight to the output."),
            ("OUTPUT", "-24 to +12 dB", "0", "Final level."),
        ]),
    ],
    tips=["Catch a loop, then set ROUTING to LOOP and FREEZE the reverb for an instant ambient bed.", "A low CLOCK on the delay gives dark, tape-like echoes."],
    specs=[("Type", "Audio effect (AU aufx), VST3, Standalone"), ("Input", "Mono or stereo"), ("Output", "Stereo")],
),
# ---------------------------------------------------------------------------
dict(
    slug="blip", name="BLiP", accent="#7B89B7", kind="fx", motion="blip",
    tagline="A glitch effect and a looper in one: chop, scatter and stutter live playing or a caught loop.",
    intro=[
        "BLiP is first a glitch effect. Six algorithms (MOSAIC, BLOCKS, INTERRUPT, ARP, HAZE and PATTERN), "
        "each with four variations, slice and rearrange what you play, locked to the host's beat.",
        "Behind it sits a looper that is always listening. Switch LOOP on and it catches the bars you just "
        "played. Two modifier slots then bend the loop (or the live signal) with speed, trims, scrambles, "
        "stutters and more, and eight undo layers keep your overdubs safe.",
    ],
    images=[("blip_playing.webp", "The main page: glitch controls up top, the loop ring below."),
            ("blip_modes.webp", "All the modifier modes, each with its own shape."),
            ("blip_options.webp", "OPTIONS: length, ramp, dry and stability.")],
    quick=[
        "Insert BLiP and pick an ALGORITHM and VARIATION.",
        "Turn up ACTIVITY and MIX to hear the glitches.",
        "Switch LOOP on to catch what you just played; DUB to layer over it.",
        "Pick modifiers in MOD A / MOD B and press their ON buttons.",
    ],
    how=[
        ("Always listening", "There is no record button. With LENGTH in bars and the host playing, pressing LOOP just after a bar line catches the bars that just ended; later in a bar it waits for the next line."),
        ("SOURCE", "Choose whether the glitch and the modifiers work on the LIVE input, the LOOP, or BOTH."),
        ("Click-free edges", "Loop seams, punches, undos and slice jumps all fade, so edits stay clean."),
    ],
    groups=[
        ("GLITCH", [
            ("ALGORITHM", "MOSAIC / BLOCKS / INTERRUPT / ARP / HAZE / PATTERN", "BLOCKS", "The kind of glitch."),
            ("VARIATION", "A / B / C / D", "A", "A different take on the same idea."),
            ("SOURCE", "LIVE / BOTH / LOOP", "BOTH", "What gets glitched."),
            ("ACTIVITY", "0-100%", "50", "How busy the glitching is."),
            ("REPEATS", "0-100%", "30", "How often slices repeat."),
            ("SHAPE", "0-100%", "30", "The envelope on each slice."),
            ("TIME", "0-100%", "60", "Slice size, locked to the beat."),
            ("FILTER", "0-100%", "50", "Tone of the wet signal."),
            ("SPACE", "0-100%", "25", "Reverb around the glitches."),
            ("MIX", "0-100%", "50", "Dry against glitch."),
        ]),
        ("LOOP", [
            ("LOOP", "ON / OFF", "OFF", "Catches a loop and plays it."),
            ("DUB", "ON / OFF", "OFF", "Overdubs onto the loop. Each pass is an undo layer (up to 8)."),
            ("LOOP (knob)", "0-100%", "80", "Loop level."),
            ("UNDO / REDO", "-", "-", "Steps back and forward through the overdub layers."),
            ("FADE", "0-100%", "0", "How much each pass fades away."),
            ("SPEED %", "1/2X / 1X / 2X, REV", "100", "Tape speed, with quick 1/2X, 1X and 2X buttons and REV for reverse."),
        ]),
        ("MODIFIERS A / B", [
            ("MODE", "see list", "OFF", "Smooth speed, step speed, dropper, trimmer, step trimmer, scrambler, filter, swapper, stutter, stretcher, stopper, pitcher, destroyer."),
            ("AMOUNT", "0-100%", "50", "How strongly the modifier works."),
            ("ON", "ON / OFF", "OFF", "Engages the slot; random patterns are re-rolled each time."),
        ]),
        ("OPTIONS", [
            ("LENGTH", "FREE / 1 / 2 / 4 / 8 BARS", "FREE", "Loop length in bars, or FREE seconds (LOOP S, 1-60 s)."),
            ("RAMP", "OFF / UP / DOWN / UP DOWN / WIGGLE / RANDOM", "OFF", "Automatically moves the modifiers over RAMP S seconds."),
            ("MODE", "NORMAL / ADDITIVE", "NORMAL", "ADDITIVE prints the modifiers into the loop as you dub."),
            ("DRY", "0-100%", "100", "Level of the dry signal."),
            ("STABILITY", "0-100%", "0", "Adds tape wobble to the loop."),
        ]),
    ],
    tips=["PATTERN with high REPEATS on drums gives sequenced stutters.", "Put the pitcher on A and the stutter on B, SOURCE LIVE, for glitched leads with no loop at all."],
    specs=[("Type", "Audio effect (AU aufx), VST3, Standalone"), ("Loop", "Up to 120 s, 8 undo layers"), ("Output", "Stereo")],
),
# ---------------------------------------------------------------------------
dict(
    slug="ionise", name="iONiSE", accent="#476A6F", kind="fx", motion="ionise",
    tagline="Distortion from a gas tube: your signal strikes a plasma arc that is either lit or dark.",
    intro=[
        "iONiSE models a gas discharge tube. The tube stays dark until your signal crosses its strike voltage, "
        "then it lights up and holds a constant level until the signal falls back below the hold point. The "
        "result is a hard, buzzing, gated fuzz that tracks your dynamics in a way no clipper does.",
        "Every edge is placed to a fraction of a sample, so the fuzz stays free of digital fizz.",
    ],
    images=[("ionise_burning.webp", "The tube lit by a loud note."), ("ionise_options.webp", "OPTIONS: tube behaviour."),
            ("ionise_sputter.webp", "SPUTTER randomising each strike.")],
    quick=["Insert iONiSE on drums, bass or guitar.", "Raise GAIN until the tube lights on every hit.", "Lower VOLTAGE to turn the tube into a gate that passes your signal's shape.", "Use BLEND to mix the dry signal back."],
    how=[
        ("Strike and hold", "The tube only lights above the strike level and only goes dark below the hold level, so it buzzes and gates naturally."),
        ("Drum friendly", "CLEAN GATE, SUSTAIN and a 3-band EQ make it work well on drum buses."),
        ("One sample of latency", "The dry path is delayed by the same amount, so BLEND never phases."),
    ],
    groups=[
        ("MAIN", [
            ("TUBE", "XENON / NEON / ARGON", "XENON", "The voicing of the tube."),
            ("GAIN", "0-48 dB", "24", "Drive into the tube."),
            ("VOLTAGE", "0-100%", "100", "Low settings let the signal's shape through, like a gate."),
            ("SPUTTER", "0-100%", "30", "Randomises the strike level each half-cycle."),
            ("COLOUR", "0-100%", "55", "Tone of the filter after the tube."),
            ("FILTER", "LOW / BAND / HIGH", "LOW", "Filter type."),
            ("OCTAVE", "OFF / DOWN / UP", "OFF", "Adds an octave."),
            ("BLEND", "0-100%", "100", "Dry against plasma."),
            ("VOLUME", "-36 to +12 dB", "0", "Output level."),
        ]),
        ("EXTRAS", [
            ("SUSTAIN / OVER-SAT", "ON / OFF", "OFF", "Longer notes, or even more saturation."),
            ("CLEAN GATE", "ON / OFF", "OFF", "Gates the output, with GATE HOLD time."),
            ("EQ LOW / MID / HIGH", "-12 to +12 dB", "0", "3-band EQ; CLEAN EQ applies it to the dry too."),
            ("TREMOLO", "ON / OFF", "OFF", "TREM RATE and TREM DEPTH; past 50% it becomes ring mod. Negative depth swings between dry and plasma. DYNAMIC follows your playing."),
        ]),
        ("OPTIONS", [
            ("JITTER, CRACKLE, SPIT", "0-100%", "-", "Unstable arc behaviour."),
            ("RESONANCE", "0-100%", "20", "Filter resonance."),
            ("STEREO", "0-100%", "30", "Left and right tubes behave differently."),
            ("LOW CUT", "Hz", "80", "Cuts lows before the tube."),
            ("DIRT", "ON / OFF", "OFF", "Extra grit."),
        ]),
    ],
    tips=["On drums, short GATE HOLD with SUSTAIN off gives tight, explosive hits.", "OCTAVE UP with SPUTTER at 60% makes a broken-synth lead."],
    specs=[("Type", "Audio effect (AU aufx), VST3, Standalone"), ("Latency", "1 sample"), ("Output", "Stereo")],
),
# ---------------------------------------------------------------------------
dict(
    slug="ripple", name="RiPPLE", accent="#519E8A", kind="fx", motion="ripple",
    tagline="Random, liquid pitch movement and a low-pass gate, like playing through moving water.",
    intro=[
        "RiPPLE moves a short delay line with random steps at random times, smoothed so they flow. The result "
        "is a seasick, watery vibrato that never repeats. After it, a low-pass gate opens with your playing and "
        "closes as notes fade, so tails go dark and soft.",
    ],
    images=[("ripple_default.webp", "A box floating on the water: it bobs with the pitch movement."),
            ("ripple_motion.webp", "The water over time."), ("ripple_wide_deep.webp", "Deep and wide.")],
    quick=["Insert RiPPLE on guitar, keys or vocals.", "Set RATE for how often the pitch wanders and DAMP for how smoothly.", "DEPTH sets how far it bends.", "LPG sets how much the filter opens and closes with your playing."],
    how=[("Random, not an LFO", "There is no repeating wave. Each move goes to a new random place."), ("Low-pass gate", "Loud playing opens the filter; FLOOR sets how far it closes; RELEASE how fast.")],
    groups=[
        ("MAIN", [
            ("RATE", "0-100%", "40", "How often a new random step arrives (every 3 s up to every 15 ms)."),
            ("DAMP", "0-100%", "40", "How smoothly the steps glide (3 ms to 1 s)."),
            ("DEPTH", "0-100%", "35", "How far the pitch bends."),
            ("LPG", "0-100%", "60", "How strongly the low-pass gate follows your playing."),
            ("MIX", "0-100%", "70", "Dry against wet."),
            ("VOLUME", "-24 to +12 dB", "0", "Output level."),
        ]),
        ("OPTIONS", [
            ("INPUT", "PAD / NORMAL / BOOST", "NORMAL", "Input level into the circuit."),
            ("CLOCK", "HI-FI / VINTAGE / LO-FI", "VINTAGE", "Darkness of the delay line."),
            ("LPG FLOOR", "Hz", "400", "How far the filter closes."),
            ("LPG RELEASE", "ms", "80", "How quickly it closes."),
            ("STEREO", "0-100%", "25", "Left and right wander apart."),
        ]),
    ],
    tips=["Low RATE, high DAMP, MIX 100% gives slow, drunk tape drift.", "Fast RATE with low DAMP is a broken, fluttering vibrato."],
    specs=[("Type", "Audio effect (AU aufx), VST3, Standalone"), ("Output", "Stereo")],
),
# ---------------------------------------------------------------------------
dict(
    slug="inhale", name="iNHALE", accent="#7EB09B", kind="fx", motion="inhale",
    tagline="A true reverse reverb: the swell breathes in and lands exactly on the note.",
    intro=[
        "Classic reverse reverb means bouncing, flipping, reverbing and flipping again. iNHALE does it live. "
        "Every sound gets a reversed tail that swells up into it, so the reverb rises and finishes on the hit.",
        "Because a swell has to start before the note, iNHALE delays its output by a whole number of bars. "
        "The MOVE EARLIER readout tells you how many; move your region that many bars earlier and it lines up "
        "perfectly.",
    ],
    images=[("inhale_default.webp", "The swell grows from a circle into a square while it breathes in."),
            ("inhale_motion.webp", "One breath, frame by frame."), ("inhale_ducked.webp", "Ducked under the dry signal.")],
    quick=["Insert iNHALE and set LENGTH for how long the swell is.", "Read MOVE EARLIER (in bars).", "Move the audio region that many bars earlier.", "Play from the top. The swell lands on each note."],
    how=[
        ("Zero reported latency", "iNHALE reports no latency and instead delays by whole bars, which keeps everything musical and simple to fix."),
        ("Change while stopped", "The bar delay only changes while the transport is stopped."),
        ("Ducking", "DUCK pushes the swell down under the plugin's own input, so the dry note stays clear."),
    ],
    groups=[
        ("MAIN", [
            ("MODE", "SYNC / FREE", "SYNC", "Swell length in note values or in ms (TIME)."),
            ("LENGTH", "note values", "-", "How long the swell is."),
            ("TAIL", "HALL / PLATE / BLOOM", "HALL", "The character of the reverb."),
            ("GAP", "ms", "0", "Silence between the swell's end and the note."),
            ("CURVE", "0-100%", "50", "Shape of the rise."),
            ("TONE", "0-100%", "60", "Brightness."),
            ("WIDTH", "0-100%", "70", "Stereo width; the shape splits in two."),
            ("MIX", "0-100%", "50", "Dry against swell."),
            ("VOLUME", "-24 to +12 dB", "0", "Output level."),
        ]),
        ("DUCK", [
            ("DUCK", "0-100%", "0", "How much the swell is pushed down."),
            ("THRESHOLD", "-60 to 0 dB", "-30", "Level that triggers the duck."),
            ("RELEASE", "ms", "300", "How fast the swell recovers."),
        ]),
    ],
    tips=["Set MIX to 100% on a send for a pure, pre-echo swell under the dry track.", "BLOOM tail with a short GAP is great on vocals before each phrase."],
    specs=[("Type", "Audio effect (AU aufx), VST3, Standalone"), ("Delay", "Whole bars, up to 32 s"), ("Output", "Stereo")],
),
# ---------------------------------------------------------------------------
dict(
    slug="interlude", name="iNTERLUDE", accent="#F26419", kind="fx", motion="interlude",
    tagline="Reverb you only hear between phrases. It rises as you stop, and steps aside when you start.",
    intro=[
        "iNTERLUDE ducks its own reverb under your playing, but looks half a second ahead. That means it can "
        "start rising before a phrase ends instead of popping on after, and fall away just before the next "
        "phrase starts. Vocals and leads stay dry and clear; the space blooms in the gaps.",
    ],
    images=[("interlude_default.webp", "Main page: when to rise, when to fall."),
            ("interlude_reverb_page.webp", "The REVERB page."), ("interlude_motion.webp", "The reverb shape across a phrase.")],
    quick=["Insert iNTERLUDE on a vocal or lead.", "Set THRESHOLD so phrases count as playing and gaps as quiet.", "GAP sets how long a silence must be to count.", "RISE sets how early the reverb starts coming up."],
    how=[
        ("500 ms lookahead", "iNTERLUDE reports a fixed 500 ms latency, which your host compensates. RISE and GAP share that window."),
        ("RISE dims", "If RISE + GAP don't fit in the lookahead, RISE is shortened and its knob dims to show it."),
        ("Five spaces", "ROOM, HALL and PLATE are dense reverbs; SPRING is a dripping two-spring tank."),
    ],
    groups=[
        ("MAIN", [
            ("THRESHOLD", "-70 to 0 dB", "-40", "Level that counts as playing."),
            ("GAP", "50-450 ms", "250", "How long quiet must last to count as a gap."),
            ("RISE", "10-450 ms", "180", "How early before the phrase ends the reverb starts coming up."),
            ("ATTACK", "10-3000 ms", "400", "How long the fade-in lasts; it can run on into the gap."),
            ("FALL", "5-450 ms", "80", "How fast it ducks before the next phrase."),
            ("DUCK", "0-100%", "100", "How far the reverb is pushed down while you play."),
            ("BLOOM", "0-1500 ms", "0", "Makes the reverb swell after each sound."),
            ("MIX / VOLUME", "% / dB", "50 / 0", "Wet level and output."),
        ]),
        ("REVERB PAGE", [
            ("SPACE", "ROOM / HALL / PLATE / SPRING", "HALL", "The reverb type."),
            ("DECAY, SIZE, PREDELAY", "-", "4 s", "Length and size of the space."),
            ("DAMPING, DIFFUSION, EARLY", "0-100%", "-", "How the space sounds."),
            ("MOD DEPTH / MOD RATE", "% / 0.1-5 Hz", "30 / 0.8", "Gentle movement in the tail."),
            ("LOW CUT / HIGH CUT", "Hz / kHz", "150 / 6", "Tone of the wet signal."),
            ("BASS DECAY", "0.5-2x", "1x", "How long lows ring compared with highs."),
            ("DRIP", "0-100%", "50", "Spring only: the splashy drip."),
        ]),
    ],
    tips=["Long DECAY with DUCK at 100% gives huge spaces that never wash out the words.", "SPRING with high DRIP is a surf-guitar gap fill."],
    specs=[("Type", "Audio effect (AU aufx), VST3, Standalone"), ("Latency", "500 ms (reported)"), ("Output", "Stereo")],
),
# ---------------------------------------------------------------------------
dict(
    slug="twirl", name="TWiRL", accent="#A4243B", kind="fx", motion="twirl",
    tagline="Lo-fi chorus, vibrato and a faux rotary: one wobbly delay chip, four knobs and a HAVOC switch.",
    intro=[
        "TWiRL is a tiny digital delay line that bends pitch as its clock speeds up and slows down. Short "
        "OFFSET gives chorus and vibrato, long OFFSET gives warped slapback. Stomp HAVOC and the speed leaps to "
        "16 Hz like a rotary speaker spinning up, and coasts back down when you let go.",
        "GRIT models the chip's character: companding, a sample clock that slows on long delays, fewer bits "
        "and a little hiss.",
    ],
    images=[("twirl_default.webp", "The shape tumbles with the LFO; its distance from the dry square is the delay."),
            ("twirl_motion.webp", "One LFO cycle."), ("twirl_havoc.webp", "HAVOC engaged.")],
    quick=["Insert TWiRL on guitar or keys.", "MIX at 50% for chorus, 100% for vibrato.", "Set SPEED and DEPTH.", "Press HAVOC for the rotary rush."],
    how=[("Pitch from the clock", "DEPTH moves the chip's clock up to an octave either way, so it bends like real tape or a bucket-brigade."),
         ("HAVOC RAMP", "RAMP sets how long it takes to spin up; it coasts down 1.5 times slower, like a rotor."),
         ("Synced", "SYNC locks the LFO to the host's beat and bar position.")],
    groups=[
        ("MAIN", [
            ("OFFSET", "0-100% (1.5-90 ms)", "35", "Delay time: chorus at the short end, slapback at the long end."),
            ("SPEED", "0-100% (0.05-10 Hz)", "35", "LFO rate."),
            ("DEPTH", "0-100%", "50", "How far pitch bends (up to an octave)."),
            ("MIX", "0-100%", "50", "Dry against wet. 100% is pure vibrato."),
            ("WAVE", "TRIANGLE / SQUARE / RANDOM", "TRIANGLE", "LFO shape. Square and random are slewed for bleep-bloops."),
            ("TONE", "FULL / HI-CUT", "FULL", "Full range or darker."),
            ("HAVOC", "ON / OFF", "OFF", "Maximum speed. HAVOC MODE: LATCH or HOLD."),
        ]),
        ("EXTRAS", [
            ("RAMP", "0-999 ms", "700", "HAVOC spin-up time."),
            ("SYNC", "free or note values", "free", "Tempo sync."),
            ("FEEDBACK", "0-100%", "0", "Repeats."),
            ("GRIT", "0-100%", "40", "Chip character."),
            ("STEREO", "0-100%", "0", "Left and right out of phase."),
            ("VOLUME", "-24 to +12 dB", "0", "Output level."),
        ]),
    ],
    tips=["RANDOM wave at slow SPEED with MIX 100% is a warped-tape wobble.", "Long OFFSET, FEEDBACK 40% and GRIT high is a broken toy delay."],
    specs=[("Type", "Audio effect (AU aufx), VST3, Standalone"), ("Output", "Stereo")],
),
# ---------------------------------------------------------------------------
dict(
    slug="hiraeth", name="HiRAETH", accent="#7B89B7", kind="fx", motion="hiraeth",
    tagline="Three cards for longing: bowed swells, memories that age, and chorus that melts away.",
    intro=[
        "HiRAETH chains three effects that each change the longer a note lives. BOW removes your pick attack "
        "and swells notes in like a bowed string. FADE ages a note as it rings, from fresh to worn tape. "
        "DiSiNTEGRATE starts as a chorus and melts into a wash.",
        "Each card has its own ON switch and can be minimised, so you can use one, two or all three.",
    ],
    images=[("hiraeth_default.webp", "BOW, FADE and DiSiNTEGRATE side by side."),
            ("hiraeth_motion.webp", "Each card's shape across a note's life."), ("hiraeth_glacier.webp", "The GLACIER preset.")],
    quick=["Insert HiRAETH on guitar, keys or vocals.", "Pick a preset, or switch cards on one at a time.", "Hold notes: each card shows what it is doing as the note ages.", "Set OUTPUT in the header."],
    how=[
        ("Lookahead attack removal", "BOW looks 6 ms ahead to dip the gain before each pick attack, then swells the note in."),
        ("Ages with time", "FADE and DiSiNTEGRATE count each note's age by NOTE, PHRASE or BAR (from the host's position)."),
        ("Low end stays put", "DiSiNTEGRATE keeps everything below LOW HZ centred and un-chorused."),
    ],
    groups=[
        ("BOW", [
            ("BOW", "CELLO / VIOLA / BASS", "CELLO", "Character of the swell and bow noise."),
            ("TRIGGER", "EVERY / GAP", "EVERY", "Swell every note, or only after a gap. SENS sets detection."),
            ("SWELL MS", "20-4000 ms", "600", "Swell time."),
            ("PRESSURE", "0-100%", "50", "Opens a low-pass, like pressing harder with the bow."),
            ("NOISE", "0-100%", "35", "Bow grain made from the note itself."),
            ("BLOOM", "0-100%", "45", "Reverb behind the bow."),
            ("MIX", "0-100%", "100", "Card mix."),
        ]),
        ("FADE", [
            ("TAPE", "CASSETTE / REEL / VHS", "CASSETTE", "Kind of wear."),
            ("AGE BY", "NOTE / PHRASE / BAR", "NOTE", "What resets the clock."),
            ("AGE MS", "100-9999 ms", "3000", "How long until fully aged."),
            ("WARBLE", "0-100%", "40", "Wow and flutter, eased in so new notes start steady."),
            ("DULL", "0-100%", "45", "Treble loss."),
            ("HISS", "0-100%", "25", "Gated tape hiss."),
            ("WEAR", "0-100%", "15", "Saturation and dropouts."),
            ("MIX", "0-100%", "100", "Card mix."),
        ]),
        ("DiSiNTEGRATE", [
            ("CHORUS", "CLASSIC / LUSH / BASS", "CLASSIC", "Chorus voicing."),
            ("MELT BY", "NOTE / PHRASE / BAR", "NOTE", "What resets the melt."),
            ("RATE / DEPTH", "0-100%", "30 / 50", "Chorus speed and depth."),
            ("MELT MS", "100-9999 ms", "2500", "Time until the chorus melts into a wash."),
            ("WASH", "0-100%", "60", "How much melts."),
            ("LOW HZ", "20-400 Hz", "120", "Below this stays centred and dry."),
            ("MIX", "0-100%", "100", "Card mix."),
        ]),
    ],
    tips=["BOW alone on clean guitar is an instant volume-pedal swell.", "FADE by PHRASE makes the end of every line sound like an old memory."],
    specs=[("Type", "Audio effect (AU aufx), VST3, Standalone"), ("Latency", "576 samples at 48 kHz"), ("Output", "Stereo")],
),
]
