# New Competitive Moves Guide

This ROM hack adds 8 popular competitive moves to enhance battle strategy!

---

## 🎯 **New Moves Added**

### **1. Will-O-Wisp** (Fire-type Status Move)
- **Type:** Fire
- **Power:** —
- **Accuracy:** 85%
- **PP:** 15
- **Effect:** Inflicts burn on the target
- **Description:** A status move that burns the opponent, halving their Attack stat and dealing residual damage each turn.

**Best Users:**
- Ghost-types (Gengar, Misdreavus)
- Fire-types (Typhlosion, Arcanine, Houndoom)
- Defensive Pokémon that want to cripple physical attackers

---

### **2. Dragon Dance** (Dragon-type Status Move)
- **Type:** Dragon
- **Power:** —
- **Accuracy:** 100%
- **PP:** 20
- **Effect:** Raises user's Attack and Speed by 1 stage each
- **Description:** A powerful setup move that boosts both offensive stats simultaneously.

**Best Users:**
- Dragonite
- Gyarados
- Tyranitar
- Kingdra
- Charizard

---

### **3. Close Combat** (Fighting-type Physical Move)
- **Type:** Fighting
- **Power:** 120
- **Accuracy:** 100%
- **PP:** 5
- **Effect:** Lowers user's Defense and Sp. Def by 1 stage after use
- **Description:** The strongest reliable Fighting-type move, trading defenses for massive power.

**Best Users:**
- Machamp
- Heracross
- Primeape
- Hitmonlee
- Lucario (if added)

---

### **4. Brave Bird** (Flying-type Physical Move)
- **Type:** Flying
- **Power:** 120
- **Accuracy:** 100%
- **PP:** 15
- **Effect:** User takes 1/3 recoil damage
- **Description:** The strongest Flying-type physical move, with significant recoil.

**Best Users:**
- Pidgeot
- Fearow
- Skarmory
- Crobat
- Dodrio

---

### **5. Scald** (Water-type Special Move)
- **Type:** Water
- **Power:** 80
- **Accuracy:** 100%
- **PP:** 15
- **Effect:** 30% chance to burn the target
- **Description:** A reliable Water-type attack that can cripple physical attackers with burns.

**Best Users:**
- Vaporeon
- Starmie
- Suicune
- Slowbro
- Politoed

---

### **6. U-Turn** (Bug-type Physical Move)
- **Type:** Bug
- **Power:** 70
- **Accuracy:** 100%
- **PP:** 20
- **Effect:** User switches out after dealing damage
- **Description:** Deals damage then switches to another Pokémon, maintaining momentum.

**Best Users:**
- Scizor
- Heracross
- Scyther
- Pinsir
- Forretress

---

### **7. Stealth Rock** (Rock-type Status Move)
- **Type:** Rock
- **Power:** —
- **Accuracy:** 100%
- **PP:** 20
- **Effect:** Sets up entry hazard that damages switching Pokémon
- **Description:** The most important competitive move - damages opponents when they switch in based on Rock-type effectiveness.

**Best Users:**
- Tyranitar
- Golem
- Steelix
- Donphan
- Forretress

---

### **8. Knock Off** (Dark-type Physical Move)
- **Type:** Dark
- **Power:** 65
- **Accuracy:** 100%
- **PP:** 20
- **Effect:** Removes target's held item
- **Description:** Removes the opponent's held item, crippling item-dependent strategies.

**Best Users:**
- Umbreon
- Houndoom
- Tyranitar
- Sneasel
- Murkrow

---

## 📊 **Move Comparison Table**

| Move | Type | Category | Power | Accuracy | PP | Key Effect |
|------|------|----------|-------|----------|----|-----------| 
| Will-O-Wisp | Fire | Status | — | 85% | 15 | Burns target |
| Dragon Dance | Dragon | Status | — | 100% | 20 | +1 Atk/Spd |
| Close Combat | Fighting | Physical | 120 | 100% | 5 | Lowers defenses |
| Brave Bird | Flying | Physical | 120 | 100% | 15 | 1/3 recoil |
| Scald | Water | Special | 80 | 100% | 15 | 30% burn |
| U-Turn | Bug | Physical | 70 | 100% | 20 | Switch out |
| Stealth Rock | Rock | Status | — | 100% | 20 | Entry hazard |
| Knock Off | Dark | Physical | 65 | 100% | 20 | Remove item |

---

## ⚙️ **Implementation Status**

### ✅ **Completed:**
1. Move constants added (`constants/move_constants.asm`)
2. Move names added (`data/moves/names.asm`)
3. Move data added - power, accuracy, type, PP (`data/moves/moves.asm`)
4. Move descriptions added (`data/moves/descriptions.asm`)
5. Move effect constants added (`constants/move_effect_constants.asm`)

