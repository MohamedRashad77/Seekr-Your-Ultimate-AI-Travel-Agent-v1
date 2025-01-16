import streamlit as st
import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.serpapi_tools import SerpApiTools
from fpdf import FPDF
from utils import create_travel_prompt, generate_pdf

# Initialize page config
st.set_page_config(
    page_title="Seekr: Your Ultimate AI Travel Agent",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar configuration
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/airplane-take-off.png")
    st.title("Trip Settings")

    # User inputs for API keys
    groq_api_key = st.text_input("🔑 Enter your Groq API Key", type="password")
    serpapi_key = st.text_input("🔑 Enter your SerpAPI Key", type="password")

    # Departure city and destination inputs
    departure_city = st.text_input("🏙️ Enter your city of departure")
    destination = st.text_input("🌍 Destination")

    # Departure date input
    departure_date = st.date_input("📅 Departure Date")

    # Duration input
    duration = st.number_input("🕒 Duration (days)", min_value=1, max_value=30, value=5)

    # Budget selection dropdown with tooltips
    budget_options = {
        "Budget": "Economical options, hostels, public transport",
        "Moderate": "Mid-range hotels, occasional splurges",
        "Luxury": "High-end accommodations and experiences"
    }
    budget = st.selectbox(
        "💸 Choose Your Budget",
        options=list(budget_options.keys()),
        help="Hover over options to see details"
    )

# Initialize session state variables
if 'travel_plan' not in st.session_state:
    st.session_state.travel_plan = None

if not groq_api_key or not serpapi_key:
    st.warning("⚠️ Please provide both Groq and SerpAPI keys.")
else:
    os.environ["GROQ_API_KEY"] = groq_api_key
    os.environ["SERP_API_KEY"] = serpapi_key

    try:
        travel_agent = Agent(
            name="Seekr Agent",
            model=Groq(id="llama-3.3-70b-versatile"),
            tools=[SerpApiTools()],
            instructions=[
                "You are a travel planning assistant using Groq Llama.",
                "Help users plan their trips, including providing live flight prices.",
                "Always verify information is current before making recommendations.",
                "Provide detailed, budget-conscious recommendations based on user preferences."
            ],
            show_tool_calls=True,
            markdown=True
        )

        st.title("✈️ Seekr: Your Ultimate AI Travel Agent")

        # Clear output button functionality
        clear_button = st.button("🔄 Clear Output")
        if clear_button:
            st.session_state.travel_plan = None
            st.experimental_rerun()

        # Show a basic itinerary description before generating the plan
        if not st.session_state.travel_plan:
            st.write("Your itinerary will appear here once generated. Please enter the necessary details and hit 'Generate My Travel Plan'.")

        if st.button("✨ Generate My Travel Plan"):
            if departure_city and destination:
                try:
                    with st.spinner("🔍 Creating your travel plan..."):
                        # Generate prompts based on budget type
                        prompt = create_travel_prompt(destination, departure_city, duration, budget)
                        
                        # Run the travel agent to generate the plan
                        response = travel_agent.run(prompt)
                        if hasattr(response, 'content'):
                            st.session_state.travel_plan = response.content
                            st.markdown(response.content)

                            # Generate PDF with improved formatting
                            pdf_output = generate_pdf(
                                response.content, 
                                departure_city, 
                                destination,
                                budget,
                                duration
                            )
                            st.download_button(
                                "📥 Download PDF", 
                                data=pdf_output, 
                                file_name=f"travel_itinerary_{destination.lower().replace(' ', '_')}.pdf"
                            )
                        else:
                            st.session_state.travel_plan = str(response)
                            st.markdown(str(response))
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter both departure city and destination.")
    except Exception as e:
        st.error(f"Application Error: {str(e)}")
