import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import streamlit.components.v1 as components

# --- Configuration ---
TARGET_DATE = datetime(2026, 1, 9, 0, 0, 0)
TITLE = "The Great Day Countdown"
GIF_PATH = "sabra gif.gif" # IMPORTANT: Ensure this GIF file is in the same directory as this Python script.

# --- Helper function ---
def get_countdown_components(target_date):
    """Calculates the time difference between now and the target date."""
    now = datetime.now()
    if now >= target_date:
        return None

    # Use relativedelta to get the exact years, months, days, etc.
    diff = relativedelta(target_date, now)
    return {
        "years": diff.years,
        "months": diff.months,
        "days": diff.days,
        "hours": diff.hours,
        "minutes": diff.minutes,
        "seconds": diff.seconds
    }

# --- Main App ---
def main():
    st.set_page_config(page_title=TITLE, layout="centered")

    # --- Global CSS Styling (moved all CSS here for centralization) ---
    st.markdown(
    """
    <style>
    /* Global Background and Text Alignment */
    body {
        background-color: #fff0f5;  /* soft wedding background */
        font-family: 'Inter', sans-serif;
    }
    h1, h3, p {
        text-align: center;
    }

    /* Make images responsive and centered (for the GIF) */
    .stImage > img {
        max-width: 100% !important;
        height: auto !important;
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    /* Keep countdown metrics (if we used them) in one row */
    .stColumns {
        display: flex !important;
        justify-content: center;
    }

    /* Make iframe responsive and centered */
    iframe {
        width: 100%;
        max-width: 600px; /* Increased max-width for better map view */
        height: 350px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    /* --- Custom HTML Countdown Component Styling --- */
    .countdown-wrapper {
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap; /* Allow wrapping on very small screens */
        margin-top: 25px;
        margin-bottom: 30px;
        text-align: center;
        padding: 15px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.8); /* Slight transparent white background for contrast */
        box-shadow: 0 4px 15px rgba(185, 28, 28, 0.3); /* Subtle wedding-themed shadow */
    }

    .count-item {
        min-width: 70px; /* Ensure columns don't collapse too much */
    }

    .count-num {
        font-size: 2.5rem;
        font-weight: 800;
        color: #b91c1c; /* Deep red for emphasis */
        line-height: 1;
    }

    .count-label {
        font-size: 0.9rem;
        color: #6b7280; /* Gray for readability */
        margin-top: 5px;
    }

    @media (max-width: 600px) {
        .count-num {
            font-size: 1.8rem;
        }
        .count-label {
            font-size: 0.8rem;
        }
        .countdown-wrapper {
            gap: 10px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # --- Title ---
    st.markdown(
        """
        <h1 style='text-align:center; color:#b91c1c; font-size:2.5rem; margin-top: 0;'>
            The Great Day Countdown
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <h3 style='text-align:center; color:#4b5563; font-size:1.25rem;'>
        <b>💖 Mohamed & Sara 💖</b> <br>
        Invite you to Celebrate their Love 💍
        and join them on their Wedding Day.
        <br>
        Friday, {TARGET_DATE.strftime('%B %d, %Y')} at 7:00 PM
        </h3>
        """,
        unsafe_allow_html=True
    )

    # --- Countdown placeholder ---
    placeholder = st.empty()

    # --- Wedding image (GIF) ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Use an external placeholder image if the GIF is missing, or rely on the user to provide it.
        # For deployment, the user MUST ensure 'sabra gif.gif' is available.
        try:
             st.image(GIF_PATH, width=330, caption="Mohamed & Sara")
        except FileNotFoundError:
             st.error(f"Image file '{GIF_PATH}' not found. Please ensure it's in the same directory.")
    
    # --- Map Section ---
    # st.markdown("<hr style='border: 1px solid #fecaca; margin: 30px 0;'>", unsafe_allow_html=True)
    
    st.markdown(
        """<p style='text-align:center; color:#6b7280; font-size:1.8rem; font-weight: 600;'>Location: Dar Zumuruda Mirage Hall.</p><br>
        <center><p>location at google map.</p></center>""",
        unsafe_allow_html=True
    )
    
    map_html = """
        <div style='display:flex; justify-content:center;'>
             <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3456.123456789!2d31.123456!3d30.123456!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1458412b4d42a1c3%3A0x123456789abcdef!2sDar%20Zumuruda%20Mirage%20Hall!5e0!3m2!1sen!2seg!4v1700000000000!5m2!1sen!2seg"
        width="100%" 
        height="400" 
        style="border:0;" 
        allowfullscreen="" 
        loading="lazy">
    </iframe>
        </div>
    """
    components.html(map_html, height=380)

    # --- Live Countdown Loop ---
    while True:
        countdown = get_countdown_components(TARGET_DATE)

        if countdown is None:
            # Display final message and break loop
            placeholder.markdown(
                "<p style='text-align:center; font-size:2rem; font-weight:bold; color:#db2777; padding: 20px;'>🎉 It's The Wedding Day! 🎉</p>",
                unsafe_allow_html=True
            )
            break

        # Generate custom HTML structure for the countdown
        # This uses the custom CSS defined at the top
        countdown_html  = f"""
<div class="countdown-wrapper">
    <div class="count-item">
        <div class="count-num">{countdown['months']:02d}</div>
        <div class="count-label">💖 Months</div>
    </div>
    <div class="count-item">
        <div class="count-num">{countdown['days']:02d}</div>
        <div class="count-label">📅 Days</div>
    </div>
    <div class="count-item">
        <div class="count-num">{countdown['hours']:02d}</div>
        <div class="count-label">⏰ Hours</div>
    </div>
    <div class="count-item">
        <div class="count-num">{countdown['minutes']:02d}</div>
        <div class="count-label">⏱ Minutes</div>
    </div>
    <div class="count-item">
        <div class="count-num">{countdown['seconds']:02d}</div>
        <div class="count-label">⌛ Seconds</div>
    </div>
</div>
"""
        placeholder.markdown(countdown_html, unsafe_allow_html=True)

        time.sleep(1) # Update every second

if __name__ == "__main__":
    main()



