# Beagle - Dog Breed Guessing Game

An interactive Streamlit game where you guess dog breeds from progressively less blurred images.

## About

Beagle is a fun, educational game that challenges players to identify dog breeds. Start with a heavily blurred image and use your attempts wisely - each guess reduces the blur, making identification easier but costing you points!

## Features

- **Progressive Blur Reduction**: Each attempt reveals more detail
- **6 Attempts per Breed**: Limited chances to guess correctly
- **Multiple Dog Breeds**: Test your knowledge across various popular breeds
- **Score Tracking**: Track your wins, losses, and attempts
- **Results Dashboard**: View your performance across all rounds

## How to Play

1. Look at the blurred dog image
2. Choose a breed from the dropdown menu
3. Click "Confirm" to submit your guess
4. If wrong, click "Reduce blur" to see more detail (costs 1 attempt)
5. Win by guessing correctly within 6 attempts!

## Installation

```bash
# Clone the repository
git clone https://github.com/mirasollar/beagle.git
cd beagle

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Requirements

- Python 3.8+
- Streamlit
- Pillow (PIL)
- Pandas
- streamlit-js-eval

## Game Mechanics

- **Starting Blur**: 50 (maximum)
- **Blur Reduction**: -6 per attempt
- **Maximum Attempts**: 6
- **Win Condition**: Correct guess within attempts
- **Loss Condition**: 6 incorrect guesses

## Project Structure

```
beagle/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/           # Streamlit configuration
│   ├── config.toml       # Theme and UI settings
│   └── secrets.toml      # Secrets (not in repo)
├── static/               # Static assets
│   ├── init_log.csv      # Initial game log
│   └── keboola.png       # Logo
└── README.md             # This file
```

## Configuration

The app uses Streamlit's configuration system. Customize the theme in `.streamlit/config.toml`:

```toml
[theme]
primaryColor="#1f8fff"
backgroundColor="#ffffff"
secondaryBackgroundColor="#edf0f5"
textColor="#222529"
font="sans serif"
```

## Contributing

Contributions are welcome! Feel free to:
- Add new dog breeds
- Improve the UI/UX
- Add difficulty levels
- Implement multiplayer features

## License

This project is open source and available under the MIT License.

## Author

Created by [@mirasollar](https://github.com/mirasollar)

---

**Have fun guessing! 🐕**
