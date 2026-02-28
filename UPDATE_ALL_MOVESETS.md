# Comprehensive Moveset Update Script

## Overview
This script provides a systematic approach to update all 286 Pokémon movesets with modern, comprehensive moves.

## Update Principles

### 1. Progressive Power Scaling
- Early levels (1-20): Basic moves, status moves
- Mid levels (21-40): Intermediate power moves
- High levels (41-60): Strong moves, signature moves
- Max levels (61+): Ultimate moves, legendary powers

### 2. Type Coverage
- Primary type moves (60-70% of moveset)
- Secondary type moves (20-30% of moveset)
- Coverage moves (10-20% of moveset)
- Status/utility moves (10-15% of moveset)

### 3. Move Categories by Type

#### Fire Type Moves
- Basic: EMBER, FIRE_SPIN
- Intermediate: FLAMETHROWER, FIRE_FANG
- Advanced: FIRE_BLAST, FLARE_BLITZ
- Ultimate: BLAST_BURN, INFERNO

#### Water Type Moves
- Basic: BUBBLE, WATER_GUN
- Intermediate: WATER_PULSE, SURF
- Advanced: HYDRO_PUMP, WATERFALL
- Ultimate: HYDRO_CANNON, ORIGIN_PULSE

#### Grass Type Moves
- Basic: VINE_WHIP, RAZOR_LEAF
- Intermediate: LEAF_STORM, GIGA_DRAIN
- Advanced: POWER_WHIP, PETAL_DANCE
- Ultimate: FRENZY_PLANT, LEAF_BLADE

#### Electric Type Moves
- Basic: THUNDERSHOCK, SPARK
- Intermediate: THUNDERBOLT, THUNDER_WAVE
- Advanced: THUNDER, DISCHARGE
- Ultimate: VOLT_TACKLE, WILD_CHARGE

#### Psychic Type Moves
- Basic: CONFUSION, PSYBEAM
- Intermediate: PSYCHIC_M, CALM_MIND
- Advanced: FUTURE_SIGHT, PSYCH_UP
- Ultimate: MIND_BLOWN, EXPANDING_FORCE

#### Fighting Type Moves
- Basic: TACKLE, LOW_KICK
- Intermediate: KARATE_CHOP, BRICK_BREAK
- Advanced: DYNAMICPUNCH, CLOSE_COMBAT
- Ultimate: FOCUS_PUNCH, SUPERPOWER

#### Dragon Type Moves
- Basic: DRAGON_RAGE, TWISTER
- Intermediate: DRAGON_CLAW, DRAGON_PULSE
- Advanced: DRAGON_DANCE, OUTRAGE
- Ultimate: DRAGON_ASCENT, DRAGON_ENERGY

#### Dark Type Moves
- Basic: BITE, PURSUIT
- Intermediate: DARK_PULSE, CRUNCH
- Advanced: FOUL_PLAY, KNOCK_OFF
- Ultimate: DARK_VOID, NIGHT_DAZE

#### Steel Type Moves
- Basic: TACKLE, METAL_CLAW
- Intermediate: IRON_HEAD, STEEL_WING
- Advanced: METEOR_MASH, IRON_DEFENSE
- Ultimate: GYRO_BALL, FLASH_CANNON

#### Fairy Type Moves
- Basic: TACKLE, CHARM
- Intermediate: DAZZLING_GLEAM, MOONBLAST
- Advanced: PLAY_ROUGH, FAIRY_WIND
- Ultimate: MISTY_EXPLOSION, FRENZY_PLANT

#### Ghost Type Moves
- Basic: LICK, ASTONISH
- Intermediate: SHADOW_BALL, HEX
- Advanced: SHADOW_CLAW, POLTERGEIST
- Ultimate: DESTINY_BOND, SHADOW_FORCE

#### Ice Type Moves
- Basic: POWDER_SNOW, ICE_SHARD
- Intermediate: ICE_BEAM, ICY_WIND
- Advanced: BLIZZARD, FROST_BREATH
- Ultimate: ICE_BURN, GLACIAL_LANCE

#### Poison Type Moves
- Basic: POISON_STING, SLUDGE
- Intermediate: SLUDGE_BOMB, POISON_JAB
- Advanced: GUNK_SHOT, TOXIC
- Ultimate: POISON_FANG, VENOSHOCK

