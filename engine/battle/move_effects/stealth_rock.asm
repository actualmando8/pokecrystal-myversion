StealthRock:
; Stealth Rock effect - sets up entry hazard
	ld hl, wEnemyScreens
	ldh a, [hBattleTurn]
	and a
	jr z, .got_screens
	ld hl, wPlayerScreens
.got_screens
	bit SCREENS_STEALTH_ROCK, [hl]
	jr nz, .failed
	
	set SCREENS_STEALTH_ROCK, [hl]
	call AnimateCurrentMove
	ld hl, StealthRockText
	jp StdBattleTextbox

.failed
	call AnimateFailedMove
	jp PrintButItFailed

StealthRockText:
	text_far _StealthRockText
	text_end
