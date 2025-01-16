from fpdf import FPDF

def create_travel_prompt(destination, departure_city, duration, budget):
    """Create the appropriate travel prompt based on budget type."""
    prompt = f""" 
Overview
Provide a brief overview of {destination}, highlighting its unique features, cultural significance, and what makes it a desirable location for {budget} travel. Include key attractions, local customs, and any notable historical or natural landmarks.

Create a detailed travel itinerary for a {budget}-friendly experience in {destination}. Focus on affordable accommodations, free activities, and budget transportation options.

Accommodation Recommendations
Suggest affordable stays such as hostels, budget hotels, or guesthouses. Provide booking resources or websites for reservations.

Flight Recommendations
List at least three flight options from {departure_city} to {destination}, including:
- Airline
- Departure city: {departure_city}
- Price range (round trip): Budget-friendly
- Booking resources or websites for reservations

Day-by-Day Itinerary
Generate a day-wise itinerary for {duration} days, focusing on low-cost and free activities such as visiting public parks, museums with free entry, or street tours. Format each day clearly and number them.
Example format for Day-by-Day Itinerary:
- Day 1: Arrival and Exploration
    - Visit the main city park (Free)
    - Explore the local markets (Free)
    - Visit a free-entry museum (e.g., City Museum)
- Day 2: Cultural Exploration
    - Take a self-guided walking tour (Free)
    - Visit local galleries (Free entry)
    - Evening at a free outdoor event (e.g., street performance)
(Repeat for each day)

Culinary Experiences
Recommend budget-friendly street food and local eateries offering inexpensive dishes. Mention any must-try dishes and provide reservation information if applicable.

Practical Travel Tips
Local Transportation Options: Recommend using public transport, walking, or budget ridesharing services.
Safety Recommendations: Provide basic safety tips for budget travelers.

Estimated Daily Budget Breakdown
Offer a breakdown of daily expenses for affordable accommodation, cheap food options, transportation, and free or low-cost attractions.

Estimated Total Trip Cost
Calculate the total estimated cost for the trip based on budget-friendly options
"""
    return prompt

def generate_pdf(content, departure_city, destination, budget, duration):
    """Generate a PDF document from the travel itinerary with improved formatting."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add cover page
    pdf.add_page()
    pdf.set_font("Arial", "B", size=28)
    pdf.cell(200, 10, txt="Seekr: Your Ultimate AI Travel Agent", ln=True, align='C')
    pdf.set_font("Arial", "B", size=24)
    pdf.cell(200, 20, txt="Travel Itinerary", ln=True, align='C')
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt=f"From {departure_city} to {destination}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Duration: {duration} days", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Budget Level: {budget}", ln=True, align='C')
    
    # Add content pages
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Process content by sections
    sections = content.split('\n\n')
    for section in sections:
        if section.strip():
            # Handle section titles
            if any(section.startswith(header) for header in ['Overview', 'Accommodation', 'Flight', 'Day', 'Culinary', 'Practical', 'Estimated']):
                pdf.set_font("Arial", "B", size=14)
                pdf.cell(0, 10, txt=section.split('\n')[0], ln=True)
                pdf.set_font("Arial", size=12)
            
            # Handle content
            pdf.multi_cell(0, 10, section.encode('latin1', 'ignore').decode('latin1'))
            pdf.ln(5)

    return pdf.output(dest='S').encode('latin1')
