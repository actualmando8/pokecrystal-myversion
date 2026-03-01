KnockOff:
; Knock Off effect - removes opponent's held item
	call BattleCommand_DamageCalc
	call BattleCommand_LowerSub
	call BattleCommand_MoveDelay
	call BattleCommand_RaiseSub
	call BattleCommand_SuperEffectiveText
	call BattleCommand_CheckFaint
	
	ld a, [wAttackMissed]
	and a
	ret nz
	
	; Check if opponent has an item
	call GetOpponentItem
	ld a, [hl]
	and a
	ret z
	
	; Remove the item
	ld [wNamedObjectIndex], a
	xor a
	ld [hl], a
	call GetItemName
	ld hl, KnockOffItemText
	jp StdBattleTextbox

KnockOffItemText:
	text_far _KnockOffItemText
	text_end
