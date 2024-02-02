# README for Frankie Assistant (Mac Version)

## Overview

Frankie Assistant is an innovative voice-activated personal assistant designed for macOS users. It leverages the OpenAI API to understand and generate human-like responses to user queries. By integrating advanced speech recognition and text-to-speech technologies, Frankie provides an interactive and engaging user experience, allowing for hands-free operation and assistance.

## Key Features

- **Voice Activation**: Simply say "Hey Frankie" to wake up the assistant and start interacting.
- **Speech Recognition**: Utilizes Google's speech recognition to accurately transcribe spoken words into text.
- **OpenAI Integration**: Leverages the powerful OpenAI API to generate meaningful and contextually relevant responses.
- **Text-to-Speech Output**: Employs macOS's built-in `say` command to verbally communicate responses to the user, making the interaction natural and accessible.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- macOS operating system.
- Python 3.6 or newer installed on your machine.
- An OpenAI API key.

## Installation Guide

### Step 1: Environment Setup

Clone this repository to your local machine to get started. It's recommended to use a virtual environment for Python projects to manage dependencies effectively:

```bash
python3 -m venv new_env
source new_env/bin/activate
```

### Step 2: Install Dependencies

Install the required Python libraries with pip:

```bash
pip install openai speechrecognition
```

### Step 3: Configure OpenAI API Key

Set your OpenAI API key as an environment variable for security. This can be done by adding the following line to your `.bash_profile`, `.zshrc`, or equivalent shell configuration file:

```bash
export OPENAI_API_KEY='your_api_key_here'
```

## How to Use Frankie Assistant

To use Frankie Assistant, follow these steps:

1. **Start the Application**

Activate your virtual environment and run the script from the terminal:

```bash
python Frankie_assist_mac.py
```

2. **Interact With Frankie**

Begin interaction by saying "Hey Frankie" to activate the assistant. Once activated, ask your question clearly. Frankie will process your query and respond verbally with the information or assistance you requested.

## Troubleshooting

- **Microphone Permissions**: If Frankie does not seem to hear you, check that your terminal or IDE has the necessary permissions to access your microphone.
- **API Key Issues**: Confirm that your OpenAI API key is correctly set up in your environment variables.
- **Dependency Problems**: Ensure all required packages are installed in your virtual environment. If you encounter errors, revisit the installation steps.

## Contributing to Frankie Assistant

Contributions to Frankie Assistant are welcome! Here's how you can contribute:

- **Report Bugs**: Submit bug reports using the issues section, providing as much detail as possible.
- **Feature Requests**: Have ideas for improvements? Share them through issues.
- **Pull Requests**: Submit pull requests with new features or bug fixes for review.

## License

This project is licensed under [LICENSE TYPE]. For more details, see the LICENSE file in the repository.

---

Frankie Assistant aims to make your daily tasks easier and more enjoyable through voice interaction. Your feedback and contributions are highly appreciated as we continue to improve and expand its capabilities.
