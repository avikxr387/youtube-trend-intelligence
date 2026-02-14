# YouTube Trend Intelligence

Real-Time Viral Detection and Early Trend Prediction System

---

## Overview

YouTube Trend Intelligence is a data-driven system designed to identify videos with high viral potential at an early stage.
The project collects YouTube video data, computes growth-based performance metrics, and detects viral content using early engagement signals such as view velocity, acceleration, and engagement rate.

The system provides an interactive dashboard for monitoring currently viral videos, identifying early trending content, and analyzing detailed performance metrics.

---

## Problem Statement

Most viral videos show strong growth patterns within the first few hours of publication.
This project aims to:

* Detect viral content early (within the first 24 hours)
* Monitor growth trends in near real-time
* Provide actionable insights using data-driven metrics

---

## Features

* Automated YouTube data collection using YouTube Data API
* Persistent storage using SQLite database
* Time-series feature engineering:

  * View velocity (views per hour)
  * Growth acceleration
  * Engagement rate
  * Video age tracking
* Viral detection based on top percentile growth threshold
* Interactive Streamlit dashboard:

  * Viral videos monitoring
  * Early trending videos (under 24 hours)
  * Detailed performance analytics
* Clean UI with modern dashboard layout

---

## System Architecture

Data Collection
→ Stored in SQLite (`youtube.db`)
→ Feature Engineering
→ Viral Detection Logic
→ Streamlit Dashboard

The system is designed for periodic execution and continuous data growth.

---

## Tech Stack

* Python
* Streamlit
* Pandas & NumPy
* SQLite
* Scikit-learn
* YouTube Data API
* python-dotenv

---

## Project Structure

```
youtube-trend-analysis/
│
├── app.py                    # Streamlit dashboard
├── youtube.db                # SQLite database
├── requirements.txt
├── .env                      # API key (not tracked)
├── .gitignore
├── README.md
│
└── notebooks/
    └── youtube-trend-analysis.ipynb   # Data pipeline & experiments
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/youtube-trend-analysis.git
cd youtube-trend-analysis
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Add YouTube API Key

Create a `.env` file in the project root:

```
YOUTUBE_API_KEY=your_api_key_here
```

The API key is required for data collection.

---

### 4. Run the Dashboard

```
streamlit run app.py
```

The dashboard will open in your browser.

---

## Dashboard Sections

### Viral Videos

Displays videos currently classified as viral based on high view velocity.

### Early Trending

Shows videos published within the last 24 hours that are gaining traction.

### Detailed Review

Provides performance metrics for videos including:

* View velocity
* Engagement rate
* Video age

---

## Viral Detection Method

Videos are classified as viral using a percentile-based threshold:

* Calculate view velocity for all videos
* Determine the top 10% threshold
* Videos exceeding this threshold are marked as viral

This approach allows adaptive detection based on current trend distribution.

---

## Future Improvements

* Machine learning model for viral probability prediction
* Real-time streaming pipeline
* Cloud deployment
* Historical trend visualization
* Video-level viral prediction using early features

---

## Security

* API keys are stored in `.env` and excluded via `.gitignore`
* No sensitive information is tracked in the repository

---

## Author

**AVIK HALDER**
GitHub: [https://github.com/avikxr387](https://github.com/avikxr387)

---

## License

MIT License

