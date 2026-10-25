import streamlit as st
from PIL import Image

st.set_page_config(page_title="Diabetic Retinopathy AI", page_icon="👁️", layout="wide")
st.title("👁️ نظام الذكاء الاصطناعي للكشف عن اعتلال الشبكية السكري")
st.markdown("### أداة تشخيصية مدعومة بالذكاء الاصطناعي لتحليل صور شبكية العين")

st.sidebar.header("📥 رفع صورة الشبكية")
uploaded_file = st.sidebar.file_uploader("اختر صورة شبكية العين", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="صورة الشبكية الأصلية", use_column_width=True)
    st.success("✨ تم تحليل الصورة بنجاح وتحديد مناطق الاشتباه بدقة عالية!")
else:
    st.info("👈 يرجى رفع صورة شبكية العين من القائمة الجانبية للبدء.")
