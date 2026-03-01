DoBurn:
; Will-O-Wisp effect - inflicts burn status
	call CheckSubstituteOpp
	jr nz, .failed

	ld a, BATTLE_VARS_STATUS_OPP
	call GetBattleVar
	and a
	jr nz, .failed

	call CheckIfTargetIsPoisonType
	jr z, .failed

	call CheckIfTargetIsFireType
	jr z, .failed

	call AnimateCurrentMove
	call BattleCommand_BurnTarget
	ld hl, WasBurnedText
	call StdBattleTextbox
	farcall UseHeldStatusHealingItem
	ret

.failed
	call AnimateFailedMove
	jp PrintDidntAffect

CheckIfTargetIsFireType:
	ld de, EnemyMonType1
	ldh a, [hBattleTurn]
	and a
	jr z, .ok
	ld de, BattleMonType1
.ok
	ld a, [de]
	cp FIRE
	ret z
	inc de
	ld a, [de]
	cp FIRE
	ret
