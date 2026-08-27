import pandas as pd
import streamlit as st
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="LLM Evaluation Lab",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# DATA PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "evaluation_results.csv"


# ============================================================
# CUSTOM DARK UI
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL BACKGROUND
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 10%,
                rgba(25, 75, 125, 0.10),
                transparent 260px
            ),
            radial-gradient(
                circle at 85% 25%,
                rgba(55, 45, 110, 0.08),
                transparent 300px
            ),
            #05080b;

        color: #dbe5ee;
    }


    /* ========================================================
       SUBTLE WATER / DROPLET TEXTURE
       ======================================================== */

    .stApp::before {

        content: "";

        position: fixed;

        inset: 0;

        pointer-events: none;

        z-index: 0;

        opacity: 0.45;

        background:

            radial-gradient(
                circle at 8% 12%,
                rgba(255,255,255,0.055) 0px,
                rgba(255,255,255,0.020) 2px,
                transparent 7px
            ),

            radial-gradient(
                circle at 22% 42%,
                rgba(255,255,255,0.045) 0px,
                rgba(255,255,255,0.015) 3px,
                transparent 8px
            ),

            radial-gradient(
                circle at 47% 18%,
                rgba(255,255,255,0.045) 0px,
                rgba(255,255,255,0.012) 3px,
                transparent 9px
            ),

            radial-gradient(
                circle at 71% 62%,
                rgba(255,255,255,0.045) 0px,
                rgba(255,255,255,0.012) 3px,
                transparent 9px
            ),

            radial-gradient(
                circle at 91% 32%,
                rgba(255,255,255,0.050) 0px,
                rgba(255,255,255,0.015) 3px,
                transparent 8px
            );

        background-size:
            170px 210px,
            230px 260px,
            260px 220px,
            250px 290px,
            200px 240px;
    }


    /* ========================================================
       SLOW DIAGONAL BLUE MOTION
       ======================================================== */

    .stApp::after {

        content: "";

        position: fixed;

        inset: -100%;

        pointer-events: none;

        z-index: 0;

        background:
            repeating-linear-gradient(
                125deg,
                transparent 0px,
                transparent 190px,
                rgba(45, 130, 230, 0.025) 191px,
                rgba(75, 155, 255, 0.045) 192px,
                rgba(45, 130, 230, 0.025) 193px,
                transparent 194px,
                transparent 360px
            );

        animation:
            backgroundDrift 32s linear infinite;
    }


    @keyframes backgroundDrift {

        0% {
            transform: translate3d(-100px, -100px, 0);
        }

        50% {
            transform: translate3d(80px, 80px, 0);
        }

        100% {
            transform: translate3d(260px, 260px, 0);
        }

    }


    /* ========================================================
       CONTENT LAYER
       ======================================================== */

    .stApp > div {
        position: relative;
        z-index: 1;
    }


    .block-container {

        max-width: 1500px;

        padding-top: 2.5rem;

        padding-bottom: 3rem;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #06090d 0%,
                #070b10 100%
            );

        border-right:
            1px solid rgba(80, 125, 170, 0.12);
    }


    section[data-testid="stSidebar"] * {
        color: #cbd7e2;
    }


    /* ========================================================
       TYPOGRAPHY
       ======================================================== */

    h1 {

        color: #edf5fc !important;

        font-size: 2.35rem !important;

        font-weight: 600 !important;

        letter-spacing: -0.8px;
    }


    h2 {

        color: #e4edf5 !important;

        font-weight: 500 !important;
    }


    h3 {

        color: #dce7f0 !important;

        font-weight: 500 !important;
    }


    p {

        color: #9baab9;
    }


    /* ========================================================
       METRIC CARDS
       ======================================================== */

    div[data-testid="stMetric"] {

        background:
            linear-gradient(
                145deg,
                rgba(18, 25, 32, 0.94),
                rgba(7, 11, 15, 0.96)
            );

        border:
            1px solid rgba(100, 145, 185, 0.16);

        border-radius: 12px;

        padding: 20px;

        box-shadow:
            0 14px 35px rgba(0, 0, 0, 0.28);

        backdrop-filter: blur(8px);

        transition:
            transform 0.2s ease,
            border-color 0.2s ease;
    }


    div[data-testid="stMetric"]:hover {

        transform: translateY(-2px);

        border-color:
            rgba(55, 145, 255, 0.38);
    }


    div[data-testid="stMetricLabel"] {

        color: #7f8e9e !important;

        font-size: 0.74rem !important;

        text-transform: uppercase;

        letter-spacing: 0.8px;
    }


    div[data-testid="stMetricValue"] {

        color: #edf5fb !important;

        font-weight: 500 !important;
    }


    /* ========================================================
       DATAFRAME
       ======================================================== */

    div[data-testid="stDataFrame"] {

        border:
            1px solid rgba(100, 145, 185, 0.14);

        border-radius: 12px;

        overflow: hidden;

        background:
            rgba(7, 11, 15, 0.86);

        box-shadow:
            0 12px 30px rgba(0, 0, 0, 0.25);
    }


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {

        border: none;

        border-top:
            1px solid rgba(100, 145, 185, 0.12);

        margin: 2rem 0;
    }


    /* ========================================================
       INFO BOX
       ======================================================== */

    div[data-testid="stAlert"] {

        background:
            rgba(12, 20, 28, 0.85);

        border-radius: 10px;

        border:
            1px solid rgba(60, 135, 210, 0.20);
    }


    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    """Load evaluation results from the project dataset."""

    if not DATA_FILE.exists():
        st.error(
            f"Evaluation dataset not found: {DATA_FILE}"
        )
        st.stop()

    return pd.read_csv(DATA_FILE)


