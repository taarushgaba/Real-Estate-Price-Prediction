
import streamlit as st
import requests


st.set_page_config(
    page_title="Real Estate Price Prediction",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)



st.markdown("""
<style>

    /* =========================
       GLOBAL
       ========================= */

    :root {
        --ink: #020407;
        --navy: #161d24;
        --panel: #151c23;
        --panel-light: #151c23;
        --line: #303b46;
        --text: #edf6ff;
        --muted: #9db2c9;
        --accent: #35c6bd;
        --accent-dark: #147f88;
    }

    html,
    body,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] > .main {
        background:
            radial-gradient(circle at 8% 0%, rgba(31, 91, 133, 0.3), transparent 32%),
            radial-gradient(circle at 92% 20%, rgba(20, 127, 136, 0.16), transparent 26%),
            #020407 !important;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
        animation: page-rise 0.55s ease-out both;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(145deg, rgba(26, 33, 41, 0.96), rgba(14, 19, 24, 0.96));
        border: 1px solid #303b46;
        border-radius: 20px;
        box-shadow: 0 18px 42px rgba(0, 0, 0, 0.22);
        padding: 0.45rem 0.8rem 0.8rem;
        transition: border-color 0.2s ease, transform 0.2s ease;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #34749a;
        transform: translateY(-2px);
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* =========================
       HERO
       ========================= */

    .hero {
        background: #14253d;

        border-radius: 26px;
        padding: 28px 36px;
        color: white;
        margin-bottom: 24px;

        box-shadow:
            0 18px 45px rgba(31, 41, 55, 0.18);

        position: relative;
        overflow: hidden;
    }

    .hero::after {
        content: "⌂";
        position: absolute;
        right: 55px;
        top: 5px;

        font-size: 170px;
        font-weight: 800;

        opacity: 0.05;
    }

    .hero-tag {
        display: inline-block;

        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);

        padding: 7px 14px;
        border-radius: 20px;

        font-size: 12px;
        font-weight: 600;

        letter-spacing: 0.6px;

        margin-bottom: 14px;
    }

    .hero-title {
        color: var(--text);
        font-size: 48px;
        font-weight: 800;

        letter-spacing: -1.5px;
        line-height: 1.1;

        margin: 0 0 28px;
        text-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        position: relative;
    }

    .hero-title::after {
        content: "";
        display: block;
        width: 64px;
        height: 3px;
        margin-top: 14px;
        border-radius: 3px;
        background: linear-gradient(90deg, var(--accent), transparent);
    }

    .hero-subtitle {
        margin-top: 13px;

        font-size: 16px;
        line-height: 1.6;

        color: rgba(255,255,255,0.78);

        max-width: 630px;
    }


    /* =========================
       SECTION TITLES
       ========================= */

    .section-title {
        font-size: 23px;
        font-weight: 750;

        color: var(--text);

        margin-bottom: 3px;
    }

    .section-subtitle {
        color: var(--muted);

        font-size: 14px;

        margin-bottom: 18px;
    }


    /* =========================
       INPUT CARD
       ========================= */

    .input-card {
        background: linear-gradient(145deg, #151c23, #10161c);

        border: 1px solid var(--line);

        border-radius: 20px;

        padding: 25px 27px 22px;

        box-shadow: 0 18px 42px rgba(0, 0, 0, 0.2);
    }


    /* =========================
       INPUTS
       ========================= */

    label {
        color: var(--text) !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="input"],
    div[data-baseweb="input"] > div,
    div[data-baseweb="input"] input,
    div[data-baseweb="select"] > div,
    div[data-baseweb="select"] [role="combobox"] {
        border-radius: 10px;
        background: #151c23 !important;
        border: 1px solid #303b46 !important;
        color: var(--text);
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    div[data-baseweb="input"]:focus-within,
    div[data-baseweb="select"] > div:focus-within {
        border-color: var(--accent);
        box-shadow: 0 0 0 3px rgba(53, 198, 189, 0.16);
    }

    div[data-baseweb="select"] span {
        color: var(--text) !important;
    }

    div[data-baseweb="input"] button {
        background: #1b344f !important;
        border-color: #315674 !important;
        color: #a9c9df !important;
    }

    div[data-baseweb="input"] button:hover {
        background: #244563 !important;
        color: #d9efff !important;
    }


    /* =========================
       PROPERTY SUMMARY
       ========================= */

    .summary-card {
        background: linear-gradient(145deg, #151c23, #10161c);

        border: 1px solid var(--line);

        border-radius: 20px;

        padding: 25px;

        box-shadow: 0 18px 42px rgba(0, 0, 0, 0.2);
    }

    .summary-header {
        font-size: 19px;
        font-weight: 750;

        color: var(--text);

        margin-bottom: 18px;
    }

    .summary-item {
        display: flex;

        justify-content: space-between;

        padding: 11px 0;

        border-bottom: 1px solid rgba(40, 82, 125, 0.7);

        font-size: 14px;
    }

    .summary-item:last-child {
        border-bottom: none;
    }

    .summary-label {
        color: var(--muted);
    }

    .summary-value {
        color: var(--text);
        font-weight: 650;
    }


    /* =========================
       PROPERTY PROFILE
       ========================= */

    .profile-box {
        background: #1b232b;

        border-radius: 14px;

        padding: 14px 16px;

        margin-top: 18px;

        border: 1px solid #3b4854;
    }

    .profile-title {
        font-size: 11px;

        color: #9ce4df;

        text-transform: uppercase;

        letter-spacing: 0.8px;

        font-weight: 700;
    }

    .profile-value {
        font-size: 17px;

        color: #d9f7f4;

        font-weight: 750;

        margin-top: 3px;
    }


    /* =========================
       PREDICT BUTTON
       ========================= */

    .stButton > button {
        width: 100%;

        height: 55px;

        border-radius: 13px;

        border: none;

        background:
            linear-gradient(
                135deg,
                #2563eb,
                #1d4ed8
            );

        color: white;

        font-size: 16px;

        font-weight: 700;

        box-shadow:
            0 7px 18px rgba(37, 99, 235, 0.25);

        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 10px 23px rgba(37, 99, 235, 0.32);

        color: white;
    }


    /* =========================
       RESULT CARD
       ========================= */

    .prediction-output {
        margin-top: 24px;
        padding: 16px 18px;
        background: linear-gradient(145deg, #1b232b, #12191f);
        border: 1px solid #303b46;
        border-radius: 12px;
        text-align: center;
    }

    .result-small {
        font-size: 12px;

        color: #a4c0d4;

        text-transform: uppercase;

        letter-spacing: 1.5px;

        font-weight: 750;
    }

    .result-price {
        font-size: 34px;

        font-weight: 850;

        color: #e7fbff;

        margin: 8px 0 13px;

        letter-spacing: -1px;
    }

    .result-category {
        display: inline-block;

        background: rgba(53, 198, 189, 0.09);

        color: #92d7d2;

        padding: 8px 18px;

        border-radius: 30px;

        font-size: 13px;

        font-weight: 700;
    }


    /* =========================
       STAT CARDS
       ========================= */

    .info-card {
        background: var(--panel-light);

        border: 1px solid var(--line);

        border-radius: 16px;

        padding: 18px;

        text-align: center;

        box-shadow:
            0 5px 18px rgba(0,0,0,0.025);
    }

    .info-number {
        font-size: 21px;

        font-weight: 750;

        color: var(--text);
    }

    .info-label {
        color: var(--muted);

        font-size: 12px;

        margin-top: 3px;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;

        color: #7f91a6;

        font-size: 12px;

        margin-top: 40px;
    }

    .summary-item {
        transition: background 0.2s ease, padding-left 0.2s ease;
    }

    .summary-item:hover {
        background: rgba(53, 198, 189, 0.08);
        padding-left: 8px;
        padding-right: 8px;
        border-radius: 6px;
    }

    .profile-box,
    .prediction-output {
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.18);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .profile-box:hover,
    .prediction-output:hover {
        transform: translateY(-2px);
        border-color: var(--accent);
    }

    .stButton > button {
        background: linear-gradient(135deg, #18456f, #102e4e);
        color: #e5f1ff;
        box-shadow: 0 10px 26px rgba(16, 46, 78, 0.3);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #225b8f, #153c63);
        color: #f0f7ff;
        box-shadow: 0 14px 32px rgba(16, 46, 78, 0.36);
    }

    @keyframes page-rise {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

</style>
""", unsafe_allow_html=True)



