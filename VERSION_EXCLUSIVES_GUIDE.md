# Pokémon Crystal - Version Exclusive Pokémon

In the original Gold/Silver/Crystal games, certain Pokémon were exclusive to specific versions. This guide documents which Pokémon need to be made available in Crystal.

## Version-Exclusive Pokémon (Gold/Silver)

### **Gold Exclusives** (Need to add to Crystal):
- **Mankey** / Primeape
- **Growlithe** / Arcanine
- **Spinarak** / Ariados
- **Gligar** → Gliscor
- **Teddiursa** / Ursaring
- **Mantine** (baby: Mantyke)

### **Silver Exclusives** (Need to add to Crystal):
- **Vulpix** / Ninetales (+ Alolan forms)
- **Meowth** / Persian
- **Ledyba** / Ledian
- **Delibird**
- **Skarmory**
- **Phanpy** / Donphan**

### **Already Available in Crystal**:
Most Pokémon are available in Crystal, including:
- All three starters (Chikorita, Cyndaquil, Totodile)
- Both legendary beasts roaming (Raikou, Entei)
- Suicune (special encounter)
- Ho-Oh and Lugia (both available with Rainbow/Silver Wing)
- Most common Pokémon

## Recommended Wild Encounter Additions

To make all Pokémon available in Crystal without trading, add these encounters:

### **Route Additions:**

**Route 42** (Gold exclusives):
- Add **Mankey** (Grass, Morning/Day)
- Add **Growlithe** (Grass, Morning/Day)

**Route 33** (Gold exclusives):
- Add **Teddiursa** (Grass, Night)
- Add **Spinarak** (Grass, Night)

**Route 40/41** (Gold exclusive):
- Add **Mantine** (Surfing, any time)

**Route 36** (Silver exclusives):
- Add **Vulpix** (Grass, Morning/Day)
- Add **Meowth** (Grass, any time)

**Route 37** (Silver exclusives):
- Add **Ledyba** (Grass, Morning)

**Ice Path** (Silver exclusive):
- Add **Delibird** (Grass, any time)

**Route 45** (Silver exclusives):
- Add **Skarmory** (Grass, Morning/Day)
- Add **Phanpy** (Grass, any time)

**Route 46** (Gold exclusive):
- Add **Gligar** (Grass, Night)

## Evolution Items Availability

Make sure these items are available for the new item-based evolutions:

- **King's Rock**: Slowpoke Well, held by wild Slowpoke (5% chance)
- **Metal Coat**: Magnet Train station, held by wild Magnemite (5% chance)
- **Dragon Scale**: Dragon's Den, held by wild Horsea/Seadra (5% chance)
- **Up-Grade**: Silph Co., one-time gift from scientist

## Implementation Notes

1. **Wild encounter files** are located in `data/wild/`
2. **Johto grass encounters**: `data/wild/johto_grass.asm`
3. **Johto water encounters**: `data/wild/johto_water.asm`
4. **Kanto encounters**: `data/wild/kanto_grass.asm` and `data/wild/kanto_water.asm`

Each route has encounter slots for different times of day (Morning, Day, Night) and different encounter types (Grass, Water, Fishing).

## Benefits of Making All Pokémon Available:

✅ **Complete Pokédex solo** - No need for multiple games
✅ **Better single-player experience** - All content accessible
✅ **Balanced distribution** - Pokémon placed in thematically appropriate locations
✅ **No version exclusivity** - Crystal becomes the definitive version

## Next Steps:

To implement these changes, you'll need to:
1. Edit wild encounter tables in `data/wild/johto_grass.asm`
2. Edit water encounter tables in `data/wild/johto_water.asm`
3. Ensure evolution items are available (already in game)
4. Test that all Pokémon are catchable
5. Verify encounter rates are balanced
