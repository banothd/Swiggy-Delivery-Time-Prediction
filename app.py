import streamlit as st
import pandas as pd
import joblib
import base64


# ==================================================
# LOAD MODEL
# ==================================================

model = joblib.load("delivery_time_model.pkl")


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Food Delivery Time Prediction",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==================================================
# BACKGROUND IMAGE
# ==================================================

def set_background(image_file):

    with open(image_file, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image:
                linear-gradient(
                    rgba(7, 20, 38, 0.60),
                    rgba(7, 20, 38, 0.60)
                ),
                url("data:image/jpg;base64,{encoded_image}");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


set_background("background.jpg")


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    /* Main title */

    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 10px;
        margin-bottom: 5px;
    }


    /* Subtitle */

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #D9E2F2;
        margin-bottom: 30px;
    }


    /* Section titles */

    .section-title {
        font-size: 24px;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 20px;
        margin-bottom: 15px;
    }


    /* Input labels */

    label {
        color: #F2F5F9 !important;
        font-weight: 500 !important;
    }


    /* Select boxes and number inputs */

    div[data-baseweb="select"] > div,
    div[data-testid="stNumberInput"] > div {
        background-color: rgba(20, 28, 42, 0.92);
        border-radius: 8px;
    }


    /* Prediction button */

    div.stButton > button {
        background-color: #F28C28;
        color: white;
        border: none;
        border-radius: 10px;
        height: 50px;
        font-size: 17px;
        font-weight: 600;
    }


    div.stButton > button:hover {
        background-color: #FF9F43;
        color: white;
    }


    /* Divider */

    hr {
        border-color: rgba(255,255,255,0.20);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="main-title">Food Delivery Time Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict estimated food delivery time using machine learning'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# ORDER INFORMATION
# ==================================================

st.markdown(
    '<div class="section-title">Order Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


# --------------------------------------------------
# COLUMN 1
# --------------------------------------------------

with col1:

    weather = st.selectbox(
        "Weather",
        [
            "sunny",
            "cloudy",
            "fog",
            "sandstorms",
            "stormy",
            "windy"
        ]
    )

    type_of_order = st.selectbox(
        "Type of Order",
        [
            "buffet",
            "drinks",
            "meal",
            "snack"
        ]
    )

    festival = st.selectbox(
        "Festival",
        [
            "no",
            "yes"
        ]
    )


# --------------------------------------------------
# COLUMN 2
# --------------------------------------------------

with col2:

    traffic = st.selectbox(
        "Traffic",
        [
            "low",
            "medium",
            "high",
            "jam"
        ]
    )

    type_of_vehicle = st.selectbox(
        "Type of Vehicle",
        [
            "bicycle",
            "electric_scooter",
            "motorcycle",
            "scooter"
        ]
    )

    city_type = st.selectbox(
        "City Type",
        [
            "semi-urban",
            "urban",
            "metropolitian"
        ]
    )


# --------------------------------------------------
# COLUMN 3
# --------------------------------------------------

with col3:

    order_day_of_week = st.selectbox(
        "Order Day",
        [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday"
        ]
    )

    order_time_of_day = st.selectbox(
        "Order Time of Day",
        [
            "after midnight",
            "morning",
            "afternoon",
            "evening",
            "night"
        ]
    )

    order_priority = st.selectbox(
        "Order Priority",
        [
            "normal",
            "high"
        ]
    )


# ==================================================
# DELIVERY INFORMATION
# ==================================================

st.markdown(
    '<div class="section-title">Delivery Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


# --------------------------------------------------
# COLUMN 1
# --------------------------------------------------

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

    ratings = st.number_input(
        "Ratings",
        min_value=1.0,
        max_value=5.0,
        value=4.0,
        step=0.1
    )


# --------------------------------------------------
# COLUMN 2
# --------------------------------------------------

with col2:

    vehicle_condition = st.number_input(
        "Vehicle Condition",
        min_value=0,
        max_value=3,
        value=1
    )

    multiple_deliveries = st.number_input(
        "Multiple Deliveries",
        min_value=0,
        max_value=3,
        value=0
    )


# --------------------------------------------------
# COLUMN 3
# --------------------------------------------------

with col3:

    pickup_time_minutes = st.number_input(
        "Pickup Time (minutes)",
        min_value=0,
        max_value=60,
        value=15
    )

    distance = st.number_input(
        "Distance",
        min_value=0.0,
        max_value=50.0,
        value=5.0,
        step=0.1
    )


# --------------------------------------------------
# COLUMN 4
# --------------------------------------------------

with col4:

    order_time_hour = st.number_input(
        "Order Time Hour",
        min_value=0,
        max_value=23,
        value=12
    )

    is_weekend = st.selectbox(
        "Is Weekend",
        [0, 1]
    )


# ==================================================
# PREDICTION BUTTON
# ==================================================

st.markdown("<br>", unsafe_allow_html=True)

button_col1, button_col2, button_col3 = st.columns([1, 2, 1])

with button_col2:

    predict_button = st.button(
        "Predict Delivery Time",
        use_container_width=True
    )


# ==================================================
# PREDICTION
# ==================================================

if predict_button:

    # --------------------------------------------------
    # CREATE INPUT DATA
    # --------------------------------------------------

    input_data = pd.DataFrame({
        "age": [age],
        "ratings": [ratings],
        "vehicle_condition": [vehicle_condition],
        "is_weekend": [is_weekend],
        "multiple_deliveries": [multiple_deliveries],
        "pickup_time_minutes": [pickup_time_minutes],
        "order_time_hour": [order_time_hour],
        "distance": [distance],
        "weather": [weather],
        "type_of_order": [type_of_order],
        "type_of_vehicle": [type_of_vehicle],
        "festival": [festival],
        "order_day_of_week": [order_day_of_week],

        # Hidden from user, required by trained model
        "city_name": ["HYD"],

        "order_time_of_day": [order_time_of_day],
        "traffic": [traffic],
        "city_type": [city_type]
    })


    # --------------------------------------------------
    # MODEL PREDICTION
    # --------------------------------------------------

    prediction = model.predict(input_data)

    predicted_time = prediction[0]


    # ==================================================
    # RESULT
    # ==================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Delivery Prediction")


    # --------------------------------------------------
    # Main Prediction
    # --------------------------------------------------

    st.success(
        f"Estimated Delivery Time: {predicted_time:.2f} minutes"
    )


    # --------------------------------------------------
    # Prediction Details
    # --------------------------------------------------

    st.markdown("### Delivery Details")

    col1, col2, col3, col4, col5 = st.columns(5)


    # Distance
    with col1:

        st.info(
            f"Distance: \n\n{distance:.1f} km"
        )


    # Traffic
    with col2:

        if traffic == "low":
            st.success(
                f"Traffic: \n\n{traffic.title()}"
            )

        elif traffic == "medium":
            st.warning(
                f"Traffic: \n\n{traffic.title()}"
            )

        else:
            st.error(
                f"Traffic: \n\n{traffic.title()}"
            )


    # Weather
    with col3:

        st.warning(
            f"Weather: \n\n{weather.title()}"
        )


    # Vehicle
    with col4:

        st.info(
            f"Vehicle: \n\n"
            f"{type_of_vehicle.replace('_', ' ').title()}"
        )


    # Order Type
    with col5:

        st.success(
            f"Order Type: \n\n"
            f"{type_of_order.title()}"
        )
