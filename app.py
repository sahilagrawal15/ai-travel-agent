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
        vibe = st.selectbox("What's the vibe?", ["Adventure", "Relaxation", "Culture", "Foodie", "Nature"])
        budget = st.selectbox("Budget Level", ["Economy", "Standard", "Luxury"])
    with col2:
        dates = st.text_input("Tentative Dates", placeholder="e.g., Early March 2026")
        departure = st.text_input("Leaving From", value="Dallas (DFW)")

    user_query = st.text_area("Anything specific you're looking for?", placeholder="e.g. Somewhere snowy with good coffee")

    if st.button("Find My Destinations"):
        # Package data for the agents
        st.session_state.prefs = {
            "vibe": vibe,
            "budget": budget,
            "dates": dates,
            "departure": departure,
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
    choice = st.text_input("Which destination should we build the master plan for?", placeholder="Enter the destination name here")
    
    if st.button("Build Detailed 7-Day Plan"):
        if not choice:
            st.error("Please enter a destination name first!")
        else:
            with st.spinner(f"The Execution Crew is mapping out {choice}..."):
                crew = VoyageOpsCrew()
                # Pass both the choice and the stored prefs
                result = crew.run_planning(choice, st.session_state.prefs)
                st.session_state.final_plan = str(result)
                st.session_state.step = 'final'
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