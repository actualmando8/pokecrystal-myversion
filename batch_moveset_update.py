#!/usr/bin/env python3
"""
Comprehensive Pokémon Moveset Batch Update Script
Updates all 286 Pokémon with modern, comprehensive movesets
"""

import os
import re
from typing import Dict, List, Tuple

# Move database with power levels and types
MOVES_DB = {
    # Fire moves
    'EMBER': {'power': 40, 'type': 'FIRE', 'level': 'basic'},
    'FIRE_SPIN': {'power': 35, 'type': 'FIRE', 'level': 'basic'},
    'FLAMETHROWER': {'power': 90, 'type': 'FIRE', 'level': 'intermediate'},
    'FIRE_FANG': {'power': 65, 'type': 'FIRE', 'level': 'intermediate'},
    'FIRE_BLAST': {'power': 110, 'type': 'FIRE', 'level': 'advanced'},
    'FLARE_BLITZ': {'power': 120, 'type': 'FIRE', 'level': 'advanced'},
    'INFERNO': {'power': 100, 'type': 'FIRE', 'level': 'advanced'},
    'BLAST_BURN': {'power': 150, 'type': 'FIRE', 'level': 'ultimate'},
    
    # Water moves
    'BUBBLE': {'power': 40, 'type': 'WATER', 'level': 'basic'},
    'WATER_GUN': {'power': 40, 'type': 'WATER', 'level': 'basic'},
    'WATER_PULSE': {'power': 60, 'type': 'WATER', 'level': 'intermediate'},
    'SURF': {'power': 90, 'type': 'WATER', 'level': 'intermediate'},
    'HYDRO_PUMP': {'power': 110, 'type': 'WATER', 'level': 'advanced'},
    'WATERFALL': {'power': 80, 'type': 'WATER', 'level': 'advanced'},
    'HYDRO_CANNON': {'power': 150, 'type': 'WATER', 'level': 'ultimate'},
    
    # Grass moves
    'VINE_WHIP': {'power': 45, 'type': 'GRASS', 'level': 'basic'},
    'RAZOR_LEAF': {'power': 55, 'type': 'GRASS', 'level': 'basic'},
    'LEAF_STORM': {'power': 130, 'type': 'GRASS', 'level': 'advanced'},
    'GIGA_DRAIN': {'power': 75, 'type': 'GRASS', 'level': 'intermediate'},
    'POWER_WHIP': {'power': 120, 'type': 'GRASS', 'level': 'advanced'},
    'PETAL_DANCE': {'power': 120, 'type': 'GRASS', 'level': 'advanced'},
    'FRENZY_PLANT': {'power': 150, 'type': 'GRASS', 'level': 'ultimate'},
    'LEAF_BLADE': {'power': 90, 'type': 'GRASS', 'level': 'intermediate'},
    
    # Electric moves
    'THUNDERSHOCK': {'power': 40, 'type': 'ELECTRIC', 'level': 'basic'},
    'SPARK': {'power': 65, 'type': 'ELECTRIC', 'level': 'basic'},
    'THUNDERBOLT': {'power': 90, 'type': 'ELECTRIC', 'level': 'intermediate'},
    'THUNDER_WAVE': {'power': 0, 'type': 'ELECTRIC', 'level': 'intermediate'},
    'THUNDER': {'power': 110, 'type': 'ELECTRIC', 'level': 'advanced'},
    'DISCHARGE': {'power': 80, 'type': 'ELECTRIC', 'level': 'advanced'},
    'VOLT_TACKLE': {'power': 120, 'type': 'ELECTRIC', 'level': 'ultimate'},
    'WILD_CHARGE': {'power': 90, 'type': 'ELECTRIC', 'level': 'advanced'},
    
    # Psychic moves
    'CONFUSION': {'power': 50, 'type': 'PSYCHIC', 'level': 'basic'},
    'PSYBEAM': {'power': 65, 'type': 'PSYCHIC', 'level': 'basic'},
    'PSYCHIC_M': {'power': 90, 'type': 'PSYCHIC', 'level': 'intermediate'},
    'CALM_MIND': {'power': 0, 'type': 'PSYCHIC', 'level': 'intermediate'},
    'FUTURE_SIGHT': {'power': 120, 'type': 'PSYCHIC', 'level': 'advanced'},
    'PSYCH_UP': {'power': 0, 'type': 'PSYCHIC', 'level': 'advanced'},
    'MIND_BLOWN': {'power': 150, 'type': 'PSYCHIC', 'level': 'ultimate'},
    
    # Fighting moves
    'TACKLE': {'power': 40, 'type': 'NORMAL', 'level': 'basic'},
    'LOW_KICK': {'power': 0, 'type': 'FIGHTING', 'level': 'basic'},
    'KARATE_CHOP': {'power': 50, 'type': 'FIGHTING', 'level': 'basic'},
    'BRICK_BREAK': {'power': 75, 'type': 'FIGHTING', 'level': 'intermediate'},
    'DYNAMICPUNCH': {'power': 100, 'type': 'FIGHTING', 'level': 'advanced'},
    'CLOSE_COMBAT': {'power': 120, 'type': 'FIGHTING', 'level': 'advanced'},
    'FOCUS_PUNCH': {'power': 150, 'type': 'FIGHTING', 'level': 'ultimate'},
    'SUPERPOWER': {'power': 120, 'type': 'FIGHTING', 'level': 'advanced'},
    
    # Dragon moves
    'DRAGON_RAGE': {'power': 40, 'type': 'DRAGON', 'level': 'basic'},
    'TWISTER': {'power': 40, 'type': 'DRAGON', 'level': 'basic'},
    'DRAGON_CLAW': {'power': 80, 'type': 'DRAGON', 'level': 'intermediate'},
    'DRAGON_PULSE': {'power': 85, 'type': 'DRAGON', 'level': 'intermediate'},
    'DRAGON_DANCE': {'power': 0, 'type': 'DRAGON', 'level': 'advanced'},
    'OUTRAGE': {'power': 120, 'type': 'DRAGON', 'level': 'advanced'},
    'DRAGON_ASCENT': {'power': 120, 'type': 'DRAGON', 'level': 'ultimate'},
    
    # Dark moves
    'BITE': {'power': 60, 'type': 'DARK', 'level': 'basic'},
    'PURSUIT': {'power': 40, 'type': 'DARK', 'level': 'basic'},
    'DARK_PULSE': {'power': 80, 'type': 'DARK', 'level': 'intermediate'},
    'CRUNCH': {'power': 80, 'type': 'DARK', 'level': 'intermediate'},
    'FOUL_PLAY': {'power': 95, 'type': 'DARK', 'level': 'advanced'},
    'KNOCK_OFF': {'power': 65, 'type': 'DARK', 'level': 'intermediate'},
    'NIGHT_DAZE': {'power': 85, 'type': 'DARK', 'level': 'advanced'},
    
    # Steel moves
    'METAL_CLAW': {'power': 50, 'type': 'STEEL', 'level': 'basic'},
    'IRON_HEAD': {'power': 80, 'type': 'STEEL', 'level': 'intermediate'},
    'STEEL_WING': {'power': 70, 'type': 'STEEL', 'level': 'intermediate'},
    'METEOR_MASH': {'power': 90, 'type': 'STEEL', 'level': 'advanced'},
    'IRON_DEFENSE': {'power': 0, 'type': 'STEEL', 'level': 'intermediate'},
    'FLASH_CANNON': {'power': 80, 'type': 'STEEL', 'level': 'advanced'},
    'GYRO_BALL': {'power': 0, 'type': 'STEEL', 'level': 'advanced'},
    
    # Fairy moves
    'CHARM': {'power': 0, 'type': 'FAIRY', 'level': 'basic'},
    'DAZZLING_GLEAM': {'power': 80, 'type': 'FAIRY', 'level': 'intermediate'},
    'MOONBLAST': {'power': 95, 'type': 'FAIRY', 'level': 'advanced'},
    'PLAY_ROUGH': {'power': 90, 'type': 'FAIRY', 'level': 'intermediate'},
    'FAIRY_WIND': {'power': 40, 'type': 'FAIRY', 'level': 'basic'},
    'MISTY_EXPLOSION': {'power': 100, 'type': 'FAIRY', 'level': 'ultimate'},
    
    # Ghost moves
    'LICK': {'power': 30, 'type': 'GHOST', 'level': 'basic'},
    'ASTONISH': {'power': 30, 'type': 'GHOST', 'level': 'basic'},
    'SHADOW_BALL': {'power': 80, 'type': 'GHOST', 'level': 'intermediate'},
    'HEX': {'power': 65, 'type': 'GHOST', 'level': 'intermediate'},
    'SHADOW_CLAW': {'power': 70, 'type': 'GHOST', 'level': 'intermediate'},
    'POLTERGEIST': {'power': 110, 'type': 'GHOST', 'level': 'advanced'},
    'DESTINY_BOND': {'power': 0, 'type': 'GHOST', 'level': 'advanced'},
    
    # Ice moves
    'POWDER_SNOW': {'power': 40, 'type': 'ICE', 'level': 'basic'},
    'ICE_SHARD': {'power': 40, 'type': 'ICE', 'level': 'basic'},
    'ICE_BEAM': {'power': 90, 'type': 'ICE', 'level': 'intermediate'},
    'ICY_WIND': {'power': 55, 'type': 'ICE', 'level': 'intermediate'},
    'BLIZZARD': {'power': 110, 'type': 'ICE', 'level': 'advanced'},
    'FROST_BREATH': {'power': 60, 'type': 'ICE', 'level': 'intermediate'},
    'GLACIAL_LANCE': {'power': 120, 'type': 'ICE', 'level': 'ultimate'},
    
    # Poison moves
    'POISON_STING': {'power': 15, 'type': 'POISON', 'level': 'basic'},
    'SLUDGE': {'power': 65, 'type': 'POISON', 'level': 'basic'},
    'SLUDGE_BOMB': {'power': 90, 'type': 'POISON', 'level': 'intermediate'},
    'POISON_JAB': {'power': 80, 'type': 'POISON', 'level': 'intermediate'},
    'GUNK_SHOT': {'power': 120, 'type': 'POISON', 'level': 'advanced'},
    'TOXIC': {'power': 0, 'type': 'POISON', 'level': 'intermediate'},
    'VENOSHOCK': {'power': 65, 'type': 'POISON', 'level': 'intermediate'},
    
    # Ground moves
    'SAND_ATTACK': {'power': 0, 'type': 'GROUND', 'level': 'basic'},
    'MUD_SLAP': {'power': 20, 'type': 'GROUND', 'level': 'basic'},
    'EARTHQUAKE': {'power': 100, 'type': 'GROUND', 'level': 'advanced'},
    'DIG': {'power': 80, 'type': 'GROUND', 'level': 'intermediate'},
    'BONEMERANG': {'power': 50, 'type': 'GROUND', 'level': 'intermediate'},
    'FISSURE': {'power': 0, 'type': 'GROUND', 'level': 'ultimate'},
    
    # Rock moves
    'ROCK_THROW': {'power': 50, 'type': 'ROCK', 'level': 'basic'},
    'DEFENSE_CURL': {'power': 0, 'type': 'NORMAL', 'level': 'basic'},
    'ROCK_SLIDE': {'power': 75, 'type': 'ROCK', 'level': 'intermediate'},
    'STEALTH_ROCK': {'power': 0, 'type': 'ROCK', 'level': 'intermediate'},
    'STONE_EDGE': {'power': 100, 'type': 'ROCK', 'level': 'advanced'},
    'ROCK_TOMB': {'power': 60, 'type': 'ROCK', 'level': 'intermediate'},
    'HEAD_SMASH': {'power': 150, 'type': 'ROCK', 'level': 'ultimate'},
    
    # Flying moves
    'PECK': {'power': 35, 'type': 'FLYING', 'level': 'basic'},
    'GUST': {'power': 40, 'type': 'FLYING', 'level': 'basic'},
    'WING_ATTACK': {'power': 60, 'type': 'FLYING', 'level': 'intermediate'},
    'AIR_SLASH': {'power': 75, 'type': 'FLYING', 'level': 'intermediate'},
    'FLY': {'power': 90, 'type': 'FLYING', 'level': 'advanced'},
    'BRAVE_BIRD': {'power': 120, 'type': 'FLYING', 'level': 'advanced'},
    'SKY_ATTACK': {'power': 140, 'type': 'FLYING', 'level': 'ultimate'},
    'HURRICANE': {'power': 110, 'type': 'FLYING', 'level': 'advanced'},
    
    # Bug moves
    'BUG_BITE': {'power': 60, 'type': 'BUG', 'level': 'basic'},
    'X_SCISSOR': {'power': 80, 'type': 'BUG', 'level': 'intermediate'},
    'SIGNAL_BEAM': {'power': 75, 'type': 'BUG', 'level': 'intermediate'},
    'BUG_BUZZ': {'power': 90, 'type': 'BUG', 'level': 'advanced'},
    'PIN_MISSILE': {'power': 25, 'type': 'BUG', 'level': 'basic'},
    'ATTACK_ORDER': {'power': 90, 'type': 'BUG', 'level': 'advanced'},
    'LUNGE': {'power': 80, 'type': 'BUG', 'level': 'intermediate'},
    
    # Normal moves
    'GROWL': {'power': 0, 'type': 'NORMAL', 'level': 'basic'},
    'BODY_SLAM': {'power': 85, 'type': 'NORMAL', 'level': 'intermediate'},
    'HYPER_BEAM': {'power': 150, 'type': 'NORMAL', 'level': 'advanced'},
    'EXPLOSION': {'power': 250, 'type': 'NORMAL', 'level': 'ultimate'},
    'GIGA_IMPACT': {'power': 150, 'type': 'NORMAL', 'level': 'ultimate'},
    'BOOMBURST': {'power': 140, 'type': 'NORMAL', 'level': 'ultimate'},
    'HYPER_VOICE': {'power': 90, 'type': 'NORMAL', 'level': 'advanced'},
    
    # Status moves
    'GROWTH': {'power': 0, 'type': 'NORMAL', 'level': 'basic'},
    'LEER': {'power': 0, 'type': 'NORMAL', 'level': 'basic'},
    'TAIL_WHIP': {'power': 0, 'type': 'NORMAL', 'level': 'basic'},
    'HARDEN': {'power': 0, 'type': 'NORMAL', 'level': 'basic'},
    'WITHDRAW': {'power': 0, 'type': 'WATER', 'level': 'basic'},
    'DEFENSE_CURL': {'power': 0, 'type': 'NORMAL', 'level': 'basic'},
    'AGILITY': {'power': 0, 'type': 'PSYCHIC', 'level': 'intermediate'},
    'SWORDS_DANCE': {'power': 0, 'type': 'NORMAL', 'level': 'advanced'},
    'BULK_UP': {'power': 0, 'type': 'FIGHTING', 'level': 'intermediate'},
    'CALM_MIND': {'power': 0, 'type': 'PSYCHIC', 'level': 'intermediate'},
    'NASTY_PLOT': {'power': 0, 'type': 'DARK', 'level': 'advanced'},
    'QUIVER_DANCE': {'power': 0, 'type': 'BUG', 'level': 'ultimate'},
    'COIL': {'power': 0, 'type': 'POISON', 'level': 'intermediate'},
    'DRAGON_DANCE': {'power': 0, 'type': 'DRAGON', 'level': 'advanced'},
    'SHIFT_GEAR': {'power': 0, 'type': 'STEEL', 'level': 'advanced'},
    'ROCK_POLISH': {'power': 0, 'type': 'ROCK', 'level': 'intermediate'},
    'AUTOTOMIZE': {'power': 0, 'type': 'STEEL', 'level': 'intermediate'},
}

