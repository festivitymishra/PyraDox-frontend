# PyraDox-frontend:zap: 
[![Language](https://img.shields.io/badge/Python-3.6.5-blue)](https://github.com/festivitymishra/PyraDox-frontend)
[![tool](https://img.shields.io/badge/Streamlit-%3C3-red)](https://streamlit.io)

Streamlit based web frontend for **PyraDox :page_with_curl:**

[PyraDox](https://github.com/festivitymishra/PyraDox) is a simple tool which helps in document **digitization** by extracting text information and **masking** of personal information with the help of Tesseract-ocr.
*****************************************************
## Demo

![Mask First Eight Digit Demo](resources/demo.gif)

*****************************************************
## Installation

#### Requirements
- [PyraDox](https://github.com/festivitymishra/PyraDox)
- [Streamlit](https://streamlit.io)
```bash
pip install streamlit
```
#### Steps
- Run PyraDox
##### Build Your Own PyraDox backend locally
```bash
python app.py #for using directly
```
##### OR Build PyraDox backend using Docker
```bash
docker build -t pyradox .
docker run -p 9001:9001 pyradox
```
- Run PyraDox-frontend
```bash
streamlit run pyradox.py
```
*****************************************************
P.S. **Streamlit** is :heart:
