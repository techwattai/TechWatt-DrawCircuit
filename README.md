# TechWatt Circuit AI ⚡

**Design Circuits at the Speed of Thought.**

TechWatt Circuit AI is an intelligent engineering assistant that transforms text descriptions into professional wiring diagrams, firmware code, and bill of materials (BOM).

![TechWatt Circuit AI](https://via.placeholder.com/1200x600?text=TechWatt+Hero+Image) 
*(Note: Replace with actual screenshot)*

## 🚀 Features

### 1. Intelligent Diagrams
Describe any circuit (e.g., *"Arduino with HC-SR04 and a servo motor"*), and the AI generates a clear, pin-to-pin wiring diagram.
- **Microcontrollers**: Arduino, ESP32, Raspbery Pi, etc.
- **Smart Wiring**: Auto-routes connections with industry-standard colors (Red=VCC, Black=GND).

### 2. Auto-Generated Code 💻
Get production-ready firmware instantly.
- **C++**: For Arduino/ESP platforms.
- **Python**: For Raspberry Pi/Pico.
- **Comments**: Detailed explanation of logic.

### 3. Instant BOM & Cost Estimation 💰
Know the price before you build.
- **Real-time Estimation**: Checks current online market rates.
- **Sourcing**: Suggests where to buy components.

### 4. Cloud Saving & History ☁️
- **User Accounts**: Sign up to save your work.
- **Shareable Links**: Send your design to a friend or colleague with a single URL.
- **Version History**: Access your past designs anytime.

## 🛠️ Tech Stack

**Frontend**
- React + Vite
- TailwindCSS (Styling)
- React Flow (Diagrams)
- Framer Motion (Animations)

**Backend**
- Python FastAPI
- PostgreSQL (Database)
- OpenAI API (Intelligence)
- SQLAlchemy (ORM)

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tech-Watt/DrawCircuit.git
   cd DrawCircuit
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
   # .env file
   OPENAI_API_KEY=your_key
   DATABASE_URL=postgresql://user:pass@localhost:5432/db
   SECRET_KEY=your_secret
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## 🚀 Deployment

The project is configured for **Railway** deployment.
- **Backend**: Deploys as a Python service.
- **Frontend**: Deploys as a static site (using `serve`).
- **Database**: Requires a PostgreSQL service attached.

## 📄 License

MIT License - Created by TechWatt AI.
