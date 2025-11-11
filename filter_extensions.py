import json
import sys
import os
import glob

PKG_REMOVE_LIST = [
    # --- PORN ---
    "eu.kanade.tachiyomi.extension.all.nhentai",
]

def filter_extensions(data):
    filtered_list = []
    removed_count = 0

    if not isinstance(data, list):
        print("Erro: O JSON original não é uma lista.")
        return []

    for ext in data:
        if isinstance(ext, dict) and ext.get('pkg') not in PKG_REMOVE_LIST:
            filtered_list.append(ext)
        elif isinstance(ext, dict):
            print(f"Removing: {ext.get('name')} ({ext.get('pkg')})")
            removed_count += 1

    print(f"\nOriginal: {len(data)}")
    print(f"Removed: {removed_count}")
    print(f"Updated: {len(filtered_list)}")
    return filtered_list

def cleanup_apks(filtered_data)
def main():
    original_file = 'original_index.json'
    output_file = 'index.json'
    output_file_min = 'index.min.json'

    if not os.path.exists(original_file):
        print(f"Error: File '{original_file}' not found.")
        print("Make sure the GitHub Action download step has been completed.")
        sys.exit(1)

    try:
        with open(original_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON from '{original_file}': {e}")
        sys.exit(1)

    filtered_data = filter_extensions(data)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, indent=2, ensure_ascii=False)
        print(f"File filtered and saved to: {output_file}")
    except IOError as e:
        print(f"Error saving '{output_file}': {e}")
        sys.exit(1)

    try:
        with open(output_file_min, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, separators=(',', ':'), ensure_ascii=False)
        print(f"Minified file saved in: {output_file_min}")
    except IOError as e:
        print(f"Error saving '{output_file_min}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()