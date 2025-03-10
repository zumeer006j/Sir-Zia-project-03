import re
import streamlit as st  
st.set_page_config(page_title="Password strength checker by SYED ZUMEER IMAM ",page_icon="🎉",layout="centered")
st.markdown("""
<style>
       .main{text-align:center;}
       .stTextInput{width:60% !important;margin:auto;}
       .stButton button {width: 50%; background-color #4CAF50; color: white; font-size: 18px;}
       .stButton button:hover {background-color: #45a049;}
            </style>            
""",unsafe_allow_html=True
)
st.title("Password Strength Generator")
st.title("Enter your password below to check its security level.🔍")

def check_password_strength(password):
    score=0
    feedback=[]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **atleast 8 character long**")

        if re.search(r"[A-Z]",password ) and re.search(r"[a-z]",password):
            score += 1
        else:
            feedback.append("❌ password should include **atleast ane number (0-9)**.")  
        if re.search(r"[!@#$%^&]",password):
            score +=1
        else:
            feedback.append("❌ Tinclude **atleast one special character (!@#$%^&*)**.")  

        if score == 4:
            st.success("✅ **Strong Password** your password is secure.")
        elif score == 3:
            st.info("⚠️ **Moderate pasword** - Consider improving security by adding more features")
        else:
            st.error("❌ **Week Password** - Follow thesuggestion below tostrength it.")

        if feedback:
            with st.expander("🔍 **Improve Your Password** "):
                for item in feedback:
                    st.write(item)
        password = st.text_input("Enter your password:",type="password",help="Ensure your password is strong 🔒")

        if st.button("Check strength"):
            if password:
                check_password_strength(password)
            else:
                st.warning("⚠️ Please enter a password first!")              