import requests

import streamlit as st

st.title("The Dadinator")
st.image("dadinator.webp")
"""
## Built With

* [![Python][Python-shield]][Python-url]
* [![Streamlit][Streamlit-shield]][Streamlit-url]

[Streamlit-shield]: https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/
[Python-shield]: https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/

"""

def tell_me_a_joke():
  return requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"}).json()["joke"]

if st.button("Make me laugh!"):
  st.write(tell_me_a_joke())