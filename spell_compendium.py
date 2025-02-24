import importlib.util
import os
from utils import RuneGenerator 

SPELLS_FOLDER = "spells"

def get_class_files():
    """Retrieve all class spell files in the spells/ directory."""
    class_files = []
    
    for filename in os.listdir(SPELLS_FOLDER):
        if filename.endswith("_spells.py"):
            class_name = filename.replace("_spells.py", "")
            class_files.append(class_name)
    
    return class_files

def gather_all_spells():
    """Dynamically import all spell lists from the spells folder."""
    all_spells = {}
    
    for class_name in get_class_files():
        module_path = os.path.join(SPELLS_FOLDER, f"{class_name}_spells.py")
        module_name = f"spells.{class_name}_spells"
        
        try:
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            spells_var_name = f"KNOWN_{class_name.upper()}_SPELLS"
            class_spells = getattr(module, spells_var_name, {})
            
            for spell_name, spell_func in class_spells.items():
                if spell_name not in all_spells:
                    all_spells[spell_name] = spell_func
        except Exception as e:
            print(f"Warning: Could not load {module_path} - {e}")
    
    return all_spells

def display_spell_info(spell_name, spell_func):
    """Display spell details and generate a rune image."""
    spell = spell_func()
    rune_gen = RuneGenerator(spell)
    rune_filename = f"{spell_name}_rune_example.png"
    rune_gen.generate_rune(rune_filename)
    
    print(spell)
    print("\n" + "-" * 50 + "\n")

def open_compendium():
    """Main function to interactively display spell information."""
    all_spells = gather_all_spells()
    
    if not all_spells:
        print("No spells found in any class files!")
        return
    
    while True:
        print("\nAvailable spells:")
        spell_names = sorted(all_spells.keys())
        for i, spell_name in enumerate(spell_names, 1):
            print(f"{i}. {spell_name}")
        
        choice = input("\nEnter a spell name (or 'quit' to exit): ").lower().strip()
        
        if choice == 'quit':
            break
        
        if choice in all_spells:
            display_spell_info(choice, all_spells[choice])
        else:
            try:
                choice_num = int(choice) - 1
                if 0 <= choice_num < len(spell_names):
                    selected_spell = spell_names[choice_num]
                    display_spell_info(selected_spell, all_spells[selected_spell])
                else:
                    print("Invalid number selection!")
            except ValueError:
                print("Spell not found! Please try again.")

if __name__ == "__main__":
    open_compendium()
