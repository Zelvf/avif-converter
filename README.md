# 📸 AVIF Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Vercel](https://img.shields.io/badge/Vercel-Hosted-black?logo=vercel)](https://vercel.com)

A powerful, multi-platform image converter that transforms your JPG and PNG files into high-performance **AVIF** format. Reduce your image file sizes by up to 50% or more while maintaining superior visual quality.

Available as a **Desktop GUI**, **CLI Tool**, and **Web Application**.

---

## 🚀 Features

-   **Desktop GUI:** Easy-to-use interface built with `customtkinter`.
-   **CLI Support:** Batch convert entire directories with a single command.
-   **Web Version:** Fully responsive web app ready for Vercel hosting.
-   **High Performance:** Optimized conversion using `Pillow` and `pillow-avif-plugin`.
-   **Batch Processing:** Convert multiple files simultaneously.
-   **Customizable Quality:** Fine-tune the quality/size tradeoff (1-100).

---

## 💻 Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/avif-converter.git
cd avif-converter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🛠 Usage

### 🖥 GUI Mode (Desktop)
Run the main application for a friendly windowed experience:
```bash
python main.py
```

### ⌨ CLI Mode (Batch Processing)
Perfect for developers and power users:
```bash
python batch_convert.py /path/to/source /path/to/destination --quality 80
```

### 🌐 Web Mode (Vercel)
The web version is located in the `api/` and `public/` directories. You can deploy it directly to Vercel:
1. Push this repo to GitHub.
2. Connect your repo to [Vercel](https://vercel.com).
3. Vercel will automatically detect the configuration and deploy.

---

## 📦 Requirements

-   Python 3.8+
-   `Pillow`
-   `pillow-avif-plugin`
-   `customtkinter` (for GUI)
-   `fastapi`, `python-multipart`, `uvicorn` (for Web version)

---

## 🚀 Deploying to Vercel

This project is pre-configured for Vercel Serverless Functions.

1. Install the Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the root directory.
3. Follow the prompts to deploy.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

*Made with ❤️ for better web performance.*