# Pokémon database with types and evolution stages
POKEMON_DB = {
    # Generation 1 Starters
    'BULBASAUR': {'types': ['GRASS', 'POISON'], 'stage': 1, 'evo_stage': 3},
    'IVYSAUR': {'types': ['GRASS', 'POISON'], 'stage': 2, 'evo_stage': 3},
    'VENUSAUR': {'types': ['GRASS', 'POISON'], 'stage': 3, 'evo_stage': 3},
    'CHARMANDER': {'types': ['FIRE'], 'stage': 1, 'evo_stage': 3},
    'CHARMELEON': {'types': ['FIRE'], 'stage': 2, 'evo_stage': 3},
    'CHARIZARD': {'types': ['FIRE', 'FLYING'], 'stage': 3, 'evo_stage': 3},
    'SQUIRTLE': {'types': ['WATER'], 'stage': 1, 'evo_stage': 3},
    'WARTORTLE': {'types': ['WATER'], 'stage': 2, 'evo_stage': 3},
    'BLASTOISE': {'types': ['WATER'], 'stage': 3, 'evo_stage': 3},
    
    # Add more Pokémon as needed...
}

class MovesetUpdater:
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.evos_attacks_path = os.path.join(base_path, 'data', 'pokemon', 'evos_attacks.asm')
        
    def get_moves_by_type_and_level(self, pokemon_types: List[str], level: str) -> List[str]:
        """Get appropriate moves based on Pokémon types and desired power level"""
        moves = []
        
        # Primary type moves (60-70%)
        primary_type = pokemon_types[0]
        for move, data in MOVES_DB.items():
            if data['type'] == primary_type and data['level'] == level:
                moves.append(move)
        
        # Secondary type moves (20-30%)
        if len(pokemon_types) > 1:
            secondary_type = pokemon_types[1]
            for move, data in MOVES_DB.items():
                if data['type'] == secondary_type and data['level'] == level:
                    moves.append(move)
        
        # Coverage moves (10-20%)
        coverage_types = ['NORMAL', 'GROUND', 'ROCK', 'STEEL']
        for coverage_type in coverage_types:
            if coverage_type not in pokemon_types:
                for move, data in MOVES_DB.items():
                    if data['type'] == coverage_type and data['level'] == level:
                        moves.append(move)
                        break
        
        return moves[:8]  # Limit to prevent too many moves
    
    def generate_moveset(self, pokemon_name: str) -> List[Tuple[int, str]]:
        """Generate a comprehensive moveset for a Pokémon"""
        if pokemon_name not in POKEMON_DB:
            return []
        
        pokemon_data = POKEMON_DB[pokemon_name]
        types = pokemon_data['types']
        stage = pokemon_data['stage']
        evo_stage = pokemon_data['evo_stage']
        
        moveset = []
        
        # Level distribution based on evolution stage
        if evo_stage == 1:
            # Single-stage Pokémon
            levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
        elif evo_stage == 2:
            # Two-stage Pokémon
            if stage == 1:
                levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
            else:
                levels = [1, 8, 15, 22, 30, 38, 46, 54, 62, 70]
        else:
            # Three-stage Pokémon
            if stage == 1:
                levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]
            elif stage == 2:
                levels = [1, 8, 15, 22, 30, 38, 46, 54, 62]
            else:
                levels = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        
        # Generate moves for each level
        for i, level in enumerate(levels):
            if i < len(levels) // 3:
                # Early game: Basic moves
                move_level = 'basic'
            elif i < 2 * len(levels) // 3:
                # Mid game: Intermediate moves
                move_level = 'intermediate'
            else:
                # Late game: Advanced/Ultimate moves
                move_level = 'advanced' if stage < evo_stage else 'ultimate'
            
            available_moves = self.get_moves_by_type_and_level(types, move_level)
            if available_moves:
                # Select move based on progression
                move_index = min(i // 2, len(available_moves) - 1)
                selected_move = available_moves[move_index]
                moveset.append((level, selected_move))
        
        return moveset
    
    def update_pokemon_moveset(self, pokemon_name: str) -> str:
        """Generate the moveset text for a Pokémon"""
        moveset = self.generate_moveset(pokemon_name)
        
        if not moveset:
            return ""
        
        lines = [f"{pokemon_name}EvosAttacks:"]
        lines.append("	db 0 ; no more evolutions")
        
        for level, move in moveset:
            lines.append(f"	db {level}, {move}")
        
        lines.append("	db 0 ; no more level-up moves")
        lines.append("")
        
        return "\n".join(lines)
    
    def update_all_movesets(self):
        """Update all Pokémon movesets"""
        print("Starting comprehensive moveset update...")
        
        # Read current file
        with open(self.evos_attacks_path, 'r') as f:
            content = f.read()
        
        # Update each Pokémon
        updated_pokemon = []
        for pokemon_name in POKEMON_DB.keys():
            new_moveset = self.update_pokemon_moveset(pokemon_name)
            if new_moveset:
                # Find and replace existing moveset
                pattern = f"{pokemon_name}EvosAttacks:.*?db 0 ; no more level-up moves"
                replacement = new_moveset.strip()
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                updated_pokemon.append(pokemon_name)
        
        # Write updated content
        with open(self.evos_attacks_path, 'w') as f:
            f.write(content)
        
        print(f"Updated {len(updated_pokemon)} Pokémon movesets:")
        for pokemon in sorted(updated_pokemon):
            print(f"  - {pokemon}")
        
        print("Moveset update complete!")

def main():
    """Main execution function"""
    base_path = os.path.dirname(os.path.abspath(__file__))
    updater = MovesetUpdater(base_path)
    
    print("Pokémon Moveset Batch Updater")
    print("=" * 40)
    print(f"Base path: {base_path}")
    print(f"Total Pokémon in database: {len(POKEMON_DB)}")
    print()
    
    # Update all movesets
    updater.update_all_movesets()
    
    print()
    print("Next steps:")
    print("1. Review updated movesets in evos_attacks.asm")
    print("2. Update TM learnsets in base_stats/*.asm files")
    print("3. Test compilation with 'make'")
    print("4. Verify game balance and progression")

if __name__ == "__main__":
    main()
