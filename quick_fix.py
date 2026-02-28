#!/usr/bin/env python3
"""
Quick fix for the moveset update script
"""

import os
import re

def fix_pokemon_database():
    """Fix the pokemon database naming convention"""
    db_path = os.path.join(os.path.dirname(__file__), 'pokemon_database.py')
    
    # Read the current database
    with open(db_path, 'r') as f:
        content = f.read()
    
    # Replace all uppercase names with proper case
    # This is a simplified fix - just convert everything to title case
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        if line.strip().startswith("'") and ":" in line:
            # Extract the pokemon name
            start = line.find("'") + 1
            end = line.find("'", start)
            if start > 0 and end > start:
                old_name = line[start:end]
                # Convert to proper case
                if '_' in old_name:
                    parts = old_name.split('_')
                    new_name = ''.join(part.capitalize() for part in parts)
                else:
                    new_name = old_name.capitalize()
                
                # Special cases
                special_cases = {
                    'MrMime': 'MrMime',
                    'MimeJr': 'MimeJr', 
                    'NinetalesA': 'NinetalesA',
                    'VulpixA': 'VulpixA',
                    'WooperP': 'WooperP',
                    'CorsolaG': 'CorsolaG'
                }
                
                if new_name in special_cases:
                    new_name = special_cases[new_name]
                
                # Replace in line
                line = line.replace(f"'{old_name}'", f"'{new_name}'")
        
        fixed_lines.append(line)
    
    # Write back
    with open(db_path, 'w') as f:
        f.write('\n'.join(fixed_lines))
    
    print("✅ Fixed pokemon database naming convention")

def test_naming():
    """Test the naming function"""
    test_names = [
        'BULBASAUR', 'CHARMANDER', 'SQUIRTLE',
        'MR_MIME', 'MIME_JR', 'NINETALES_A',
        'VULPIX_A', 'WOOPER_P', 'CORSOLA_G'
    ]
    
    def to_proper_case(name):
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
        
        if '_' in name:
            parts = name.split('_')
            return ''.join(part.capitalize() for part in parts)
        else:
            return name.capitalize()
    
    print("Testing naming convention:")
    for name in test_names:
        proper = to_proper_case(name)
        print(f"  {name} -> {proper}")

if __name__ == "__main__":
    print("🔧 Quick Fix for Pokemon Moveset Update")
    print("=" * 50)
    
    test_naming()
    print()
    
    fix_pokemon_database()
    print()
    print("✅ Fix complete! Try running the update script again.")
