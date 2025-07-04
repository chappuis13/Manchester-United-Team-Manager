# Manchester United Team Manager
Project UAS Object Oriented Programming

## Inspiration

This project is inspired by my passion for football and in particular as a big Manchester United fan. I wanted to create a desktop application that helps manage football players on a team in a simple, structured, and user-friendly way. Manual player tracking is error-prone and inefficient, so I applied Object-Oriented Programming (OOP) principles to build a functional Football Team Manager.

## Features

- **Player Management**: Add football players with name, age, and position.
- **GUI Interface**: Interactive user interface built using Tkinter.
- **Coach Display**: Coach information is displayed automatically at the top (non-editable).
- **Save and Load**: Save players to a JSON file and load them back on the next session.
- **Clean Layout**: Form inputs are aligned, theme color styled to represent Manchester United.

## Technologies

- Python 3.x
- Tkinter for GUI
- JSON for data persistence
- Object-Oriented Programming concepts (inheritance, abstract classes, composition)

## Installation make git clone Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/chappuis13/Manchester-United-Team-Manager.git
    cd Manchester-United-Team-Manager
    ```

2. **Ensure Python is installed**:

    ```bash
    python --version
    ```

3. **No additional packages required** - uses only Python standard library


## How to Run Standard

1. **Make sure you have Python installed**:
   ```bash
   python --version
   ```

2. **Run the main program**:
   ```bash
   python main.py
   ```

3. **Usage Instructions**:
   - Fill in player name, age, and position
   - Click **Add Player** to see it added to the list
   - Click **Save Players** to save to file
   - Click **Load Players** to reload previously saved players

## Usage Guide

### Coach

- The coach is shown on top of the window as:
  ```
  👤 Coach: Ruben Amorim
  ```
- It is hardcoded and **cannot be modified by the user** through the GUI.

### Adding Players

- Fill in:
  - Name (e.g., Andre Onani)
  - Age (e.g., 29)
  - Position (e.g., GK)
- Then click **Add Player**

### Saving and Loading

- Click **Save Players** to store data into `data/players.json`
- Click **Load Players** to reload previously saved players

### Folder Structure

```
Manchester United Team Manager/
├── main.py
├── gui.py
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── player.py
│   ├── coach.py
│   └── team.py
├── data/
│   └── players.json  ← (auto-created)
├── football_icon.png
└── README.md
```

## Data Storage

- File: `data/players.json`
- Format:
```json
[
  {
    "name": "Andre Onani",
    "age": 29,
    "position": "GK"
  }
]
```

## Demo Video (YouTube)

Link (if applicable):  
[📺 Watch the demo](https://www.youtube.com/your-demo-video-link)

## Author

Nama: [Chairil Sutisna]  
NIM: [20230040056]

Developed as part of Object-Oriented Programming (OOP) final project.

## License

This project is for educational and personal learning purposes only.
