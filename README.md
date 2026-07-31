# Automated File Organizer

## Overview

The Automated File Organizer is a Python application that automatically organizes files into categorized folders based on their file extensions. It is designed to reduce desktop or downloads folder clutter by sorting files into predefined directories.

This project was created to strengthen Python skills in file system automation.

---

## Features

* Automatically scans a specified directory
* Organizes files into categorized folders
* Supports common file types including:

  * Documents
  * Images
  * Videos
  * Audio
  * Archives
  * Spreadsheets
  * Presentations
  * Code files
* Creates destination folders automatically if they do not exist
* Skips files that are already organized
* Logs every file operation to a log file

---

## Technologies Used

* Python 3
* pathlib
* shutil

---

## How It Works

1. The program scans a target directory.
2. Each file's extension is evaluated.
3. The file is matched to a predefined category.
4. If the category folder does not exist, it is created automatically.
5. The file is moved into the appropriate folder.
6. Record of every action is added to "organized_files.log" for auditing and troubleshooting.

---

## Example

### Before

```text
Downloads/
    report.pdf
    vacation.jpg
    budget.xlsx
    random.html
    video.mp4
    song.mp3
```

### After

```text
Downloads/
    Documents/
        report.pdf
        budget.xlsx

    Images/
        vacation.jpg

    Videos/
        video.mp4

    Audio/
        song.mp3

    Misc/
        random.html
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/travie-trav/python-file-organizer.git
```

Navigate to the project directory:

```bash
cd python-file-organizer
```

Run the program:

```bash
python main.py
```

---

## Configuration

Edit the source code to specify the directory you want to organize, or use the default current working directory.

Example:

```python
base = Path("C:\Users\YourName\Downloads")
```

You can also customize:

* Supported file extensions
* Folder names
* Destination directory

---

## Future Enhancements

The following features are planned for future versions:

* Recursive directory scanning
* Duplicate file detection
* Automatic filename conflict resolution
* ~~Logging~~ - **Completed 7/30/26**
* Dry-run mode to preview changes
* Command-line arguments 
* Scheduled execution using Windows Task Scheduler or cron

---

## Skills Demonstrated

This project demonstrates practical experience with:

* Python scripting
* File system automation
* Working with file paths
* Standard library usage
* Writing maintainable, readable code
* Logging

---

## License

This project is provided for educational and portfolio purposes.
