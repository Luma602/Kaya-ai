# KAYA – Dual System AI Architecture 🌱🤖

Kaya is a **dual-system AI assistant** designed with **one shared backend (brain)** and **two different interfaces**:
- A **public chatbot website** for everyone
- A **private owner application (PWA)** for development, control, and upgrades

---

## 🧩 System Overview

### 1️⃣ Public Website (Everyone)

- AI chatbot assistant
- No login required
- Read-only & safe
- Limited knowledge access
- Available publicly on the internet
- Hosted using Render

Purpose:
> To allow anyone to interact with Kaya as an assistant without risk.

---

### 2️⃣ Owner Application (Private – You Only)

- Login required (owner only)
- Full administrative control
- Weather API integration
- Knowledge editing (future upgrade)
- Offline mode support (future upgrade)
- Can be installed as a PWA on mobile

Purpose:
> To safely develop, manage, and evolve Kaya without affecting the public system.

---

## 🧠 Technology Stack

- **Python**
- **Flask** – Web framework
- **Flask-Login** – Authentication
- **Requests** – External APIs (weather, future services)
- **Gunicorn** – Production server
- **Render** – Cloud hosting
- **GitHub** – Source control

---

## 📂 Project Structure