#### Ground Type Moves
- Basic: SAND_ATTACK, MUD_SLAP
- Intermediate: EARTHQUAKE, DIG
- Advanced: BONEMERANG, PRECIPICE_BLADES
- Ultimate: FISSURE, THOUSAND_ARROWS

#### Rock Type Moves
- Basic: ROCK_THROW, DEFENSE_CURL
- Intermediate: ROCK_SLIDE, STEALTH_ROCK
- Advanced: STONE_EDGE, ROCK_TOMB
- Ultimate: HEAD_SMASH, PRECIPICE_BLADES

#### Flying Type Moves
- Basic: PECK, GUST
- Intermediate: WING_ATTACK, AIR_SLASH
- Advanced: FLY, BRAVE_BIRD
- Ultimate: SKY_ATTACK, HURRICANE

#### Bug Type Moves
- Basic: TACKLE, BUG_BITE
- Intermediate: X_SCISSOR, SIGNAL_BEAM
- Advanced: BUG_BUZZ, PIN_MISSILE
- Ultimate: ATTACK_ORDER, LUNGE

#### Normal Type Moves
- Basic: TACKLE, GROWL
- Intermediate: BODY_SLAM, HYPER_BEAM
- Advanced: EXPLOSION, GIGA_IMPACT
- Ultimate: BOOMBURST, HYPER_VOICE

## Implementation Strategy

### Phase 1: Starter Pokémon (Priority 1)
- Bulbasaur line ✅
- Charmander line ✅
- Squirtle line
- Chikorita line
- Cyndaquil line
- Totodile line

### Phase 2: Legendary Pokémon (Priority 1)
- Articuno, Zapdos, Moltres
- Mewtwo, Mew
- Raikou, Entei, Suicune
- Lugia, Ho-Oh
- Celebi

### Phase 3: Popular Competitive Pokémon (Priority 2)
- Gengar, Alakazam, Machamp
- Dragonite, Gyarados, Snorlax
- Tyranitar, Metagross, Salamence
- Lucario, Garchomp, etc.

### Phase 4: Common Pokémon (Priority 3)
- Pidgey, Rattata, Caterpie lines
- Eeveelutions
- Common route Pokémon

### Phase 5: All Remaining Pokémon (Priority 4)
- Complete coverage of all 286 Pokémon

## Move Level Distribution Template

### Basic Stage Pokémon (1-2 evolutions)
```
Level 1: Basic move 1, Basic move 2
Level 5-10: Status move, Basic attack
Level 15-20: Intermediate attack
Level 25-30: Better intermediate attack
Level 35-40: Strong attack
Level 45-50: Signature move
Level 55-60: Ultimate move
```

### Two-Stage Pokémon
```
Level 1: Basic moves (2-3)
Level 10-15: Status moves, basic attacks
Level 20-25: Intermediate attacks
Level 30-35: Strong attacks
Level 40-45: Signature moves
Level 50-55: Ultimate moves
Level 60+: Final ultimate moves
```

### Three-Stage Pokémon
```
Level 1: Basic moves (2-3)
Level 8-12: Status moves, basic attacks
Level 15-20: Intermediate attacks
Level 25-30: Strong attacks
Level 35-40: Signature moves
Level 45-50: Ultimate moves
Level 55-60: Final ultimate moves
Level 65+: Legendary ultimate moves
```

## Special Considerations

### Baby Pokémon
- Start with weaker moves
- Learn status moves early
- Evolution moves at appropriate levels

### Legendary Pokémon
- Higher base power moves
- More signature moves
- Earlier access to powerful moves

### Pseudo-Legendary Pokémon
- Dragonite, Tyranitar, Salamence, Metagross, Garchomp
- Very strong move pools
- Multiple signature moves

### Eeveelutions
- Type-specific moves
- Some status moves
- Good coverage options

## Execution Plan

1. **Update evos_attacks.asm** with new level-up moves
2. **Update base_stats/*.asm** files with new TM learnsets
3. **Verify move compatibility** with Pokémon types
4. **Test compilation** to ensure no errors
5. **Balance check** for game progression

## Quality Assurance

### Move Power Scaling
- Ensure appropriate power progression
- Avoid overpowered early moves
- Balance signature moves

### Type Coverage
- Verify type compatibility
- Ensure good coverage options
- Avoid redundant moves

### Game Balance
- Consider early game difficulty
- Maintain progression curve
- Keep competitive viability

This systematic approach ensures comprehensive, balanced updates to all 286 Pokémon movesets while maintaining game balance and playability.
