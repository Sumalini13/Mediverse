# Medical Image Analysis Application

## Overview
This repository contains the source code for a cutting-edge medical image analysis application developed using Python, Streamlit, and Google's Generative AI (Gen AI) model. The application allows users to upload medical images and receive instant analysis, including detailed reports, recommendations, and treatment suggestions.

## Features
- Upload medical images for analysis
- Instant analysis using Gen AI's Gemini Pro Vision model
- Detailed reports and treatment recommendations
- User-friendly interface built with Streamlit
- Multilingual support with audio output
- Disclaimer stressing the importance of consulting healthcare professionals

## Getting Started
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Obtain API keys for Google's Gen AI model and configure safety settings.
4. Customize prompts and messages for tailored responses.
5. Run the application using `streamlit run app.py`.

## Usage
1. Launch the application by running `streamlit run app.py`.
2. Upload a medical image for analysis.
3. View the detailed analysis, recommendations, and treatment suggestions.
4. Follow the disclaimer to consult healthcare professionals for medical advice.

## Configuration
- `config.py`: Configure API keys, safety settings, and prompts.
- `app.py`: Main application file with Streamlit interface.
- `requirements.txt`: List of dependencies required for the application.

## Deployment
This application can be deployed using various platforms, including:
- Heroku
- AWS
- Google Cloud Platform

Choose a deployment platform based on your requirements and follow the platform-specific deployment instructions.

## Testing
Unit tests are available in the `tests/` directory. Run tests using `pytest`:
```bash
pytest