df = load_data()


# ============================================================
# VALIDATE DATA
# ============================================================

required_columns = [
    "id",
    "accuracy",
    "relevance",
    "completeness",
    "instruction_following",
    "hallucination",
    "overall_score",
]


missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]


if missing_columns:

    st.error(
        "The evaluation dataset is missing: "
        + ", ".join(missing_columns)
    )

    st.stop()


# ============================================================
# CALCULATE METRICS
# ============================================================

accuracy = df["accuracy"].mean()

relevance = df["relevance"].mean()

completeness = df["completeness"].mean()

instruction_following = (
    df["instruction_following"].mean()
)


hallucination_rate = (
    (df["hallucination"] > 0).mean()
) * 100


weighted_score = (

    (accuracy * 0.35)

    + (relevance * 0.25)

    + (completeness * 0.20)

    + (instruction_following * 0.20)
)


overall_score = (
    weighted_score / 5
) * 100


# ============================================================
# QUALITY CLASSIFICATION
# ============================================================

if overall_score >= 90:

    classification = "Excellent"

elif overall_score >= 80:

    classification = "Strong"

elif overall_score >= 70:

    classification = "Acceptable"

elif overall_score >= 60:

    classification = "Needs Improvement"

else:

    classification = "Poor"


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            padding: 10px 0 25px 0;
        ">

        <div style="
            font-size: 34px;
            margin-bottom: 8px;
        ">
        ◈
        </div>

        <div style="
            font-size: 19px;
            font-weight: 600;
            color: #e9f2fa;
        ">
        LLM Evaluation Lab
        </div>

        <div style="
            color: #738495;
            font-size: 13px;
            margin-top: 5px;
        ">
        AI Response Quality Framework
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    st.divider()


    st.markdown("### Overview")

    st.markdown(
        """
        **Evaluation Framework**

        Measures AI-generated responses
        across multiple quality dimensions.
        """
    )


    st.markdown("### Metrics")

    st.markdown(
        """
        • Accuracy  
        • Relevance  
        • Completeness  
        • Instruction Following  
        • Hallucination
        """
    )


    st.divider()


    st.caption(
        "LLM Evaluation Lab"
    )

    st.caption(
        "AI Quality & Evaluation"
    )


# ============================================================
# HEADER
# ============================================================

header_col, status_col = st.columns(
    [7, 1]
)


with header_col:

    st.title("LLM Evaluation Lab")

    st.markdown(
        """
        **AI Response Quality Evaluation Dashboard**

        Evaluate AI-generated responses across accuracy,
        relevance, completeness, instruction following,
        and hallucination detection.
        """
    )


