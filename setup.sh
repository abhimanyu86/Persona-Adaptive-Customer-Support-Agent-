#!/bin/bash

echo ""
echo "=================================================="
echo "🤖 INTELLIGENT SUPPORT AGENT - PRODUCTION SETUP"
echo "=================================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 not found. Please install pip"
    exit 1
fi

echo "✅ pip found"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
echo "   - openai (LLM integration)"
echo "   - flask (web framework)"
echo "   - python-dotenv (env management)"
echo "   - scikit-learn (TF-IDF for KB retrieval)"
echo "   - numpy (numerical operations)"
echo ""

pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "=================================================="
echo "✅ SETUP COMPLETE!"
echo "=================================================="
echo ""
echo "📝 NEXT STEPS:"
echo ""
echo "1️⃣  CREATE YOUR .env FILE:"
echo "   cp .env.example .env"
echo ""
echo "2️⃣  ADD YOUR API KEY:"
echo "   Get key from: https://platform.openai.com/api-keys"
echo "   Edit .env and replace 'your-actual-api-key-here'"
echo ""
echo "3️⃣  RUN THE APPLICATION:"
echo "   python3 app.py"
echo ""
echo "4️⃣  OPEN IN BROWSER:"
echo "   http://localhost:5000"
echo ""
echo "=================================================="
echo "✨ FEATURES INCLUDED:"
echo "   ✅ Smart TF-IDF KB Retrieval"
echo "   ✅ Persona Caching (80%+ confidence)"
echo "   ✅ Combined LLM Calls (50% cost reduction)"
echo "   ✅ Live Metrics Dashboard"
echo "   ✅ Sentiment Degradation Tracking"
echo "   ✅ Production-Ready Error Handling"
echo "=================================================="
echo ""