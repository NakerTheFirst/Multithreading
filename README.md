# Multithreading GUI Example with PyQt6
This project demonstrates the use of multithreading in a PyQt6 application to manage character appending and deleting to a `QLineEdit` widget, with real-time updates on a simple ASCII progress bar.

<br>
<p align="center"><img width="403" src="https://github.com/NakerTheFirst/Multithreading/blob/main/gui.png" alt="Image of an interface of a multithreading exemplary app"></p>
<p align="center">App's Graphical User Interface</p>

## Overview
The application features a main window with:
- A read-only `QLineEdit` where characters are appended and deleted.
- An ASCII progress bar that visually represents the percentage of characters in the `QLineEdit`.
- A text box to set the delay for deleting characters.
- A start button to initiate the threads.

## Functionality

- **Appending Characters**: Three threads (`thread1`, `thread2`, `thread3`) continuously append characters ('p', 's', 't') to the text box.
- **Deleting Characters**: A separate thread (`deleting_thread`) continuously removes the last character from the text box based on a user-defined delay.
- **Progress Bar**: Updates in real-time to reflect the current percentage of the maximum 40 characters allowed in the text box.

## Setup

### Prerequisites

Ensure you have Python installed along with PyQt6. You can install PyQt6 using pip if it's not already installed:

```bash
pip install PyQt6
```

## Running the Application
Clone this repository and navigate to the directory containing `multithreading.py`. Run the following command to start the application:
```bash
python multithreading.py
```


## Architecture
- **MainWindow**: Manages the UI and threads.
- **Worker**: Handles the appending of characters.
- **DeletingWorker**: Manages the deletion of characters.

Each worker is moved to a separate QThread to ensure that the GUI remains responsive.
