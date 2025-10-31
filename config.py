import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
    OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "1000"))
    
    # Flask Configuration
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    
    # Agent Configuration
    PERSONA_CONFIDENCE_THRESHOLD = 0.8  # Cache persona if confidence > 80%
    ESCALATION_MESSAGE_THRESHOLD = 5
    SENTIMENT_DEGRADATION_THRESHOLD = 2  # Escalate if sentiment drops 2 times
    
    # Validate required configuration
    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found! "
                "Please set it in .env file or environment variable"
            )
        
        if cls.OPENAI_API_KEY == "your-actual-api-key-here":
            raise ValueError(
                "Please replace 'your-actual-api-key-here' with your actual OpenAI API key"
            )
        
        return True