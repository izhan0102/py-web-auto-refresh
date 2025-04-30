# JKBOSE Results Monitor

A simple automation tool I built when waiting for my Class 12 results. Manually refreshing the JKBOSE website every few seconds was driving me crazy, so I created this Python script to do it for me.

## What it does

The script opens Chrome, navigates to the JKBOSE results page, and refreshes it automatically every 5 seconds. This way, you can focus on other things while waiting for your results to appear.

## Why I made this

Result day is stressful enough without having to constantly hit F5 on your browser. This tool helped me:
- Reduce anxiety by automating the refresh process
- Get notified immediately when the page changes
- Focus on other tasks while waiting

## Requirements

- Python 3.6 or higher
- Chrome browser

## How to use it

1. Install Python packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the script:
   ```
   python jkbose_monitor.py
   ```

3. Let it run until your results appear
   (Press Ctrl+C when you want to stop)

## Troubleshooting

If you have issues with Chrome:
1. Make sure Chrome is installed and updated
2. If you get driver errors, download chromedriver from https://chromedriver.chromium.org/downloads
3. Make sure the chromedriver version matches your Chrome version

## Technical details

This script uses Selenium WebDriver to control Chrome and the Chrome DevTools Protocol for browser automation. 
