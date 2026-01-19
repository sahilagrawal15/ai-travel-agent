#  VoyageOps-Pro - AI Travel Agency

A sophisticated CrewAI-powered travel planning application that provides personalized destination discovery and comprehensive travel itineraries using multiple specialized AI agents.

##  Features

- ** Smart Discovery**: AI-powered destination suggestions based on travel preferences
- ** Multi-Agent Planning**: Collaborative crew of specialized travel agents
- ** Detailed Itineraries**: Day-by-hour activity planning with weather considerations
- ** Safety Monitoring**: Real-time safety alerts and local insights
- ** Logistics Coordination**: Flights, hotels, and transportation planning
- ** Experience Optimization**: Golden hour scheduling and photography tips
- ** State-Machine UI**: Non-resetting interface with seamless flow

##  AI Agents

### Discovery Strategist
- Analyzes travel preferences and suggests 3 perfect destination concepts
- Considers vibe, budget, dates, and traveler requirements

### Logistics Architect  
- Finds optimal flights, hotels, and rental cars
- Handles EV charging infrastructure and parking logistics
- Provides booking-ready recommendations

### Daily Rhythm Guide
- Creates hour-by-hour activity schedules
- Monitors weather forecasts and crowd patterns
- Optimizes trip duration for maximum value

### Safety & Experience Scout
- Provides safety briefings and local insights
- Optimizes for photography (sunrise/sunset timing)
- Identifies authentic local dining experiences
  
##  Quick Start

### Prerequisites
- Python 3.11+
- Groq API key
- (Optional) Serper API key for enhanced search

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-travel-agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
GROQ_API_KEY=your_groq_api_key_here

# Optional (for enhanced search)
SERPER_API_KEY=your_serper_api_key_here
```

### Getting API Keys

- **Groq API Key**: Get from [console.groq.com](https://console.groq.com)
- **Serper API Key**: Get from [serper.dev](https://serper.dev) (optional)

## 📱 Usage

1. **Enter Travel Preferences**
   - Select your travel vibe (Adventure, Relaxation, Culture, etc.)
   - Set budget level and dates
   - Specify departure location
   - Add any special requirements

2. **Discover Destinations**
   - AI analyzes your preferences
   - Suggests 3 tailored destination concepts
   - Each includes detailed descriptions and timing recommendations

3. **Choose & Plan**
   - Select your preferred destination
   - Multi-agent crew creates comprehensive 7-day itinerary
   - Includes logistics, activities, safety briefings, and local tips

4. **Get Your Master Plan**
   - Complete day-by-hour schedule
   - Booking recommendations with links
   - Safety alerts and weather considerations
   - Photography opportunities and local insights

## 🏗️ Architecture

### State-Machine Pattern
The application uses a robust state-machine pattern to prevent page resets:

- **Discovery State**: Input collection and destination suggestions
- **Planning State**: Destination selection and crew execution  
- **Final State**: Complete itinerary display

### CrewAI Integration
- Sequential process with agent collaboration
- Memory and caching disabled for reliability
- Groq LLM integration for fast responses
- Error handling and graceful degradation

##  Development

### Project Structure
```
ai-travel-agent/
├── app.py                 # Main Streamlit application
├── src/
│   ├── agents.py          # AI agent definitions
│   ├── crew.py            # Crew orchestration
│   ├── tasks.py           # Task definitions
│   └── tools.py           # Tool integrations
├── requirements.txt        # Python dependencies
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
└── README.md            # This file
```

### Key Dependencies
- **streamlit**: Web UI framework
- **crewai**: AI agent orchestration
- **groq**: LLM provider
- **httpx**: HTTP client for API calls

##  Troubleshooting

### Common Issues

**"Invalid API Key" Error**
- Verify GROQ_API_KEY in .env file
- Check for extra spaces or special characters
- Ensure API key is active and has credits

**"No Search Results"**
- Optional: Add SERPER_API_KEY for enhanced search
- Check internet connection
- Try more general destination names

**Page Reset Issues**
- Ensure browser cookies are enabled
- Check for conflicting browser extensions
- Try refreshing the page completely

**Slow Performance**
- Install watchdog: `pip install watchdog`
- Check internet connection speed
- Reduce concurrent agent tasks

### Debug Mode
Enable verbose logging by setting:
```python
# In agents.py, change verbose=True for individual agents
# In crew.py, change verbose=True for crew execution
```

##  Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Update README for new features
- Test with different travel scenarios

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Acknowledgments

- **CrewAI** - Multi-agent orchestration framework
- **Groq** - Fast LLM inference
- **Streamlit** - Beautiful web UI framework
- **Serper** - Real-time search capabilities

##  Support

For issues, questions, or feature requests:
- Create an issue in the repository
- Check existing issues for solutions
- Include error logs and reproduction steps

---

** Happy travels with VoyageOps-Pro!**
