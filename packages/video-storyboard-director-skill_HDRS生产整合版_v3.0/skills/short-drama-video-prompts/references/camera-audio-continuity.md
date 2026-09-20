# Camera, audio, and continuity

## Camera

Camera movement is event-triggered. A shot moves because a story event changes information, emotion, power or distance; otherwise it stays locked or uses only the accepted minimal movement.

Use one primary camera movement per AI generation unit. If a shot needs a push and then an arc and then a pan to remain readable, the shot is probably overloaded and should be split upstream.

## Audio

Dialogue, VO, sync sound, ambience, SFX and music are separate information layers.

- Dialogue stays verbatim.
- VO stays verbatim and does not cause visible mouth movement unless the visible character is actually speaking.
- Keep speaker identity explicit where multiple voices exist.
- Ambient sound should support location continuity, not substitute for missing story information.
- Music supports emotion and rhythm but does not hide failed performance or unclear plot exposition.

## Continuity

Check character identity, wardrobe, hair, wounds, makeup, props, hand ownership, stance, left/right relation, action direction, eyeline, axis, room geography, door/window state, light/time, object position, action start state and action end state.

The next shot inherits the previous shot's accepted end state. It does not reinitialize the character or prop state.