with status_col:

    st.markdown(
        """
        <div style="
            margin-top: 15px;
            padding: 10px 14px;
            background: rgba(10, 20, 25, 0.75);
            border: 1px solid rgba(70, 140, 180, 0.18);
            border-radius: 9px;
            text-align: center;
        ">

        <span style="
            color: #4ade80;
            font-size: 11px;
        ">
        ●
        </span>

        <span style="
            color: #aebdca;
            font-size: 12px;
            margin-left: 5px;
        ">
        LIVE
        </span>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# OVERVIEW METRICS
# ============================================================

st.subheader("Evaluation Overview")


metric1, metric2, metric3, metric4 = st.columns(4)


with metric1:

    st.metric(
        "Overall Quality",
        f"{overall_score:.2f}/100",
    )


with metric2:

    st.metric(
        "Classification",
        classification,
    )


with metric3:

    st.metric(
        "Responses Evaluated",
        len(df),
    )


with metric4:

    st.metric(
        "Hallucination Rate",
        f"{hallucination_rate:.2f}%",
    )


# ============================================================
# QUALITY DIMENSIONS
# ============================================================

st.subheader("Quality Dimensions")


left, right = st.columns(
    [1, 1.15]
)


with left:

    st.markdown(
        "#### Dimension Scores"
    )


    dimensions = {

        "Accuracy": accuracy,

        "Relevance": relevance,

        "Completeness": completeness,

        "Instruction Following":
            instruction_following,
    }


    for name, score in dimensions.items():

        st.markdown(
            f"""
            <div style="
                margin-top: 18px;
                margin-bottom: 4px;
                color: #c7d2dd;
                font-size: 14px;
            ">
            {name}
            </div>

            <div style="
                width: 100%;
                height: 8px;
                background: #111a22;
                border-radius: 10px;
                overflow: hidden;
            ">

                <div style="
                    width: {(score / 5) * 100}%;
                    height: 100%;
                    background: linear-gradient(
                        90deg,
                        #1769d1,
                        #3b9cff
                    );
                    border-radius: 10px;
                ">
                </div>

            </div>

            <div style="
                text-align: right;
                color: #7f91a2;
                font-size: 12px;
                margin-top: 3px;
            ">
            {score:.2f} / 5
            </div>
            """,
            unsafe_allow_html=True,
        )


with right:

    st.markdown(
        "#### Evaluation Distribution"
    )


    chart_data = pd.DataFrame(
        {
            "Accuracy": [
                accuracy
            ],

            "Relevance": [
                relevance
            ],

            "Completeness": [
                completeness
            ],

            "Instruction Following": [
                instruction_following
            ],
        }
    )


    st.bar_chart(
        chart_data.T,
        height=280,
    )


# ============================================================
# EVALUATION RESULTS
# ============================================================

st.divider()

st.subheader("Evaluation Results")


display_columns = [
    "id",
    "accuracy",
    "relevance",
    "completeness",
    "instruction_following",
    "hallucination",
    "overall_score",
]


display_df = df[display_columns].copy()


display_df.columns = [
    "ID",
    "Accuracy",
    "Relevance",
    "Completeness",
    "Instruction Following",
    "Hallucination",
    "Overall Score",
]


st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# METHODOLOGY
# ============================================================

st.divider()

st.subheader("Evaluation Methodology")


method1, method2, method3 = st.columns(3)


with method1:

    st.markdown(
        "#### Weighted Scoring"
    )

    st.markdown(
        """
        **35% — Accuracy**

        **25% — Relevance**

        **20% — Completeness**

        **20% — Instruction Following**
        """
    )


with method2:

    st.markdown(
        "#### Scoring Scale"
    )

    st.markdown(
        """
        Each response dimension is scored
        from **0 to 5**.

        The weighted result is converted
        into a **0–100 quality score**.
        """
    )


with method3:

    st.markdown(
        "#### Hallucination Detection"
    )

    st.markdown(
        """
        Responses containing unsupported
        or fabricated information are
        flagged separately.

        This helps measure reliability
        independently from general quality.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "LLM Evaluation Lab  •  AI Quality & Evaluation Framework"
)