### ⚠️ **To Complete:**
The following still need to be implemented for the moves to work in-game:

1. **Move Effects Programming** - ASM code for each new effect:
   - `EFFECT_BURN` - Will-O-Wisp effect (inflict burn status)
   - `EFFECT_ATTACK_SPEED_UP` - Dragon Dance effect (+1 Atk, +1 Spd)
   - `EFFECT_CLOSE_COMBAT` - Lowers user's Def/SpDef after hit
   - `EFFECT_STEALTH_ROCK` - Entry hazard implementation
   - `EFFECT_KNOCK_OFF` - Remove opponent's held item
   - Note: Brave Bird uses existing `EFFECT_RECOIL_HIT`
   - Note: Scald uses existing `EFFECT_BURN_HIT`
   - Note: U-Turn uses existing `EFFECT_BATON_PASS` (needs modification)

2. **Move Effect Pointers** - Add to `data/moves/effects_pointers.asm`

3. **Move Animations** - Add to `data/moves/animations.asm`

4. **Pokémon Learnsets** - Distribute moves to appropriate Pokémon
   - Level-up moves in `data/pokemon/evos_attacks.asm`
   - TM/HM compatibility (if making TMs)

5. **AI Logic** - Teach AI when to use these moves effectively

---

## 🎮 **Suggested Distribution**

### **Will-O-Wisp:**
- Gengar (Level 45)
- Typhlosion (Level 48)
- Houndoom (Level 46)
- Misdreavus (Level 43)
- Arcanine (Level 45)
- Ninetales (Level 44)

### **Dragon Dance:**
- Dragonite (Level 50)
- Gyarados (Level 48)
- Tyranitar (Level 52)
- Kingdra (Level 49)
- Charizard (Level 50)

### **Close Combat:**
- Machamp (Level 48)
- Heracross (Level 46)
- Primeape (Level 45)
- Hitmonlee (Level 44)
- Hitmonchan (Level 44)

### **Brave Bird:**
- Pidgeot (Level 47)
- Fearow (Level 45)
- Skarmory (Level 50)
- Crobat (Level 48)
- Dodrio (Level 46)

### **Scald:**
- Vaporeon (Level 42)
- Starmie (Level 40)
- Suicune (Level 45)
- Slowbro (Level 44)
- Politoed (Level 43)
- Lapras (Level 45)

### **U-Turn:**
- Scizor (Level 40)
- Heracross (Level 38)
- Scyther (Level 40)
- Pinsir (Level 42)
- Forretress (Level 38)

### **Stealth Rock:**
- Tyranitar (Level 40)
- Golem (Level 38)
- Steelix (Level 40)
- Donphan (Level 38)
- Forretress (Level 35)
- Rhydon (Level 40)

### **Knock Off:**
- Umbreon (Level 38)
- Houndoom (Level 40)
- Tyranitar (Level 42)
- Sneasel (Level 36)
- Murkrow (Level 35)

---

## 💡 **Competitive Impact**

### **Meta-Defining Moves:**
1. **Stealth Rock** - The most important move added. Forces switches and chip damage.
2. **Dragon Dance** - Enables sweep strategies for physical attackers.
3. **Will-O-Wisp** - Cripples physical threats without using an attack slot.

### **High-Value Additions:**
4. **Scald** - Gives Water-types a reliable STAB move with utility.
5. **U-Turn** - Enables momentum-based playstyles.
6. **Close Combat** - Makes Fighting-types much more threatening.

### **Utility Moves:**
7. **Brave Bird** - Gives Flying-types a powerful STAB option.
8. **Knock Off** - Disrupts item-dependent strategies.

---

## 🔧 **Next Steps for Full Implementation**

To complete the implementation, you'll need to:

1. **Program Move Effects** in `engine/battle/move_effects/` directory
   - Create new effect files or modify existing ones
   - Reference existing effects like `EFFECT_RECOIL_HIT` for Brave Bird patterns

2. **Add Effect Pointers** in `data/moves/effects_pointers.asm`
   - Link each new effect constant to its code

3. **Create Animations** (optional but recommended)
   - Add battle animations for visual feedback

4. **Update Learnsets** in `data/pokemon/evos_attacks.asm`
   - Add moves to appropriate Pokémon at suitable levels

5. **Test Thoroughly**
   - Verify each move works correctly
   - Check for bugs or crashes
   - Balance test the competitive impact

---

## 📝 **Files Modified**

1. `constants/move_constants.asm` - Added move IDs 105-10c
2. `data/moves/names.asm` - Added move names
3. `data/moves/moves.asm` - Added move data
4. `data/moves/descriptions.asm` - Added descriptions
5. `constants/move_effect_constants.asm` - Added effect constants

---

**Note:** The core move data is in place, but move effects need ASM programming to function. This is a solid foundation for adding these competitive moves to your ROM hack!