st.markdown(
    '<div class="hero-title">Real Estate Price Prediction</div>',
    unsafe_allow_html=True
)



left, right = st.columns(
    [1.65, 1],
    gap="large"
)



with left.container(border=True):

    st.markdown(
        '<div class="section-title">Property details</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Adjust the details below to describe the property.'
        '</div>',
        unsafe_allow_html=True
    )

    

    col1, col2 = st.columns(2)

    with col1:

        area = st.number_input(
            "Area (sqft)",
            min_value=1.0,
            value=1200.0,
            step=50.0
        )

    with col2:

        bedrooms = st.number_input(
            "Bedrooms",
            min_value=1,
            value=3,
            step=1
        )



    col3, col4 = st.columns(2)

    with col3:

        bathrooms = st.number_input(
            "Bathrooms",
            min_value=1,
            value=2,
            step=1
        )

    with col4:

        stories = st.number_input(
            "Stories",
            min_value=1,
            value=2,
            step=1
        )




    col5, col6 = st.columns(2)

    with col5:

        parking = st.number_input(
            "Parking spaces",
            min_value=0,
            value=1,
            step=1
        )

    with col6:

        mainroad = st.selectbox(
            "Main road access",
            [True, False],
            format_func=lambda x: "Yes" if x else "No"
        )



    furnishingstatus = st.selectbox(
        "Furnishing status",
        [
            "furnished",
            "semi-furnished",
            "unfurnished"
        ],
        format_func=lambda x:
            x.replace("-", " ").title()
    )


    st.write("")



    predict = st.button(
        "✦  Estimate Property Value"
    )



