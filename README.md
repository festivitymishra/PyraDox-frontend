# PyraDox-frontend:zap: 
[![Language](https://img.shields.io/badge/Python-3.6.5-blue)](https://github.com/festivitymishra/PyraDox-frontend)
[![tool](https://img.shields.io/badge/Streamlit-%3C3-red)](https://streamlit.io)

Streamlit based web frontend for **PyraDox :page_with_curl:**

[PyraDox](https://github.com/festivitymishra/PyraDox) is a simple tool which helps in document **digitization** by extracting text information and **masking** of personal information with the help of Tesseract-ocr.
*****************************************************
## Demo
#### click on the below video to play.
[![PyraDox Frontend Demo](resources/demo.png?raw=true "Click to play")](https://www.youtube.com/watch?v=Knyxk3vAONk)

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


## Notes

### License
[Apache License 2.0](https://github.com/festivitymishra/PyraDox-frontend/blob/master/LICENSE)

#### Sample Aadhar Cards are just samples taken from google search and not original documents.
If there is anything totally unclear, or not working, please feel free to file an issue.
reach out at [Email](utsav.iitkgp@gmail.com) :innocent:

If this project was helpful for you please show some love :star:

P.S. **Streamlit** is :heart:
