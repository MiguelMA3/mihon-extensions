import json
import sys
import os
import glob

PKG_REMOVE_LIST = [
    # --- PORN ---
    "eu.kanade.tachiyomi.extension.all.ahottie",
    "eu.kanade.tachiyomi.extension.all.asmhentai",
    "eu.kanade.tachiyomi.extension.all.ehentai",
    "eu.kanade.tachiyomi.extension.all.hentai3",
    "eu.kanade.tachiyomi.extension.all.hentaicosplay",
    "eu.kanade.tachiyomi.extension.all.hentaiera",
    "eu.kanade.tachiyomi.extension.all.hentaifox",
    "eu.kanade.tachiyomi.extension.all.hentaihand",
    "eu.kanade.tachiyomi.extension.all.hitomi",
    "eu.kanade.tachiyomi.extension.all.imhentai",
    "eu.kanade.tachiyomi.extension.all.mihentai",
    "eu.kanade.tachiyomi.extension.all.nhentaicom",
    "eu.kanade.tachiyomi.extension.all.simplyhentai",
    "eu.kanade.tachiyomi.extension.ar.arabshentai",
    "eu.kanade.tachiyomi.extension.ar.hentaislayer",
    "eu.kanade.tachiyomi.extension.ca.fansubscathentai",
    "eu.kanade.tachiyomi.extension.en.beehentai",
    "eu.kanade.tachiyomi.extension.en.hentai20",
    "eu.kanade.tachiyomi.extension.en.hentai2read",
    "eu.kanade.tachiyomi.extension.en.hentai3zcc",
    "eu.kanade.tachiyomi.extension.en.hentai4free",
    "eu.kanade.tachiyomi.extension.en.hentaidex",
    "eu.kanade.tachiyomi.extension.en.hentaidexy",
    "eu.kanade.tachiyomi.extension.en.hentaihere",
    "eu.kanade.tachiyomi.extension.en.hentaimanga",
    "eu.kanade.tachiyomi.extension.en.hentainexus",
    "eu.kanade.tachiyomi.extension.en.hentairead",
    "eu.kanade.tachiyomi.extension.en.hentaiwebtoon",
    "eu.kanade.tachiyomi.extension.en.hentaixcomic",
]

def filter_extensions(data):
    filtered_list = []
    removed_count = 0

    if not isinstance(data, list):
        print("Error: JSON is not a list.")
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
    output_file = 'index.json'
    output_file_min = 'index.min.json'

    if not os.path.exists(original_file):
        print(f"Error: File '{original_file}' not found.")
        print("Make sure the GitHub Action sync step has been completed.")
        sys.exit(1) 

    try:
        with open(original_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON from '{original_file}': {e}")
        sys.exit(1)

    filtered_data = filter_extensions(data)

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