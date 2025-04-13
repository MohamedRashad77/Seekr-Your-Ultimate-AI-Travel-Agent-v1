# Seekr - Your Ultimate AI Travel Agent 🌍✈️

## Overview

Seekr is an AI-powered travel planning assistant that helps users create personalized travel itineraries. Using the power of Groq's LLM and real-time data from SerpAPI, Seekr generates comprehensive travel plans including accommodations, flights, daily activities, and budget breakdowns.

## Features

- 🌟 Personalized travel itineraries
- 💰 Multiple budget options (Budget, Moderate, Luxury)
- ✈️ Real-time flight recommendations
- 🏨 Accommodation suggestions
- 🗺️ Day-by-day activity planning
- 📊 Budget breakdown and cost estimates
- 📑 PDF export functionality

## Prerequisites

- Python 3.8 or higher (Download Python)-[https://www.python.org/downloads/]
- Groq API key (Get Groq API key)-[https://groq.com/]
- SerpAPI key  (Get SerpAPI key)-[https://serpapi.com/]

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MohamedRashad77/Seekr-Your-Ultimate-AI-Travel-Agent-v1.git
cd Seekr-Your-Ultimate-AI-Travel-Agent-v1
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your API keys:
```
GROQ_API_KEY=your_groq_api_key
SERP_API_KEY=your_serpapi_key
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run Seekr-streamlit-app.py
```

2. Enter your API keys in the sidebar
3. Fill in your travel details:
   - Departure city
   - Destination
   - Travel dates
   - Duration
   - Budget preference

4. Click "Generate My Travel Plan" to create your itinerary
5. Download the generated PDF for offline access

## Project Structure

```
seekr-travel-agent/
├── Seekr-streamlit-app.py    # Main Streamlit application
├── utils.py                  # Utility functions
├── requirements.txt          # Project dependencies
├── README.md                # Project documentation
└── .env                     # API keys (create this file)
```

## Key Components

- **Streamlit Interface**: User-friendly web interface for input and display
- **Groq Integration**: Advanced language model for generating travel recommendations
- **SerpAPI Integration**: Real-time data for flights and travel information
- **PDF Generation**: Creates downloadable travel itineraries
- **Budget Management**: Tailored recommendations based on budget level

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Acknowledgments

- Groq for their powerful language model
- SerpAPI for real-time travel data
- Streamlit for the web interface framework
- All contributors and users of the application
