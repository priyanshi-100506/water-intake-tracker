# 🚀 INSTALLATION & SETUP GUIDE

## Step 1: Download and Install Ollama

### Windows Installation

1. **Download Ollama**
   - Visit: https://ollama.ai
   - Click "Download" button
   - Select Windows version

2. **Install Ollama**
   - Run the downloaded installer
   - Follow the installation wizard
   - Accept default settings
   - Installation completes (~100MB)

3. **Verify Installation**
   - Open PowerShell or Command Prompt
   - Run: `ollama --version`
   - You should see the version number

4. **Pull the Llama 3.2 Model**
   ```bash
   ollama pull llama3.2
   ```
   - First time will download the model (~5GB)
   - Takes 5-15 minutes depending on internet
   - You'll see download progress

5. **Start Ollama Server**
   ```bash
   ollama serve
   ```
   - Keep this terminal open
   - You should see: `Listening on 127.0.0.1:11434`

---

## Step 2: Install Python Dependencies

In your project directory with the virtual environment activated:

```bash
# Upgrade pip first
python -m pip install --upgrade pip setuptools wheel

# Install all dependencies
pip install -r requirements.txt --prefer-binary
```

If you get errors, install individually:
```bash
pip install fastapi uvicorn pydantic python-dotenv
pip install langchain langchain-ollama langchain-core
pip install streamlit plotly pytz pandas
```

---

## Step 3: Start the Application

Open **3 separate terminals** and run these commands:

### Terminal 1: Start Ollama
```bash
ollama serve
```
✅ Should show: `Listening on 127.0.0.1:11434`

### Terminal 2: Start FastAPI Server
Navigate to project directory first:
```bash
cd "C:\Users\USER\Documents\water intake tracker"
```

Then start the API:
```bash
python -m uvicorn src.api:app --host 127.0.0.1 --port 8000 --reload
```
✅ Should show: `Uvicorn running on http://127.0.0.1:8000`

### Terminal 3: Start Streamlit Dashboard
In the project directory:
```bash
streamlit run dashboard_new.py
```
✅ Should show: `Local URL: http://localhost:8501`

---

## Step 4: Access the Application

1. **Open your browser**
2. **Go to:** http://localhost:8501
3. **Create a user profile:**
   - Click "New User" button in sidebar
   - Fill in your details
   - Click "Create Profile"
4. **Start tracking:**
   - Enter water intake amount
   - Click "Log & Analyze"
   - View AI-powered recommendations!

---

## ✅ Verification Checklist

- [ ] Ollama downloaded and installed
- [ ] Llama 3.2 model pulled: `ollama pull llama3.2`
- [ ] Virtual environment activated: `.venv`
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Ollama server running (Terminal 1)
- [ ] API server running (Terminal 2)
- [ ] Streamlit dashboard running (Terminal 3)
- [ ] Dashboard loads: http://localhost:8501
- [ ] API docs accessible: http://127.0.0.1:8000/docs

---

## 🔧 Troubleshooting

### "ollama is not recognized"
- Ollama not installed or not in PATH
- Solution: Download from https://ollama.ai and install

### "Connection refused at 127.0.0.1:11434"
- Ollama server not running
- Solution: Run `ollama serve` in Terminal 1

### "ImportError: cannot import name..."
- Old version of langchain installed
- Solution: Upgrade: `pip install --upgrade langchain langchain-core langchain-ollama`

### "Port 8000 already in use"
- Another service using port 8000
- Solution: Kill the process or use a different port:
  ```bash
  python -m uvicorn src.api:app --host 127.0.0.1 --port 8001 --reload
  ```

### "Port 8501 already in use"
- Another Streamlit app running
- Solution: Specify a different port:
  ```bash
  streamlit run dashboard_new.py --server.port 8502
  ```

### Dashboard won't load/API errors
- Make sure all 3 services are running
- Check that Ollama server is listening
- Verify model is pulled: `ollama list`

---

## 📊 System Requirements

- **RAM:** 4GB minimum (8GB recommended)
- **Storage:** 10GB (for Ollama + model)
- **Internet:** For first-time model download
- **Python:** 3.9 or higher

---

## 🎯 What Each Service Does

| Service | Port | Purpose | Terminal |
|---------|------|---------|----------|
| **Ollama** | 11434 | AI/LLM backend (Llama 3.2) | 1 |
| **FastAPI** | 8000 | REST API server | 2 |
| **Streamlit** | 8501 | Web dashboard UI | 3 |

---

## 📚 Next Steps

1. Follow all steps above
2. Start all 3 services
3. Open http://localhost:8501
4. Create a profile
5. Start logging water intake
6. View AI recommendations
7. Generate weekly reports

---

## 🆘 Still Stuck?

Check these files for more help:
- **SETUP_GUIDE.md** - Detailed setup
- **QUICK_START.txt** - Quick reference
- **API_REFERENCE.md** - API endpoints
- **README.md** - Project overview

---

**Ready to go! 💧**

Once all 3 services are running, your AI Hydration Platform is ready to use!
