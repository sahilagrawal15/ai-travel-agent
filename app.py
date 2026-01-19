import os
# DISABLE TELEMETRY IMMEDIATELY
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

import streamlit as st
from src.crew import VoyageOpsCrew

st.set_page_config(page_title="VoyageOps Pro", layout="wide", page_icon="🧭")

# --- INITIALIZE SESSION STATE ---
if 'step' not in st.session_state: st.session_state.step = 'discovery'
if 'prefs' not in st.session_state: st.session_state.prefs = {}
if 'suggestions' not in st.session_state: st.session_state.suggestions = None
if 'final_plan' not in st.session_state: st.session_state.final_plan = None

st.title("🧭 VoyageOps: Digital Travel Agency")

# --- STEP 1: DISCOVERY ---
if st.session_state.step == 'discovery':
    st.header("Step 1: Your Travel Profile")
    
    col1, col2 = st.columns(2)
    with col1:
        vibe = st.selectbox("What's your travel vibe?", [
            "Adventure & Outdoor", 
            "Relaxation & Beach", 
            "Cultural & Historical", 
            "Food & Culinary", 
            "Nature & Wildlife",
            "Urban Exploration",
            "Nightlife & Entertainment",
            "Off-the-beaten-path",
            "Luxury & Premium",
            "Budget-Friendly",
            "Family-Friendly",
            "Romantic & Couples",
            "Solo Travel",
            "Wellness & Spa"
        ])
        
        budget = st.selectbox("What's your budget level?", [
            "Economy ($500-1000)",
            "Standard ($1000-2500)", 
            "Mid-Range ($2500-5000)",
            "Luxury ($5000-10000)",
            "Premium ($10000+)"
        ])
        
        travelers = st.selectbox("How many travelers?", [1, 2, 3, 4, 5, 6, 7, 8])
        
        duration = st.selectbox("Trip duration?", [
            "Weekend (3 days)",
            "Short (5 days)", 
            "Standard (7 days)",
            "Extended (10 days)",
            "Two Weeks (14 days)"
        ])
        
    with col2:
        dates = st.text_input("Tentative dates", placeholder="e.g., Early March 2026")
        departure = st.text_input("Leaving from", value="Dallas (DFW)")
        
        # Additional filters
        st.subheader("Travel Preferences")
        accommodation = st.selectbox("Accommodation preference?", [
            "Hotel", "Airbnb", "Resort", "Hostel", "Any"
        ])
        
        transport = st.selectbox("Transportation preference?", [
            "Rental Car", "Public Transport", "Walking", "Mixed", "Any"
        ])
        
        pace = st.selectbox("Travel pace?", [
            "Relaxed", "Moderate", "Packed", "Flexible"
        ])

    user_query = st.text_area("Anything specific you're looking for?", 
                           placeholder="e.g. Somewhere snowy with good coffee, or Beach with great snorkeling, or Mountains with hiking trails")

    if st.button("Find My Destinations"):
        # Package data for agents
        st.session_state.prefs = {
            "vibe": vibe,
            "budget": budget,
            "dates": dates,
            "departure": departure,
            "travelers": travelers,
            "duration": duration,
            "accommodation": accommodation,
            "transport": transport,
            "pace": pace,
            "query": user_query
        }
        
        with st.spinner("Our Strategist is scouting locations..."):
            crew = VoyageOpsCrew()
            result = crew.run_discovery(st.session_state.prefs)
            st.session_state.suggestions = str(result)
            st.session_state.step = 'planning'
            st.rerun()

# --- STEP 2: PLANNING ---
elif st.session_state.step == 'planning':
    st.header("Step 2: Review Options & Plan Logistics")
    st.markdown(st.session_state.suggestions)
    
    st.divider()
    st.subheader("Select Your Preferred Destination")
    
    # Extract destination options from suggestions more robustly
    destination_options = []
    suggestions_text = st.session_state.suggestions
    
    # Try multiple extraction patterns
    import re
    
    # Pattern 1: Look for numbered destinations
    numbered_pattern = r'(?:\*\*)?\s*(\d+)\.\s*\*\*?\s*([A-Za-z\s,\s]+[A-Za-z]+)'
    numbered_matches = re.findall(numbered_pattern, suggestions_text)
    
    # Pattern 2: Look for "Destination X:" format
    dest_pattern = r'(?:Destination\s+(\d+):\s*([A-Za-z\s,\s]+[A-Za-z]+))'
    dest_matches = re.findall(dest_pattern, suggestions_text)
    
    # Pattern 3: Look for bold destination names
    bold_pattern = r'\*\*([A-Za-z\s,\s]+[A-Za-z]+)\*\*'
    bold_matches = re.findall(bold_pattern, suggestions_text)
    
    # Combine all matches and deduplicate
    all_matches = []
    for match in numbered_matches:
        all_matches.append(f"Destination {match[0]}: {match[1].strip()}")
    for match in dest_matches:
        all_matches.append(f"Destination {match[0]}: {match[1].strip()}")
    for match in bold_matches:
        all_matches.append(match.strip())
    
    # If still no matches, create generic options based on content
    if not all_matches:
        # Look for any capitalized location names
        location_pattern = r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*)'
        locations = re.findall(location_pattern, suggestions_text)
        if locations:
            for i, loc in enumerate(locations[:3], 1):
                all_matches.append(f"Destination {i}: {loc}")
        else:
            all_matches = ["Destination 1", "Destination 2", "Destination 3"]
    
    # Remove duplicates and clean up
    destination_options = list(dict.fromkeys(all_matches))[:3]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        choice = st.selectbox("Which destination should we build your master plan for?", 
                           options=[""] + destination_options,
                           help="Select from the destinations suggested above",
                           key="destination_select")
        
        # Show prefilled selection if available
        if choice:
            st.success(f"✅ Selected: {choice}")
            st.info("The Logistics Architect will now find flights, hotels, and transportation for this destination.")
    
    with col2:
        st.write("")  # Spacer for layout
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 Build Detailed 7-Day Plan", type="primary", disabled=not choice):
            with st.spinner(f"The Execution Crew is mapping out {choice}..."):
                crew = VoyageOpsCrew()
                # Pass both choice and stored prefs
                result = crew.run_planning(choice, st.session_state.prefs)
                st.session_state.final_plan = str(result)
                st.session_state.step = 'final'
                st.rerun()
    
    with col2:
        if st.button("🔄 Modify Search", type="secondary"):
            st.session_state.step = 'discovery'
            st.session_state.suggestions = None
            st.session_state.final_plan = None
            st.rerun()
    
    with col3:
        if st.button("🔄 Reset Everything", type="secondary"):
            # Reset all session state
            st.session_state.step = 'discovery'
            st.session_state.prefs = {}
            st.session_state.suggestions = None
            st.session_state.final_plan = None
            st.rerun()
    
    if st.button("← Back to Discovery"):
        st.session_state.step = 'discovery'
        st.rerun()

# --- STEP 3: FINAL ---
elif st.session_state.step == 'final':
    st.header("Your 7-Day Master Itinerary")
    st.markdown(st.session_state.final_plan)
    
    if st.button("Start a New Search"):
        st.session_state.step = 'discovery'
        st.session_state.suggestions = None
        st.session_state.final_plan = None
        st.rerun()