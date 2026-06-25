# Success, Info, Warning, Error, Exception


# import module
import streamlit as st

# success
st.success("success")

# success
st.info("information")

# success
st.warning("waring")

# success
st.error("error")

# exception - this has been added later
exp = ZeroDivisionError("trying to divide by zero")
st.exception(exp)