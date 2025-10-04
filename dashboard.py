import streamlit as st
import pandas as pd
import boto3

# --------------------------
# Streamlit Ayarları
# --------------------------
st.set_page_config(
    page_title="Email Dashboard",
    layout="wide"
)

st.title("🏠 Email Dashboard")

# --------------------------
# S3'ten CSV oku
# --------------------------
@st.cache_data
def load_data():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"],
        region_name=st.secrets["AWS_REGION"]
    )
    obj = s3.get_object(Bucket=st.secrets["BUCKET_NAME"], Key=st.secrets["FILE_KEY"])
    df = pd.read_csv(obj["Body"])
    return df


if st.button("🔄 Refresh Data"):
    st.cache_data.clear()
    st.rerun()

# --------------------------
# Veriyi Yükle ve Göster
# --------------------------
df = load_data()

st.data_editor(
    df,
    hide_index=True,
    disabled=True,
    height=700,
    use_container_width=True
)
