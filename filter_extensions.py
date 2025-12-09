import json
import sys
import os
import glob

def load_blocked_extensions(file_path):
    if not os.path.exists(file_path):
        print(f"Warning: Block file '{file_path} not found. Extensions will not be filtered.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print(f"Error: File '{file_path}' must contain a JSON list.")
                sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON '{file_path}': {e}")
        sys.exit(1)

def filter_extensions(data, remove_list):
    filtered_list = []
    removed_count = 0

    if not isinstance(data, list):
        print("Error: JSON is not a list.")
        return []

    remove_set = set(remove_list)

    for ext in data:
        if isinstance(ext, dict):
            pkg_name = ext.get('pkg')
            
            if pkg_name not in remove_set:
                filtered_list.append(ext)
            else:
                print(f"Removing: {ext.get('name')} ({pkg_name})")
                removed_count += 1

    print(f"\nOriginal: {len(data)}")
    print(f"Removed: {removed_count}")
    print(f"Updated: {len(filtered_list)}")
    return filtered_list

def cleanup_apks(filtered_data):
    apk_dir = 'apk'
    if not os.path.isdir(apk_dir):
        print(f"Warning: Directory '{apk_dir}' not found. Skipping APK cleanup.")
        return

    valid_apks = set()
    for ext in filtered_data:
        apk_filename = ext.get('apk')
        if apk_filename:
            valid_apks.add(apk_filename)

    print(f"\nTotal valid APKs identified: {len(valid_apks)}")

    current_apks = glob.glob(os.path.join(apk_dir, '*.apk'))
    removed_apk_count = 0

    for apk_path in current_apks:
        filename = os.path.basename(apk_path)

        if filename not in valid_apks:
            print(f"Deleting APK: {filename}")
            try:
                os.remove(apk_path)
                removed_apk_count += 1
            except OSError as e:
                print(f"Error deleting file {filename}: {e}")

    print(f"Total deleted APKs: {removed_apk_count}")


def main():
    original_file = 'original_index.json'
    blocklist_file = 'rm_extensions.json'
    output_file = 'index.json'
    output_file_min = 'index.min.json'

    if not os.path.exists(original_file):
        print(f"Error: File '{original_file}' not found.")
        print("Make sure the GitHub Action sync step has been completed.")
        sys.exit(1) 

    pkg_remove_list = load_blocked_extensions(blocklist_file)
    print(f"{len(pkg_remove_list)} Extensions loaded to remove.")

    try:
        with open(original_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON from '{original_file}': {e}")
        sys.exit(1)

    filtered_data = filter_extensions(data, pkg_remove_list)

    cleanup_apks(filtered_data)

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