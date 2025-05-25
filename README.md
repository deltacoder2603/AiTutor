# AI Tutor

<div align="center">

![AI Tutor Logo](https://img.shields.io/badge/AI-Tutor-blueviolet?style=for-the-badge&logo=robot&logoColor=white)

**An intelligent learning companion powered by advanced AI**

Specialized tutoring in Chemistry, Mathematics, and Physics with personalized learning experiences

[![Live Demo](https://img.shields.io/badge/🌐-Live_Demo-success?style=for-the-badge)](https://ai-tutor-frontend-topaz.vercel.app/)

---

[![Next.js](https://img.shields.io/badge/frontend-Next.js-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/frontend-React-blue?style=flat-square&logo=react)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/language-TypeScript-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/backend-FastAPI-teal?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/language-Python-yellow?style=flat-square&logo=python)](https://www.python.org/)
[![Google ADK](https://img.shields.io/badge/AI-Google_ADK-red?style=flat-square&logo=google)](https://developers.generativeai.google/)

</div>

## 🎯 Overview

AI Tutor is a cutting-edge educational platform that transforms the learning experience through personalized AI-powered tutoring. Built with modern web technologies and powered by Google's advanced AI models, it provides students with instant, accurate, and contextually relevant assistance across three core STEM subjects.

**🚀 [Try it live →](https://ai-tutor-frontend-topaz.vercel.app/)**

## ✨ Key Features

### 🧠 Intelligent Learning System
- **Multi-Subject Expertise**: Specialized AI agents for Chemistry, Mathematics, and Physics
- **Smart Query Routing**: Automatically identifies and routes questions to the most appropriate subject expert
- **Contextual Understanding**: Processes complex questions with deep subject matter comprehension

### 💬 Modern Chat Experience
- **Real-time Interactions**: Instant responses with typing indicators for natural conversation flow
- **Rich Content Rendering**: Support for mathematical expressions, chemical formulas, and formatted text
- **Responsive Design**: Seamless experience across desktop, tablet, and mobile devices

### 🎨 User Experience
- **Intuitive Interface**: Clean, modern design focused on learning efficiency
- **Error Resilience**: Comprehensive error handling with helpful user guidance
- **Accessibility**: Built with accessibility standards for inclusive learning

## 🏗️ System Architecture

```
┌─────────────────┐    HTTP/REST     ┌──────────────────┐
│                 │ ◄─────────────── │                  │
│   Frontend      │                  │   Backend API    │
│   (Next.js)     │ ──────────────► │   (FastAPI)      │
│                 │                  │                  │
└─────────────────┘                  └──────────────────┘
                                               │
                                               ▼
                                     ┌──────────────────┐
                                     │   AI Agent       │
                                     │   Router         │
                                     └─────────┬────────┘
                                               │
                          ┌────────────────────┼────────────────────┐
                          │                    │                    │
                          ▼                    ▼                    ▼
                   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
                   │ Chemistry   │   │ Mathematics │   │ Physics     │
                   │ Agent       │   │ Agent       │   │ Agent       │
                   └─────────────┘   └─────────────┘   └─────────────┘
```

### Backend Components
- **FastAPI Framework**: High-performance REST API with automatic documentation
- **Google ADK Integration**: Leverages Google's Agent Development Kit for AI orchestration
- **Gemini 2.0 Flash**: Powered by Google's latest language model for accurate responses
- **Agent Router**: Intelligent query classification and routing system

### Frontend Components
- **Next.js Framework**: React-based full-stack framework with server-side rendering
- **TypeScript**: Type-safe development for enhanced code quality
- **TailwindCSS**: Utility-first CSS framework for rapid UI development
- **Real-time Communication**: Seamless API integration with loading states and error handling

## 🚀 Quick Start

### Prerequisites
```bash
Node.js >= 18.0.0
Python >= 3.9.0
npm or yarn
pip
```

### 🖥️ Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd AiTutor_backend
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment** (if needed)
   ```bash
   # Add any required environment variables
   export GOOGLE_API_KEY=your_api_key_here
   ```

4. **Start the server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   📍 Backend available at: `http://localhost:8000`

### 🎨 Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd AiTutor_frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Configure environment**
   ```bash
   # Create .env.local file
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

4. **Start development server**
   ```bash
   npm run dev
   # or
   yarn dev
   ```
   📍 Frontend available at: `http://localhost:3000`

## 📚 Subject Specialists

### 🧪 Chemistry Agent
Comprehensive coverage of chemical concepts including:
- **Periodic Table**: Element properties, trends, and relationships
- **Chemical Reactions**: Balancing equations, reaction mechanisms, kinetics
- **Molecular Structure**: Bonding theories, VSEPR, molecular geometry
- **Thermodynamics**: Enthalpy, entropy, free energy calculations

### 📐 Mathematics Agent
Advanced mathematical problem-solving across:
- **Algebra**: Linear equations, polynomials, systems of equations
- **Calculus**: Derivatives, integrals, differential equations
- **Geometry**: Euclidean and analytic geometry, trigonometry
- **Statistics**: Probability, distributions, hypothesis testing

### ⚡ Physics Agent
In-depth physics understanding covering:
- **Classical Mechanics**: Kinematics, dynamics, energy, momentum
- **Electromagnetism**: Electric fields, magnetic fields, circuits
- **Thermodynamics**: Heat transfer, laws of thermodynamics
- **Modern Physics**: Quantum mechanics, relativity, atomic structure

## 🔌 API Reference

### Health Check
```http
GET /health
```
**Response:** `200 OK`
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### Ask Question
```http
POST /ask
Content-Type: application/json
```

**Request Body:**
```json
{
  "question": "What is the molecular geometry of water?"
}
```

**Response:** `200 OK`
```json
{
  "response": "Water (H₂O) has a bent molecular geometry...",
  "subject": "chemistry",
  "confidence": 0.95
}
```

## 🛠️ Technology Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **Frontend** | Next.js, React, TypeScript, TailwindCSS |
| **Backend** | Python, FastAPI, Google ADK |
| **AI/ML** | Google Gemini 2.0 Flash, Agent Development Kit |
| **Development** | ESLint, Prettier, uvicorn |
| **Deployment** | Vercel (Frontend), Cloud hosting (Backend) |

</div>

## 📈 Performance Features

- **⚡ Fast Response Times**: Optimized API endpoints with sub-second response times
- **🔄 Real-time Updates**: Live typing indicators and instant message delivery
- **📱 Mobile Optimized**: Responsive design that works seamlessly on all devices
- **🛡️ Error Resilience**: Comprehensive error handling and graceful degradation

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow TypeScript/Python best practices
- Write comprehensive tests for new features
- Update documentation for API changes
- Ensure responsive design for UI changes

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google AI team for the powerful Gemini models and ADK
- Open source community for the amazing tools and libraries
- Educators and students who inspire continuous improvement

---

<div align="center">

**Made with ❤️ for the future of education**

[🌟 Star this project](https://github.com/yourusername/ai-tutor) • [🐛 Report Bug](https://github.com/yourusername/ai-tutor/issues) • [💡 Request Feature](https://github.com/yourusername/ai-tutor/issues)

</div>
