# AI Tutor

<div align="center">

![AI Tutor Logo](https://img.shields.io/badge/AI-Tutor-blueviolet?style=for-the-badge&logo=robot&logoColor=white)

An intelligent learning companion powered by advanced AI to help students with chemistry, mathematics, and physics.

[![Next.js](https://img.shields.io/badge/frontend-Next.js-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/frontend-React-blue?style=flat-square&logo=react)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/language-TypeScript-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/backend-FastAPI-teal?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/language-Python-yellow?style=flat-square&logo=python)](https://www.python.org/)
[![Google ADK](https://img.shields.io/badge/AI-Google_ADK-red?style=flat-square&logo=google)](https://developers.generativeai.google/)

</div>

## 📚 Overview

AI Tutor is an educational application that leverages advanced AI to provide personalized tutoring in chemistry, mathematics, and physics. The application uses a specialized agent system to route questions to the appropriate subject expert, ensuring accurate and helpful responses for students.

## ✨ Features

- **Subject-Specific AI Tutoring**: Specialized agents for chemistry, mathematics, and physics
- **Intelligent Query Routing**: Automatically directs questions to the appropriate subject expert
- **Beautiful Chat Interface**: Modern, responsive UI with real-time typing indicators
- **Markdown Support**: Renders formatted text, code blocks, and mathematical expressions
- **Error Handling**: Graceful error management with user-friendly messages

## 🏗️ Architecture

The project is divided into two main components:

### Backend (`AiTutor_backend`)

- Built with FastAPI and Google's Agent Development Kit (ADK)
- Implements a root agent that routes queries to specialized subject agents
- Provides a RESTful API endpoint for the frontend to communicate with

### Frontend (`AiTutor_frontend`)

- Built with Next.js, React, and TypeScript
- Features a modern, responsive UI with animations and a chat interface
- Communicates with the backend API to process user queries
- Renders AI responses with proper formatting for educational content

## 🚀 Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.9 or higher)
- npm or yarn
- pip

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd AiTutor_backend
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the backend server:
   ```bash
   python main.py
   ```
   The server will start on http://localhost:8000

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd AiTutor_frontend
   ```

2. Install the required dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Run the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```
   The application will be available at http://localhost:3000

## 🔧 API Endpoints

- `GET /health`: Check if the API is running
- `POST /ask`: Send a question to the AI tutor
  - Request body: `{ "question": "Your question here" }`
  - Response: `{ "response": "AI response" }`

## 🧠 AI Agents

The system uses three specialized agents:

1. **Chemistry Agent**: Handles questions about chemical elements, reactions, compounds, and the periodic table
2. **Mathematics Agent**: Solves problems related to algebra, calculus, geometry, and other math topics
3. **Physics Agent**: Answers questions about mechanics, electricity, thermodynamics, and other physics concepts

The root agent intelligently routes queries to the appropriate specialized agent based on the question's content.

## 🛠️ Technologies Used

### Backend
- Python
- FastAPI
- Google ADK (Agent Development Kit)
- Gemini 2.0 Flash model

### Frontend
- Next.js
- React
- TypeScript
- TailwindCSS
- Lucide React (for icons)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

<div align="center">

Made with ❤️ for education

</div>
