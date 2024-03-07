import streamlit as st
from PIL import Image
from functions import *
import requests
from streamlit_lottie import st_lottie
import webbrowser

st.set_page_config(page_title="Cyberbullying", page_icon="logo.png")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl(
    "https://lottie.host/ea778dba-1c32-446e-9944-997643978f56/XyKvrkZVTU.json"
)
img_logo = Image.open(
    "/ComSci/2-year_Semester-2/Data Mining/project/Streamlit_app_cyber/image/logo.png"
)
img_stk = Image.open(
    "/ComSci/2-year_Semester-2/Data Mining/project/Streamlit_app_cyber/image/group.png"
)
img_stk2 = Image.open(
    "/ComSci/2-year_Semester-2/Data Mining/project/Streamlit_app_cyber/image/people.png"
)
bully_age = Image.open(
    "/ComSci/2-year_Semester-2/Data Mining/project/Streamlit_app_cyber/image/bully_age.png"
)
bully_ethnicity = Image.open(
    "/ComSci/2-year_Semester-2/Data Mining/project/Streamlit_app_cyber/image/bully_ethnicity.png"
)
bully_gender = Image.open(
    "/ComSci/2-year_Semester-2/Data Mining/project/Streamlit_app_cyber/image/bully_gender.png"
)
bully_religion = Image.open(
    "/ComSci/2-year_Semester-2/Data Mining/project/Streamlit_app_cyber/image/bully_religion.png"
)
bully_not = Image.open(
    "/ComSci/2-year_Semester-2/Data Mining/project/Streamlit_app_cyber/image/bully_not.png"
)

with st.container():
    logo_column, text_column = st.columns([1, 6])
    with logo_column:
        st.image(img_logo, width=100)
    with text_column:
        # ปรับแต่งสไตล์ CSS
        st.markdown(
            f"""
        <style>
        h1, h2 {{
        line-height: 0.2;
        color: #FF5E00;
        font-weight: bold;
        }}
        </style>
        """,
            unsafe_allow_html=True,
        )
        st.header("Cyberbullying")
        st.header("Detector")

with st.container():
    left_column, middle_column, right_column = st.columns([3, 0.5, 3])
    with left_column:
        st.markdown("______")
    with middle_column:
        st.image(img_stk2, width=50)
    with right_column:
        st.markdown("______")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        # ปรับแต่งสไตล์ CSS
        st.markdown(
            f"""
        <style>
        h3 {{
        line-height: 0.5;
        font-size: 49px;
        font-weight: bold;
        }}
        </style>
        """,
            unsafe_allow_html=True,
        )
        st.subheader("WE CAN STOP")
        st.subheader("CYBERBULLYING!")

        st.markdown(
            f"""
        <style>
        p {{
        line-height: 0.8;
        }}
        </style>
        """,
            unsafe_allow_html=True,
        )

        st.caption(
            """
            Here's how it works:

            1. Copy and paste text from social media posts, messages, or online forums.
            2. We will analyzes the content using advanced algorithms trained to identify characteristics associated with cyberbullying.
            3. Receive a clear indication of whether the content is likely to be cyberbullying or not.
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=350, key="coding")

with st.container():
    middle_column = st.columns(1)[0]
    with middle_column:
        st.markdown(
            f"""
        <style>
        input {{
        width: 200px;
        height: 150px;
        }}
        </style>
        """,
            unsafe_allow_html=True,
        )
        tweet_input = st.text_input("Enter text : ")
        st.button("ENTER")
        print(tweet_input)
        st.write(
            """
        ***
        """
        )

        st.markdown(
            f"""
        <style>
        h2 {{
        line-height: 0.5;
        }}
        em {{
        font-style: italic;
        font-size: 18px;
        font-weight: bold;
        line-height: 0.8;
        }}
        </style>
        """,
            unsafe_allow_html=True,
        )
        # print input on webpage
        st.header("Entered Tweet text ")
        if tweet_input:
            st.write(
                f"""
            ***{tweet_input}***
            """
            )
        else:
            st.write(
                """
            ***No Tweet Text Entered!***
            """
            )

        # justify content center
        st.markdown(
            f"""
        <style>
        .st-emotion-cache-1kyxreq {{
        justify-content: center;
        }}
        </style>
        """,
            unsafe_allow_html=True,
        )

        if tweet_input:
            prediction = custom_input_prediction(tweet_input)
            if prediction == "Age":
                st.image(bully_age, width=400)
            elif prediction == "Ethnicity":
                st.image(bully_ethnicity, width=400)
            elif prediction == "Gender":
                st.image(bully_gender, width=400)
            elif prediction == "Not Cyberbullying":
                st.image(bully_not, width=400)
            elif prediction == "Religion":
                st.image(bully_religion, width=400)

        st.write(
            """
        ***
        """
        )

        st.header("Learn more about Cyberbullying")
        st.write("")
        if tweet_input:
            prediction = custom_input_prediction(tweet_input)
            if prediction == "Age":
                st.video(
                    "https://www.youtube.com/watch?v=BIyOtjRY_0I&pp=ygUfaG93IHRvIGhhbmRsZSBhZ2UgY3liZXJidWxseWluZw%3D%3D"
                )
                if st.button("***Learn How to Deal With Cyberbullying***"):
                    resource_url = "https://parents.au.reachout.com/common-concerns/everyday-issues/cyberbullying-and-teenagers"
                    webbrowser.open(resource_url)
            elif prediction == "Ethnicity":
                st.video(
                    "https://www.youtube.com/watch?v=CFekuzaWcLI&pp=ygUjaG93IHRvIGhhbmRsZSBldGhpY2FsIGN5YmVyYnVsbHlpbmc%3D"
                )
                if st.button("***Learn How to Deal With Cyberbullying***"):
                    resource_url = "https://www.ipl.org/essay/Ethical-Issues-In-Social-Media-Bullying-P3RWGHHESJFR"
                    webbrowser.open(resource_url)
            elif prediction == "Gender":
                st.video("https://www.youtube.com/watch?v=iFlrCuSyhvU")
                if st.button("***Learn How to Deal With Cyberbullying***"):
                    resource_url = "https://spssi.onlinelibrary.wiley.com/doi/full/10.1111/josi.12503"
                    webbrowser.open(resource_url)
            elif prediction == "Religion":
                st.video("https://www.youtube.com/watch?v=dRAWq-JqLY4")
                if st.button("***Learn How to Deal With Cyberbullying***"):
                    resource_url = "https://cyberbullying.org/bullying-and-religion"
                    webbrowser.open(resource_url)
            elif prediction == "Not Cyberbullying":
                st.video("https://www.youtube.com/watch?v=dMdKmHjpgFk")
                if st.button("***Learn How to Deal With Cyberbullying***"):
                    resource_url = "https://www.hp.com/ca-en/shop/offer.aspx?p=best-ways-to-prevent-cyber-bullying-online"
                    webbrowser.open(resource_url)
        else:
            st.write(
                """***No information to display. Please enter a tweet text to get more information.***"""
            )

with st.container():
    left_column, middle_column, right_column = st.columns([3, 0.5, 3])
    with left_column:
        st.markdown("______")
    with middle_column:
        st.image(img_stk, width=50)
    with right_column:
        st.markdown("______")

# แสดงรายการ categories
categories = ["Age", "Ethnicity", "Gender", "Religion", "Not Cyberbullying"]

st.write("**Categories**")
for category in categories:
    st.write(f"- {category}")

st.markdown("______")
