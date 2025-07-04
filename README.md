# Manchester United Team Manager
Project UAS Object Oriented Programming

## Inspiration

This project is inspired by my passion for football and specifically my admiration for Manchester United. I wanted to create a desktop application that helps manage football players on a team in a simple, structured, and user-friendly way. Manual player tracking is error-prone and inefficient, so I applied Object-Oriented Programming (OOP) principles to build a functional Football Team Manager.

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

## How to Run

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
  👤 Coach: Erik ten Hag
  ```
- It is hardcoded and **cannot be modified by the user** through the GUI.

### Adding Players

- Fill in:
  - Name (e.g., Marcus Rashford)
  - Age (e.g., 26)
  - Position (e.g., Forward)
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
    "name": "Luke Shaw",
    "age": 28,
    "position": "Defender"
  }
]
```

## Demo Video (YouTube)

Link (if applicable):  
[📺 Watch the demo](https://www.youtube.com/your-demo-video-link)

## Author

Nama: [Isi Nama Kamu]  
NIM: [Isi NIM Kamu]

Developed as part of Object-Oriented Programming (OOP) final project.

## License

This project is for educational and personal learning purposes only.
