# WhatsApp Google Calendar Notifier

Automatically send your daily Google Calendar events to your WhatsApp number at a specific time using Python.

---

## Features

* Fetches events directly from your Google Calendar
* Sends a daily summary to your WhatsApp
* Runs automatically at your chosen time
* Simple setup using Google Cloud & Task Scheduler

---

## Setup Guide

### 1. Create a Google Cloud Project

* Go to Google Cloud Console
* Create a new project

### 2. Enable Google Calendar API

* Search for **Google Calendar API** and enable it

### 3. Configure OAuth Consent Screen

* Add yourself as a **Test User**

### 4. Create Credentials

* Go to **Credentials**
* Click **Create Credentials → OAuth Client ID**
* Download the JSON file
* Place it in your project folder

### 5. Install Dependencies

Run the following command:

```
pip install google-auth-oauthlib google-api-python-client requests
```

### 6. Configure Script

* Open the main Python file
* Replace the phone number with your WhatsApp number with your country code

### 7. First Run (Authentication)

* Run the script
* A browser window will open
* Log in and grant permissions
* A `token.json` file will be generated automatically

### 8. Automate with Task Scheduler (Windows)

* Open **Task Scheduler**
* Create a new task
* Set trigger → Daily at your preferred time
* Set action → Run your Python script

---

##  Note

* Keep `credentials.json` and `token.json` private
* Make sure your system is on at the scheduled time
* Internet connection is required

---
