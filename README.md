# Weather Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

A simple reflex agent that fetches real-time weather data from the OpenWeatherMap API, analyses it across four dimensions, and saves a structured report to a text file.

---

## What is this project?

This project is a practical implementation of a **simple reflex agent** — one of the foundational agent architectures in Artificial Intelligence.

A simple reflex agent does not maintain memory or learn from past states. It perceives its environment through sensors (in this case, live weather data from an API) and responds with pre-defined actions based purely on **condition → action** rules. The agent asks: *"What do the current conditions say, and what should I do about them?"*

```
Percept (API data) → Rules (Python functions) → Action (written report)
```

This makes the architecture transparent, predictable, and easy to reason about — a solid starting point for understanding how intelligent agents work.

---

## Features

The agent applies four independent analyses to the retrieved weather data:

| Analysis | What it evaluates | Example output |
|---|---|---|
| **Clothing** | Temperature in °C | *"Wear light clothing, the temperature is high."* |
| **Wind** | Wind speed in m/s | *"Moderate wind — hold light objects outdoors."* |
| **Cloud cover** | Sky cloudiness in % | *"Partly cloudy sky."* |
| **Rain** | Weather description string | *"No precipitation expected."* |

Each rule maps a measurable threshold to a plain-language recommendation, keeping the logic explicit and easy to extend.

---

## Project structure

```
weather-agent/
├── weather-agent.py          # Agent source code
├── .env                      # Your API key (not committed)
├── .env.example              # Template for the .env file
├── .gitignore
├── LICENSE
└── weather_report_YYYY-MM-DD.txt   # Generated on each run (not committed)
```

---

## Prerequisites

- Python 3.10 or higher
- A free [OpenWeatherMap](https://openweathermap.org/api) API key
- The following Python packages:
  - `requests`
  - `python-dotenv`

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/weather-agent.git
cd weather-agent
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows
```

**3. Install dependencies**

```bash
pip install requests python-dotenv
```

**4. Set up your API key**

Copy the provided template and add your key:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder:

```
API_KEY=your_openweathermap_api_key_here
```

---

## Usage

Run the agent with:

```bash
python weather-agent.py
```

A report file named `weather_report_YYYY-MM-DD.txt` will be created in the project directory. The coordinates in `main()` currently point to **Luanda, Angola** — change `lat` and `lon` to target any location.

---

## Example output

```
Weather Report - 2026-05-04 12:38:44
•Temperature: 28.0°C
•Feels like: 29.6°C
•Humidity: 61%
•Wind speed: 5.7 m/s
•Cloudiness: 40%
•Description: scattered clouds

Analysis:
•Clothing: Hot conditions — opt for light, breathable clothing.
•Wind: Light to moderate breeze — keep an eye on loose objects.
•Cloud cover: Partly cloudy — a mix of sun and clouds expected.
•Rain: Dry conditions expected — no umbrella needed.
```

---

## Possible future improvements

- **Accept coordinates as CLI arguments** — remove the hardcoded location and let the user pass `--lat` / `--lon` flags.
- **Add city name lookup** — resolve a city name to coordinates using the OpenWeatherMap Geocoding API so users don't need to know lat/lon.
- **Schedule automatic runs** — use `cron` (Linux/macOS) or Task Scheduler (Windows) to generate a daily report automatically.
- **Forecast support** — extend the agent to use the `/forecast` endpoint and produce a multi-day outlook.
- **Output formats** — support JSON or HTML in addition to plain text, making the report easier to consume by other systems.
- **Stateful agent upgrade** — add a history file so the agent can compare today's conditions against yesterday's and highlight changes (moving toward a model-based reflex agent).
- **Notifications** — send the report by email or messaging app when certain thresholds are met (e.g., heavy rain or extreme heat).

---

## License

This project is licensed under the [MIT License](LICENSE).
