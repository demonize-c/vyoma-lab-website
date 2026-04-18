import os

PEOPLE_ROOT = 'images/people'

def run():
    for root, dirs, files in os.walk(PEOPLE_ROOT):
        # We only want to delete original images in the base category folders
        # not the ones in sm/md/lg/placeholder subfolders we just created.
        if any(s in root for s in ['sm', 'md', 'lg', 'placeholder']):
            continue
            
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                path = os.path.join(root, file)
                print(f"Deleting original source: {path}")
                os.remove(path)

if __name__ == "__main__":
    run()
