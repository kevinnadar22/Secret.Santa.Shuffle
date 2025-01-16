<div align="center">

# 🎅 Secret Santa Shuffle

> Tired of drawing names from a hat? Make Secret Santa fun and easy with digital shuffling!

<img src="https://cdn.elearningindustry.com/wp-content/uploads/2021/11/shutterstock_1820896832.jpg" alt="Secret Santa Shuffle Preview" width="600"/>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green?logo=flask)](https://flask.palletsprojects.com/)
[![Socket.IO](https://img.shields.io/badge/Socket.IO-4.0+-black?logo=socket.io)](https://socket.io/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0-blue?logo=tailwind-css)](https://tailwindcss.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/kevinnadar22/Secret.Santa.Shuffle)

### 🎯 No More Paper Slips | 🌍 Perfect for Remote Groups | ⚡ Instant Results

*Say goodbye to the traditional paper-based Secret Santa! Create digital rooms instantly, invite participants, and let the app handle the gift assignments automatically. Perfect for remote teams, families, and friend groups across the globe!*

[Features](#-features) •
[Installation](#-installation) •
[Deployment](#-deployment) •
[Contributing](#-contributing)

</div>

---

## 📋 Table of Contents
- [Features](#-features)
- [Quick Start](#-quick-start)
- [Deployment](#-deployment)
  - [Heroku](#heroku)
  - [Docker](#docker)
- [Development](#-development)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

<div align="center">

| 🎯 Core Features | 🛠️ Technical Features | 🎨 UI Features |
|:---------------:|:--------------------:|:-------------:|
| Gift Assignment | WebSocket | Responsive Design |
| Room Creation | Cache Storage | Modern Interface |
| Room Codes | Session Management | Animated Transitions |

</div>

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/kevinnadar22/Secret.Santa.Shuffle
cd Secret.Santa.Shuffle

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python run.py
```

Visit `http://localhost:5000` in your browser.

## 🌐 Deployment

### Heroku

One-click deployment:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/kevinnadar22/Secret.Santa.Shuffle)



### Docker

```bash
# Build image
docker build -t santa-shuffle .

# Run container
docker run -p 5000:5000 -e SECRET_KEY=your_secret_key santa-shuffle
```


## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. 💫 Commit your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. 📤 Push to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. 🎉 Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### Made by [Kevin Nadar](https://github.com/kevinnadar22)

<p align="center">
  <a href="https://github.com/kevinnadar22">
    <img src="https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github">
  </a>
</p>

</div>
