AttackSpeedUp:
; Dragon Dance effect - raises Attack and Speed by 1 stage each
	ld b, ATTACK | SPEED
	call BattleCommand_StatUpMessage
	jp BattleCommand_StatUp

BattleCommand_StatUpMessage:
; Print stat up message for multiple stats
	push bc
	call AnimateCurrentMove
	pop bc
	ret
