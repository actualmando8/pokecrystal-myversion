#!/usr/bin/env python3
"""
Comprehensive Pokémon Moveset Update Execution Script
This script will update all 286 Pokémon movesets systematically
"""

import os
import re
import sys
from typing import Dict, List, Tuple, Optional

# Import our databases
from pokemon_database import POKEMON_DB, SPECIAL_MOVES, CATEGORY_PRIORITIES
from batch_moveset_update import MOVES_DB

class ComprehensiveMovesetUpdater:
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.evos_attacks_path = os.path.join(base_path, 'data', 'pokemon', 'evos_attacks.asm')
        self.base_stats_path = os.path.join(base_path, 'data', 'pokemon', 'base_stats')
        
        # Load current evos_attacks file
        with open(self.evos_attacks_path, 'r') as f:
            self.original_content = f.read()
        
        self.updated_content = self.original_content
        self.update_log = []
        
    def get_moves_by_priority(self, pokemon_name: str, priorities: List[str]) -> List[str]:
        """Get moves based on priority list"""
        moves = []
        pokemon_data = POKEMON_DB[pokemon_name]
        types = pokemon_data['types']
        
        for priority in priorities:
            if priority == 'basic':
                # Basic moves of primary type
                primary_type = types[0]
                for move, data in MOVES_DB.items():
                    if data['type'] == primary_type and data['level'] == 'basic':
                        if move not in moves:
                            moves.append(move)
            
            elif priority == 'intermediate':
                # Intermediate moves of primary and secondary types
                for type_name in types:
                    for move, data in MOVES_DB.items():
                        if data['type'] == type_name and data['level'] == 'intermediate':
                            if move not in moves:
                                moves.append(move)
            
            elif priority == 'advanced':
                # Advanced moves of all types
                for type_name in types:
                    for move, data in MOVES_DB.items():
                        if data['type'] == type_name and data['level'] == 'advanced':
                            if move not in moves:
                                moves.append(move)
            
            elif priority == 'ultimate':
                # Ultimate moves
                for type_name in types:
                    for move, data in MOVES_DB.items():
                        if data['type'] == type_name and data['level'] == 'ultimate':
                            if move not in moves:
                                moves.append(move)
            
            elif priority == 'status':
                # Status moves
                status_moves = ['GROWL', 'TAIL_WHIP', 'HARDEN', 'WITHDRAW', 'DEFENSE_CURL', 
                               'GROWTH', 'AGILITY', 'SWORDS_DANCE', 'CALM_MIND', 'NASTY_PLOT']
                for move in status_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'coverage':
                # Coverage moves (different types)
                coverage_types = ['NORMAL', 'GROUND', 'ROCK', 'STEEL']
                for coverage_type in coverage_types:
                    if coverage_type not in types:
                        for move, data in MOVES_DB.items():
                            if data['type'] == coverage_type and data['level'] in ['intermediate', 'advanced']:
                                if move not in moves:
                                    moves.append(move)
                                    break
            
            elif priority == 'type_specific':
                # Type-specific moves
                for type_name in types:
                    for move, data in MOVES_DB.items():
                        if data['type'] == type_name:
                            if move not in moves:
                                moves.append(move)
            
            elif priority == 'signature':
                # Signature moves for this Pokémon
                if pokemon_name in SPECIAL_MOVES:
                    for move in SPECIAL_MOVES[pokemon_name]:
                        if move in MOVES_DB and move not in moves:
                            moves.append(move)
            
            elif priority == 'flying':
                # Flying moves
                flying_moves = ['PECK', 'GUST', 'WING_ATTACK', 'AIR_SLASH', 'FLY', 'BRAVE_BIRD', 'SKY_ATTACK']
                for move in flying_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'bug':
                # Bug moves
                bug_moves = ['BUG_BITE', 'X_SCISSOR', 'SIGNAL_BEAM', 'BUG_BUZZ', 'PIN_MISSILE', 'ATTACK_ORDER']
                for move in bug_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'water':
                # Water moves
                water_moves = ['BUBBLE', 'WATER_GUN', 'WATER_PULSE', 'SURF', 'HYDRO_PUMP', 'WATERFALL', 'HYDRO_CANNON']
                for move in water_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'fire':
                # Fire moves
                fire_moves = ['EMBER', 'FIRE_SPIN', 'FLAMETHROWER', 'FIRE_FANG', 'FIRE_BLAST', 'FLARE_BLITZ', 'INFERNO', 'BLAST_BURN']
                for move in fire_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'grass':
                # Grass moves
                grass_moves = ['VINE_WHIP', 'RAZOR_LEAF', 'LEAF_STORM', 'GIGA_DRAIN', 'POWER_WHIP', 'PETAL_DANCE', 'FRENZY_PLANT', 'LEAF_BLADE']
                for move in grass_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'electric':
                # Electric moves
                electric_moves = ['THUNDERSHOCK', 'SPARK', 'THUNDERBOLT', 'THUNDER_WAVE', 'THUNDER', 'DISCHARGE', 'VOLT_TACKLE', 'WILD_CHARGE']
                for move in electric_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'psychic':
                # Psychic moves
                psychic_moves = ['CONFUSION', 'PSYBEAM', 'PSYCHIC_M', 'CALM_MIND', 'FUTURE_SIGHT', 'PSYCH_UP', 'MIND_BLOWN']
                for move in psychic_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'fighting':
                # Fighting moves
                fighting_moves = ['LOW_KICK', 'KARATE_CHOP', 'BRICK_BREAK', 'DYNAMICPUNCH', 'CLOSE_COMBAT', 'FOCUS_PUNCH', 'SUPERPOWER']
                for move in fighting_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'dragon':
                # Dragon moves
                dragon_moves = ['DRAGON_RAGE', 'TWISTER', 'DRAGON_CLAW', 'DRAGON_PULSE', 'DRAGON_DANCE', 'OUTRAGE', 'DRAGON_ASCENT']
                for move in dragon_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'dark':
                # Dark moves
                dark_moves = ['BITE', 'PURSUIT', 'DARK_PULSE', 'CRUNCH', 'FOUL_PLAY', 'KNOCK_OFF', 'NIGHT_DAZE']
                for move in dark_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'steel':
                # Steel moves
                steel_moves = ['METAL_CLAW', 'IRON_HEAD', 'STEEL_WING', 'METEOR_MASH', 'IRON_DEFENSE', 'FLASH_CANNON', 'GYRO_BALL']
                for move in steel_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'fairy':
                # Fairy moves
                fairy_moves = ['CHARM', 'DAZZLING_GLEAM', 'MOONBLAST', 'PLAY_ROUGH', 'FAIRY_WIND', 'MISTY_EXPLOSION']
                for move in fairy_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'ghost':
                # Ghost moves
                ghost_moves = ['LICK', 'ASTONISH', 'SHADOW_BALL', 'HEX', 'SHADOW_CLAW', 'POLTERGEIST', 'DESTINY_BOND']
                for move in ghost_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'ice':
                # Ice moves
                ice_moves = ['POWDER_SNOW', 'ICE_SHARD', 'ICE_BEAM', 'ICY_WIND', 'BLIZZARD', 'FROST_BREATH', 'GLACIAL_LANCE']
                for move in ice_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'poison':
                # Poison moves
                poison_moves = ['POISON_STING', 'SLUDGE', 'SLUDGE_BOMB', 'POISON_JAB', 'GUNK_SHOT', 'TOXIC', 'VENOSHOCK']
                for move in poison_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'ground':
                # Ground moves
                ground_moves = ['SAND_ATTACK', 'MUD_SLAP', 'EARTHQUAKE', 'DIG', 'BONEMERANG', 'FISSURE']
                for move in ground_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'rock':
                # Rock moves
                rock_moves = ['ROCK_THROW', 'DEFENSE_CURL', 'ROCK_SLIDE', 'STEALTH_ROCK', 'STONE_EDGE', 'ROCK_TOMB', 'HEAD_SMASH']
                for move in rock_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'normal':
                # Normal moves
                normal_moves = ['TACKLE', 'GROWL', 'BODY_SLAM', 'HYPER_BEAM', 'EXPLOSION', 'GIGA_IMPACT', 'BOOMBURST', 'HYPER_VOICE']
                for move in normal_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'iconic':
                # Iconic moves (for special Pokémon)
                iconic_moves = ['THUNDERBOLT', 'PSYCHIC_M', 'FLAMETHROWER', 'SURF', 'ICE_BEAM']
                for move in iconic_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
            
            elif priority == 'unique':
                # Unique moves based on Pokémon characteristics
                unique_moves = []
                if 'GRASS' in types:
                    unique_moves.extend(['LEECH_SEED', 'SPORE', 'SYNTHESIS'])
                if 'FIRE' in types:
                    unique_moves.extend(['SUNNY_DAY', 'WILL_O_WISP'])
                if 'WATER' in types:
                    unique_moves.extend(['RAIN_DANCE', 'WATER_SPORT'])
                if 'ELECTRIC' in types:
                    unique_moves.extend(['THUNDER_WAVE', 'CHARGE'])
                if 'PSYCHIC' in types:
                    unique_moves.extend(['TELEPORT', 'MIRACLE_EYE'])
                if 'DARK' in types:
                    unique_moves.extend(['TAUNT', 'TAUNT_DANCE'])
                if 'FAIRY' in types:
                    unique_moves.extend(['MOONLIGHT', 'AROMATHERAPY'])
                
                for move in unique_moves:
                    if move in MOVES_DB and move not in moves:
                        moves.append(move)
        
        return moves[:12]  # Limit to prevent too many moves
    
    def generate_level_distribution(self, pokemon_name: str) -> List[int]:
        """Generate level distribution based on evolution stage"""
        pokemon_data = POKEMON_DB[pokemon_name]
        stage = pokemon_data['stage']
        evo_stage = pokemon_data['evo_stage']
        category = pokemon_data['category']
        
        # Adjust levels based on category
        if category in ['legendary', 'mythic']:
            base_levels = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        elif category in ['pseudo_legendary']:
            base_levels = [1, 8, 15, 22, 30, 38, 46, 54, 62, 70, 78, 86]
        elif category in ['starter']:
            base_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
        elif category in ['baby']:
            base_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40]
        else:
            base_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
        
        # Adjust for evolution stage
        if evo_stage == 1:
            # Single-stage Pokémon
            return base_levels[:10]
        elif evo_stage == 2:
            # Two-stage Pokémon
            if stage == 1:
                return base_levels[:8]
            else:
                return base_levels[2:12]
        else:
            # Three-stage Pokémon
            if stage == 1:
                return base_levels[:8]
            elif stage == 2:
                return base_levels[2:12]
            else:
                return base_levels[4:14]
        
        return base_levels
    
    def generate_moveset(self, pokemon_name: str) -> List[Tuple[int, str]]:
        """Generate comprehensive moveset for a Pokémon"""
        if pokemon_name not in POKEMON_DB:
            return []
        
        pokemon_data = POKEMON_DB[pokemon_name]
        category = pokemon_data['category']
        stage = pokemon_data['stage']
        evo_stage = pokemon_data['evo_stage']
        
        # Get level distribution
        levels = self.generate_level_distribution(pokemon_name)
        
        # Get category priorities
        if category in CATEGORY_PRIORITIES:
            priorities = CATEGORY_PRIORITIES[category]
        else:
            # Default priorities
            priorities = ['basic', 'status', 'intermediate', 'type_specific', 'advanced', 'coverage', 'ultimate']
        
        # Generate moves for each level
        moveset = []
        available_moves = self.get_moves_by_priority(pokemon_name, priorities)
        
        # Distribute moves across levels
        for i, level in enumerate(levels):
            if i < len(available_moves):
                move = available_moves[i]
                moveset.append((level, move))
            else:
                # Add signature moves if available
                if pokemon_name in SPECIAL_MOVES:
                    signature_moves = SPECIAL_MOVES[pokemon_name]
                    if i - len(available_moves) < len(signature_moves):
                        move = signature_moves[i - len(available_moves)]
                        moveset.append((level, move))
        
        return moveset
    
    def generate_moveset_text(self, pokemon_name: str) -> str:
        """Generate moveset text for a Pokémon"""
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
    
    def update_pokemon_moveset(self, pokemon_name: str) -> bool:
        """Update a single Pokémon's moveset"""
        try:
            new_moveset = self.generate_moveset_text(pokemon_name)
            if not new_moveset:
                return False
            
            # Convert to proper naming convention (PascalCase)
            proper_name = self.to_proper_case(pokemon_name)
            
            # Find and replace existing moveset
            pattern = f"{proper_name}EvosAttacks:.*?db 0 ; no more level-up moves"
            replacement = new_moveset.strip()
            
            if re.search(pattern, self.updated_content, flags=re.DOTALL):
                self.updated_content = re.sub(pattern, replacement, self.updated_content, flags=re.DOTALL)
                self.update_log.append(f"✅ Updated {pokemon_name}")
                return True
            else:
                self.update_log.append(f"❌ Could not find {pokemon_name} moveset")
                return False
                
        except Exception as e:
            self.update_log.append(f"❌ Error updating {pokemon_name}: {str(e)}")
            return False
    
    def to_proper_case(self, name: str) -> str:
        """Convert pokemon name to proper case format used in file"""
        # Handle special cases
        special_cases = {
            'MR_MIME': 'MrMime',
            'MIME_JR': 'MimeJr',
            'NINETALES_A': 'NinetalesA',
            'VULPIX_A': 'VulpixA',
            'WOOPER_P': 'WooperP',
            'CORSOLA_G': 'CorsolaG',
        }
        
        if name in special_cases:
            return special_cases[name]
        
        # Handle standard cases
        if '_' in name:
            parts = name.split('_')
            return ''.join(part.capitalize() for part in parts)
        else:
            return name.capitalize()
    
    def update_all_movesets(self) -> bool:
        """Update all Pokémon movesets"""
        print("🚀 Starting comprehensive moveset update...")
        print(f"📊 Total Pokémon to update: {len(POKEMON_DB)}")
        print()
        
        # Group Pokémon by category for better progress tracking
        categories = {}
        for pokemon_name, data in POKEMON_DB.items():
            category = data['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(pokemon_name)
        
        # Update by category
        total_updated = 0
        for category, pokemon_list in sorted(categories.items()):
            print(f"📂 Updating {category} Pokémon ({len(pokemon_list)}):")
            
            category_updated = 0
            for pokemon_name in sorted(pokemon_list):
                if self.update_pokemon_moveset(pokemon_name):
                    category_updated += 1
                    total_updated += 1
            
            print(f"   ✅ {category_updated}/{len(pokemon_list)} updated")
            print()
        
        # Write updated content
        try:
            with open(self.evos_attacks_path, 'w') as f:
                f.write(self.updated_content)
            print(f"💾 Successfully wrote updated movesets to {self.evos_attacks_path}")
        except Exception as e:
            print(f"❌ Error writing file: {str(e)}")
            return False
        
        # Print summary
        print()
        print("📋 UPDATE SUMMARY:")
        print(f"   ✅ Total Pokémon updated: {total_updated}/{len(POKEMON_DB)}")
        print(f"   📊 Success rate: {total_updated/len(POKEMON_DB)*100:.1f}%")
        print()
        
        # Print errors if any
        errors = [log for log in self.update_log if log.startswith("❌")]
        if errors:
            print("⚠️  ERRORS ENCOUNTERED:")
            for error in errors:
                print(f"   {error}")
            print()
        
        return total_updated > 0
    
    def create_backup(self):
        """Create backup of original file"""
        backup_path = self.evos_attacks_path + ".backup"
        try:
            with open(backup_path, 'w') as f:
                f.write(self.original_content)
            print(f"💾 Backup created: {backup_path}")
        except Exception as e:
            print(f"❌ Error creating backup: {str(e)}")

def main():
    """Main execution function"""
    print("=" * 60)
    print("🎮 POKÉMON COMPREHENSIVE MOVESET UPDATER")
    print("=" * 60)
    print()
    
    # Get base path
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(f"📁 Base path: {base_path}")
    print(f"📁 Evos attacks file: {os.path.join(base_path, 'data', 'pokemon', 'evos_attacks.asm')}")
    print()
    
    # Initialize updater
    updater = ComprehensiveMovesetUpdater(base_path)
    
    # Create backup
    print("🔒 Creating backup...")
    updater.create_backup()
    print()
    
    # Update all movesets
    success = updater.update_all_movesets()
    
    if success:
        print()
        print("🎉 MOVESET UPDATE COMPLETED SUCCESSFULLY!")
        print()
        print("📋 NEXT STEPS:")
        print("   1. Review updated movesets in data/pokemon/evos_attacks.asm")
        print("   2. Update TM learnsets in data/pokemon/base_stats/*.asm files")
        print("   3. Test compilation with 'make'")
        print("   4. Verify game balance and progression")
        print("   5. Test in-game to ensure moves work correctly")
        print()
        print("🔧 TROUBLESHOOTING:")
        print("   - If compilation fails, check for syntax errors")
        print("   - If moves don't work, verify move constants exist")
        print("   - If balance is off, adjust move levels or powers")
        print()
    else:
        print()
        print("❌ MOVESET UPDATE FAILED!")
        print("   Please check the error messages above and try again.")
        print()
    
    print("=" * 60)

if __name__ == "__main__":
    main()
