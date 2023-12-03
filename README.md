# File Sorting Script

This script is designed to organize files in your folders into specific subfolders based on their file types. It aims to simplify the clutter in your Downloads directory by categorizing files such as images, videos, audio, documents, and code files into distinct folders.

## Usage

Follow these steps to run the script:

1. **Requirements**: Ensure you have Python installed on your system.

2. **Clone the Repository**:
   - Clone this repository to your local machine using the following command:
     ```bash
     git clone https://github.com/harish-mm/WindowsFileSorter.git
     ```

3. **Navigate to the Script Directory**:
   - Open a terminal or command prompt.
   - Change your current directory to the location where the script is saved.

4. **Run the Script**:
   - Execute the script by running the following command:
     ```bash
     python fiel_sorter.py
     ```

5. **Review Organized Files**:
   - Once the script completes execution, check your Downloads folder.
   - Files should be organized into subfolders like 'Media', 'Images', 'Videos', 'Audio', etc.

## Customization

You can customize the script by modifying the `file_types` dictionary in the script. Add or remove file extensions and corresponding folder names according to your preferences.

```python
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


