; New Fairy-type move animations

BattleAnim_Moonblast:
	anim_2gfx BATTLE_ANIM_GFX_BEAM, BATTLE_ANIM_GFX_MISC
	anim_bgeffect BATTLE_BG_EFFECT_CYCLE_MID_OBPALS_GRAY_AND_YELLOW, $0, $2, $0
	anim_obj BATTLE_ANIM_OBJ_MOON, 96, 40, $0
	anim_wait 6
	anim_obj BATTLE_ANIM_OBJ_BEAM, 96, 40, $0
	anim_wait 16
	anim_ret

BattleAnim_PlayRough:
	anim_1gfx BATTLE_ANIM_GFX_HIT
	anim_sound 0, 1, SFX_MEGA_PUNCH
	anim_obj BATTLE_ANIM_OBJ_01, 112, 56, $0
	anim_wait 6
	anim_sound 0, 1, SFX_MEGA_PUNCH
	anim_obj BATTLE_ANIM_OBJ_01, 112, 56, $0
	anim_wait 6
	anim_sound 0, 1, SFX_MEGA_PUNCH
	anim_obj BATTLE_ANIM_OBJ_01, 112, 56, $0
	anim_wait 16
	anim_ret

BattleAnim_DazzlingGleam:
	anim_2gfx BATTLE_ANIM_GFX_SHINE, BATTLE_ANIM_GFX_MISC
	anim_bgeffect BATTLE_BG_EFFECT_CYCLE_MID_OBPALS_GRAY_AND_YELLOW, $0, $2, $0
	anim_obj BATTLE_ANIM_OBJ_GLIMMER, 96, 40, $0
	anim_wait 4
	anim_obj BATTLE_ANIM_OBJ_GLIMMER, 112, 48, $0
	anim_wait 4
	anim_obj BATTLE_ANIM_OBJ_GLIMMER, 80, 48, $0
	anim_wait 16
	anim_ret

BattleAnim_DrainingKiss:
	anim_2gfx BATTLE_ANIM_GFX_OBJECTS, BATTLE_ANIM_GFX_ANGELS
	anim_obj BATTLE_ANIM_OBJ_SWEET_KISS, 96, 40, $0
	anim_wait 16
	anim_sound 0, 0, SFX_MEGA_DRAIN
	anim_call BattleAnim_FollowEnemyFeet_0
	anim_call BattleAnim_ShowMon_0
	anim_ret

BattleAnim_FairyWind:
	anim_1gfx BATTLE_ANIM_GFX_WIND
	anim_sound 6, 2, SFX_MENU
	anim_obj BATTLE_ANIM_OBJ_GUST, 96, 40, $0
	anim_wait 2
	anim_obj BATTLE_ANIM_OBJ_GUST, 96, 40, $8
	anim_wait 2
	anim_obj BATTLE_ANIM_OBJ_GUST, 96, 40, $10
	anim_wait 64
	anim_ret

BattleAnim_DisarmingVoice:
	anim_1gfx BATTLE_ANIM_GFX_NOISE
	anim_sound 6, 2, SFX_PERISH_SONG
	anim_obj BATTLE_ANIM_OBJ_WAVE, 64, 96, $2
	anim_wait 4
	anim_obj BATTLE_ANIM_OBJ_WAVE, 64, 96, $2
	anim_wait 4
	anim_obj BATTLE_ANIM_OBJ_WAVE, 64, 96, $2
	anim_wait 64
	anim_ret

BattleAnim_FlowerShield:
	anim_2gfx BATTLE_ANIM_GFX_FLOWER, BATTLE_ANIM_GFX_MISC
	anim_bgeffect BATTLE_BG_EFFECT_CYCLE_MID_OBPALS_GRAY_AND_YELLOW, $0, $2, $0
	anim_obj BATTLE_ANIM_OBJ_FLOWER, 64, 96, $2
	anim_wait 2
	anim_obj BATTLE_ANIM_OBJ_FLOWER, 64, 96, $2
	anim_wait 2
	anim_obj BATTLE_ANIM_OBJ_FLOWER, 64, 96, $2
	anim_wait 64
	anim_ret

BattleAnim_FairyLock:
	anim_1gfx BATTLE_ANIM_GFX_MISC
	anim_sound 0, 0, SFX_MEAN_LOOK
	anim_obj BATTLE_ANIM_OBJ_01, 112, 56, $0
	anim_wait 32
	anim_ret

BattleAnim_BabyDollEyes:
	anim_2gfx BATTLE_ANIM_GFX_OBJECTS, BATTLE_ANIM_GFX_ANGELS
	anim_bgeffect BATTLE_BG_EFFECT_CYCLE_MID_OBPALS_GRAY_AND_YELLOW, $0, $2, $0
	anim_obj BATTLE_ANIM_OBJ_SWEET_KISS, 96, 40, $0
	anim_wait 16
	anim_ret
