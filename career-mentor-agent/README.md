# 🤖 Career Mentor Agent

Career Mentor Agent is an intelligent career guidance app built using **Streamlit** and powered by **multi-agent support** with **Gemini API**. It helps users discover career fields, learn essential skills, and explore top job roles — all based on their personal interests.

---

## 🚀 Features

- 🔍 Detects your career field from interests using AI
- 🛠️ Generates skill roadmap using a Skill Agent
- 💼 Recommends top job roles via Job Agent
- 🤖 Uses multi-agent system architecture
- 🌐 Gemini API-powered backend
- 🎨 Clean, modern UI with a professional look

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Gemini API (Google)
- OpenAI Agent SDK (via agents: `career_agent`, `skill_agent`, `job_agent`)
- HTML/CSS (for custom UI styling)

---

## 📸 UI Preview

> 💡 Add screenshot image in your repo (e.g., `assets/screenshot.png`) and uncomment the line below:

<!-- ![App Screenshot](assets/screenshot.png) -->

---

## ⚙️ How to Use

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/career-mentor-agent.git
   cd career-mentor-agent
   ```

2. (Optional) Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Gemini API key:
   - Create a `.env` file in the root folder:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - OR directly update it in `gemini.py` (not recommended for production).

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 📁 Folder Structure

```
career-mentor-agent/
│
├── agents/
│   ├── __init__.py
│   ├── career_agent.py
│   ├── skill_agent.py
│   └── job_agent.py
│
├── app.py
├── utils/
│   └── gemini.py
├── .env              # (ignored from Git)
├── requirements.txt
└── README.md
```

---

## 🔐 .gitignore Tips

Make sure your `.gitignore` includes:

```
.env
venv/
__pycache__/
*.pyc
.vscode/
```

---

## 🙌 Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open source. You may use, modify, and distribute it under the MIT License.

---

## 👨‍💻 Developed by

**Made with ❤️ by [CodeWithAhtii](https://github.com/CodeWithAhtii)**