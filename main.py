import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import streamlit.components.v1 as components

# --- Configuration ---
TARGET_DATE = datetime(2026, 1, 9, 0, 0, 0)
TITLE = "The Great Day Countdown"

# --- Helper functions ---
def get_countdown_components(target_date):
    now = datetime.now()
    if now >= target_date:
        return None

    diff = relativedelta(target_date, now)
    return {
        "years": diff.years,
        "months": diff.months,
        "days": diff.days,
        "hours": diff.hours,
        "minutes": diff.minutes,
        "seconds": diff.seconds
    }

def format_metric(col, value, label, emoji=""):
    col.metric(label=f"{emoji} {label}", value=f"{value:02d}", delta_color="off")

# --- Main App ---
def main():
    st.markdown(
    """
    <style>
    body {
        background-color: #fff0f5;  /* soft wedding background */
    }
    h1, h3, p {
        text-align: center;
    }

    /* Make images responsive */
    .stImage > img {
        max-width: 100% !important;
        height: auto !important;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* Keep countdown metrics in one row and responsive */
    .stMetric > div {
        text-align: center !important;
        flex: 1 1 0 !important;  /* allow shrinking proportionally */
        min-width: 60px;         /* prevent metrics from collapsing */
    }

    .stColumns {
        display: flex !important;
        flex-wrap: nowrap !important; /* keep in one row */
        justify-content: center;
    }

    /* Make iframe responsive */
    iframe {
        width: 100%;
        max-width: 500px;
        height: 320px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    @media (max-width: 500px) {
        .stMetric > div {
            min-width: 40px;  /* allow small screens */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

    st.set_page_config(page_title=TITLE, layout="centered")

    
    # --- Title ---
    st.markdown(
        """
        <h1 style='text-align:center; color:#b91c1c; font-size:2rem;'>
             The Great Day Countdown 
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <h3 style='text-align:center; color:#6b7280;'>
       <b>💖 Mohamed & Sara 💖</b> <br>
        Invite you to Celebrate their Love
        and join them on their Wedding Day.
        <br>
        Friday, {TARGET_DATE.strftime('%B %d, %Y')}
        <br>
        <b>At 7:00 PM</b>
        </h3>
        """,
        unsafe_allow_html=True
    )

    # --- Wedding image ---
    countdown = get_countdown_components(TARGET_DATE)

    if countdown is None:
        st.markdown(
"<p style='text-align:center; font-size:2rem; font-weight:bold; color:#db2777;'>🎉 It's The Wedding Day! 🎉</p>",
unsafe_allow_html=True
)

    # --- Countdown placeholder ---
    placeholder = st.empty()
    col1, col2, col3 = st.columns([1, 2, 1])  # middle column is wider
    with col2:
        st.image("sabra gif.gif", width=330)
    
    map_html = """
        <div style='display:flex; justify-content:center;'>
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d713.4572357953222!2d31.245209723711024!3d30.106784046199227!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1458401909243259%3A0x687fb3307fd76ba4!2z2YLYp9i52Ycg2LLZhdix2K_YqSDZhNmE2K3ZgdmE2KfYqg!5e1!3m2!1sar!2seg!4v1763382033537!5m2!1sar!2seg" 
                width="500" 
                height="320" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        </div>
            """
    st.markdown(
    "<p style='text-align:center; color:#6b7280; font-size:2.3rem;'>Location for Dar Zumuruda Mirage Hall</p>",
    unsafe_allow_html=True
)
    components.html(map_html, height=320)
    
    while True:
        countdown = get_countdown_components(TARGET_DATE)

        if countdown is None:
            st.markdown(
    "<p style='text-align:center; font-size:2rem; font-weight:bold; color:#db2777;'>🎉 It's The Wedding Day! 🎉</p>",
    unsafe_allow_html=True
)
            break

        countdown_html = f"""
    <div style="
        display:flex; 
        justify-content:center; 
        gap:30px; 
        flex-wrap: nowrap;
        font-family: 'Arial', sans-serif;
        margin-top:20px;
        margin-bottom:20px;
    ">
        <div style="text-align:center;">
            <div style="font-size:2rem; color:#fff;">{countdown['months']:02d}</div>
            <div style="color:#fff;">💖 Months</div>
        </div>
        <div style="text-align:center;">
            <div style="font-size:2rem; color:#fff;">{countdown['days']:02d}</div>
            <div style="color:#fff;">📅 Days</div>
        </div>
        <div style="text-align:center;">
            <div style="font-size:2rem; color:#fff;">{countdown['hours']:02d}</div>
            <div style="color:#fff;">⏰ Hours</div>
        </div>
        <div style="text-align:center;">
            <div style="font-size:2rem; color:#fff;">{countdown['minutes']:02d}</div>
            <div style="color:#fff;">⏱ Minutes</div>
        </div>
        <div style="text-align:center;">
            <div style="font-size:2rem; color:#fff;">{countdown['seconds']:02d}</div>
            <div style="color:#fff;">⌛ Seconds</div>
        </div>
    </div>
    """
        placeholder.markdown(countdown_html, unsafe_allow_html=True)

        time.sleep(1)

    # --- Map ---
    

if __name__ == "__main__":
    main()
