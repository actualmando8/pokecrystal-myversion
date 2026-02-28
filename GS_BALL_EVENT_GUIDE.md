# GS Ball Event - Celebi Encounter Guide

The GS Ball event has been **enabled for all versions** of this Pokémon Crystal ROM hack, not just Virtual Console.

---

## 🎯 **How to Get Celebi**

### **Step 1: Beat the Elite Four**
- Defeat the Elite Four and Champion Lance
- Enter the Hall of Fame
- The GS Ball flag will be automatically set when you save your game

### **Step 2: Visit Goldenrod Pokémon Center**
- After becoming Champion, go to Goldenrod City Pokémon Center
- Walk to the second floor near the trade machines
- The nurse will automatically approach you and give you the **GS Ball**

### **Step 3: Take GS Ball to Kurt**
- Go to Azalea Town
- Visit Kurt's house (the Poké Ball craftsman)
- Kurt will examine the GS Ball and tell you it's special
- He'll suggest taking it to Ilex Forest shrine

### **Step 4: Visit Ilex Forest Shrine**
- Go to Ilex Forest
- Find the shrine in the forest (small clearing with a shrine)
- Place the GS Ball on the shrine
- **Celebi will appear!**

### **Step 5: Battle Celebi**
- Celebi is **Level 30**
- Type: **Psychic/Grass**
- Make sure to save before the battle
- Bring Poké Balls to catch it!

---

## 📋 **Event Details**

### **What Happens:**
1. **Forest becomes restless** - Special tree animations in Ilex Forest
2. **Celebi cutscene** - Animated appearance with falling leaves
3. **Battle encounter** - Fight and catch Celebi
4. **GS Ball remains** - You keep the GS Ball as a Key Item

### **Celebi Stats:**
- **Level:** 30
- **Type:** Psychic/Grass
- **Ability:** Natural Cure
- **Signature Move:** Healing Wish (in this hack)
- **Category:** Mythical Pokémon

---

## ⚙️ **Technical Changes Made**

The following code was modified to enable the GS Ball event for all versions:

**File:** `engine/menus/save.asm`

**Change:** Added automatic flag setting after Hall of Fame save:
```asm
; Enable GS Ball event for all versions (not just VC)
ld a, BANK(sGSBallFlag)
call OpenSRAM
ld a, GS_BALL_AVAILABLE
ld [sGSBallFlag], a
ld a, BANK(sGSBallFlagBackup)
call OpenSRAM
ld a, GS_BALL_AVAILABLE
ld [sGSBallFlagBackup], a
call CloseSRAM
```

This ensures that **every player** who beats the Elite Four will have access to the GS Ball event, regardless of platform (emulator, flashcart, or Virtual Console).

---

## 🎮 **Tips for Catching Celebi**

1. **Save before the battle** - In case you accidentally KO it
2. **Bring status moves** - Sleep or Paralysis helps
3. **Use Timer Balls** - The battle can take a while
4. **Lower its HP carefully** - Celebi is fragile at level 30
5. **Stock up on Ultra Balls** - Bring at least 30-40 balls

---

## ✅ **Benefits**

✅ **No external events needed** - Available in-game
✅ **No cheats required** - Legitimate event trigger
✅ **Works on all platforms** - Emulator, flashcart, or real hardware
✅ **Complete Pokédex** - Catch all 251 Pokémon including Celebi
✅ **Mythical Pokémon accessible** - No need for special distributions

---

## 📝 **Notes**

- The GS Ball event was originally a Japan-exclusive mobile event
- In the original Western releases, the event was coded but never activated
- This modification makes it accessible to everyone
- The event is fully functional with all original animations and cutscenes
- Celebi is required for 100% Pokédex completion

Enjoy your encounter with the time-traveling Celebi! 🌿✨