if area >= 2000:
    profile = "Spacious property"
elif area >= 1200:
    profile = "Mid-size property"
else:
    profile = "Compact property"



with right.container(border=True):

    st.markdown(
        '<div class="summary-header">'
        '🏡 Property profile'
        '</div>',
        unsafe_allow_html=True
    )



    st.html(
        f"""
        <div class="summary-item">
            <span class="summary-label">
                Area
            </span>

            <span class="summary-value">
                {area:,.0f} sqft
            </span>
        </div>

        <div class="summary-item">
            <span class="summary-label">
                Bedrooms
            </span>

            <span class="summary-value">
                {bedrooms}
            </span>
        </div>

        <div class="summary-item">
            <span class="summary-label">
                Bathrooms
            </span>

            <span class="summary-value">
                {bathrooms}
            </span>
        </div>

        <div class="summary-item">
            <span class="summary-label">
                Stories
            </span>

            <span class="summary-value">
                {stories}
            </span>
        </div>

        <div class="summary-item">
            <span class="summary-label">
                Parking
            </span>

            <span class="summary-value">
                {parking} space(s)
            </span>
        </div>

        <div class="summary-item">
            <span class="summary-label">
                Main road
            </span>

            <span class="summary-value">
                {"Yes" if mainroad else "No"}
            </span>
        </div>

        <div class="summary-item">
            <span class="summary-label">
                Furnishing
            </span>

            <span class="summary-value">
                {furnishingstatus.replace("-", " ").title()}
            </span>
        </div>
        """
    )

    st.html(
        f"""
        <div class="profile-box">
            <div class="profile-title">Property profile</div>
            <div class="profile-value">{profile}</div>
        </div>
        """
    )

    prediction_placeholder = st.empty()



if predict:

    data = {

        "area": area,

        "bedrooms": bedrooms,

        "bathrooms": bathrooms,

        "stories": stories,

        "parking": parking,

        "mainroad": mainroad,

        "furnishingstatus": furnishingstatus

    }


   

    with st.spinner(
        "Analyzing property details..."
    ):

        try:

          

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=data
            )


            response.raise_for_status()


            result = response.json()


            predicted_price = result[
                "predicted_price"
            ]

            predicted_category = result[
                "predicted_category"
            ]


           

            try:

                formatted_price = (
                    f"₹ {float(predicted_price):,.0f}"
                )

            except:

                formatted_price = (
                    f"₹ {predicted_price}"
                )




            prediction_placeholder.html(
                f"""
                <div class="prediction-output">

                    <div class="result-small">
                        Estimated property value
                    </div>

                    <div class="result-price">
                        {formatted_price}
                    </div>

                    <div class="result-category">
                        {predicted_category}
                    </div>

                </div>

                """
            )


        
        except requests.exceptions.ConnectionError:

            st.error(
                "⚠️ Unable to connect to the FastAPI server. "
                "Make sure FastAPI is running on port 8000."
            )


       

        except requests.exceptions.HTTPError:

            st.error(
                f"⚠️ FastAPI returned an error: "
                f"{response.status_code}"
            )

            st.code(
                response.text
            )


        

        except Exception as e:

            st.error(
                f"⚠️ Prediction error: {e}"
            )
