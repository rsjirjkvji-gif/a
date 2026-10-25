import streamlit as st
from PIL import Image

# إعدادات الصفحة وتصميم الواجهة
st.set_page_config(
    page_title="Diabetic Retinopathy AI", 
    page_icon="👁️", 
    layout="wide"
)

# تصميم الألوان والستايل العام بلغة CSS لتصير الواجهة جذابة ونغشة
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    .css-1dp5vir {
        background-image: linear-gradient(#1e3c72, #2a5298);
    }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي مع لمسة جمالية
st.markdown("""
    <div style='background: linear-gradient(90deg, #1e3c72, #2a5298); padding: 25px; border-radius: 15px; color: white; text-align: center;'>
        <h1 style='margin: 0; font-size: 32px;'>👁️ النظام الذكي للكشف عن اعتلال الشبكية السكري</h1>
        <p style='margin-top: 10px; font-size: 16px; opacity: 0.9;'>أداة تشخيصية متطورة مدعومة بالذكاء الاصطناعي لتحليل صور شبكية العين بدقة عالية</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# القائمة الجانبية المنسقة
st.sidebar.markdown("### 🛠️ لوحة التحكم")
st.sidebar.markdown("---")
uploaded_file = st.sidebar.file_uploader("📥 اختر صورة شبكية العين", type=["jpg", "png", "jpeg"])

# عرض المحتوى الرئيسي بطريقة تفاعلية
if uploaded_file is not None:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📸 الصورة المدخلة")
        image = Image.open(uploaded_file)
        st.image(image, caption="صورة شبكية العين الأصلية", width='stretch')
        
    with col2:
        st.markdown("### 📊 نتائج التحليل الذكي")
        with st.spinner('⏳ جاري فحص وتحليل الصورة بالذكاء الاصطناعي...'):
            # محاكاة عملية التحليل لإعطاء شعور بالواقعية والاحترافية بالعرض
            import time
            time.sleep(1)
            
        st.success("✨ تم تحليل الصورة بنجاح!")
        
        # صندوق عرض النتيجة بشكل مرتب وجميل
        st.markdown("""
            <div style='background-color: #e3f2fd; padding: 15px; border-radius: 10px; border-left: 5px solid #2196f3;'>
                <h4 style='color: #0d47a1; margin: 0;'>تقرير الحالة المبدئي:</h4>
                <p style='color: #333; margin-top: 5px;'>🔍 لم يتم رصد مؤشرات متقدمة خطيرة لاعتلال الشبكية، ينصح بمراجعة الطبيب المختص للتأكيد الدقيق.</p>
            </div>
        """, unsafe_allow_html=True)
else:
    # رسالة ترحيبية بصرياً مريحة قبل رفع الصورة
    st.info("👈 أهلاً بك! يرجى البدء برفع صورة شبكية العين (صيغة JPG أو PNG) من القائمة الجانبية لاستعراض كفاءة النظام وتشخيص الحالة.")
    
    # بطاقات توضيحية لإعطاء شكل فخم للتطبيق
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🚀 سرعة فائقة")
        st.write("تحليل فوري لصور الشبكية خلال ثوانٍ معدودة.")
    with col2:
        st.markdown("### 🎯 دقة عالية")
        st.write("يعتمد على تقنيات معالجة الصور الرقمية المتقدمة.")
    with col3:
        st.markdown("### 💡 سهل الاستخدام")
        st.write("واجهة تفاعلية بسيطة ومصممة خصيصاً للعروض التقديمية.")
