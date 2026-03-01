CloseCombat:
; Close Combat effect - lowers user's Defense and Sp. Def by 1 stage after dealing damage
	call BattleCommand_DamageCalc
	call BattleCommand_LowerSub
	call BattleCommand_MoveDelay
	call BattleCommand_RaiseSub
	call BattleCommand_SuperEffectiveText
	call BattleCommand_CheckFaint
	
	; Lower user's Defense and Sp. Def
	ld a, [wAttackMissed]
	and a
	ret nz
	
	call BattleCommand_SwitchTurn
	
	; Lower Defense
	ld a, DEFENSE
	ld [wLoweredStat], a
	call BattleCommand_LowerStat
	
	; Lower Sp. Def
	ld a, SP_DEFENSE
	ld [wLoweredStat], a
	call BattleCommand_LowerStat
	
	jp BattleCommand_SwitchTurn

BattleCommand_LowerStat:
	ld a, [wLoweredStat]
	ld b, a
	ld a, $1 ; lower by 1 stage
	ld hl, .stat_down_message
	call BattleCommand_StatDown
	ret

.stat_down_message
	text_far _StatFellText
	text_end
