# 🎮 Guess the Number & Tic-Tac-Toe Game

Welcome to the **GameWorld Project**! This project includes two fun Python games:

* **Guess The Number Game**
* **Tic-Tac-Toe (with Computer AI)**

This README explains how the games work, how to run them, and what features they include.

---

## 📌 Features

### ⭐ Guess The Number

* Random number between **1 and 10**.
* Colored feedback using `colorama`.
* Hints:

  * 🔥 Very close
  * 🙂 Close
  * ❄️ Far
* Input validation (numbers only).
* Replay system.

### ⭐ Tic-Tac-Toe

* Player is **X**, computer is **O**.
* Beautiful colored board.
* Smart random AI.
* Win, tie, and board checking.
* Clean and organized code.

---

## ▶️ How to Run the Game

1. Make sure you installed Python.

2. Install colorama:

```
pip install colorama
```

3. Run the game:

```
python GameWorld.py
```

---

## 📦 Creating .EXE File

If you want to turn the game into an EXE file, install PyInstaller:

```
pip install pyinstaller
```

Then run:

```
pyinstaller --onefile GameWorld.py
```

Your EXE will appear in the **dist** folder.

---

## 🎥 Video Demo

Here is the gameplay recording:
*([(https://hc-cdn.hel1.your-objectstorage.com/s/v3/b30fb7927ee0a4275cf8f4fc2a86ea5589f90496_screen_recording_2025-11-23_6.23.13_am.webm))*
]
---

## 📄 Project Structure

```
Project.11/
│── GameWorld.py
│── README.md
│── dist/ (created after EXE build)
│── build/ (created after EXE build)
```

---

## 👤 Author

Created by **Wafa Adam**.

If you need help improving the game or adding new features, feel free to ask! 🎮✨
