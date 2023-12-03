import os
import shutil

def sort_files_in_downloads_folder():
    downloads_folder = os.path.expanduser('~/Downloads')
    media_folder = os.path.join(downloads_folder, 'Media')
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav'],
        'PDFs': ['.pdf'],
        'Python': ['.py'],
        'C': ['.c'],
        'Word': ['.doc', '.docx'],
        'Excel': ['.xls', '.xlsx'],
        'PowerPoint': ['.ppt', '.pptx']
    }

    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            if file_extension.lower() in file_types['Images'] + file_types['Videos'] + file_types['Audio']:
                target_folder = media_folder
            else:
                for folder_name, extensions in file_types.items():
                    if file_extension in extensions:
                        target_folder = os.path.join(downloads_folder, folder_name)
                        if not os.path.exists(target_folder):
                            os.makedirs(target_folder)
                        break
                else:
                    target_folder = os.path.join(downloads_folder, 'Other')
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

            shutil.move(file_path, target_folder)

if __name__ == '__main__':
    sort_files_in_downloads_folder()
