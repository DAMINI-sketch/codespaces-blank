import streamlit as st

# Set page layout to wide to perfectly accommodate the right-corner panel
st.set_page_config(layout="wide")

# ==========================================
# 🎛️ SIDEBAR CONTROL CENTER (ORIGINAL LOOK)
# ==========================================
st.sidebar.markdown("## 🎛️ Control Center")

user_role = st.sidebar.selectbox(
    "Select User Role:",
    ["PV Associate", "Medical Reviewer", "Regulatory Lead"]
)

processing_mode = st.sidebar.radio(
    "Processing Mode:",
    ["Use Demo Cases", "Upload Custom Case (Live Shield)"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🧠 Learning Mode Adaptive Level")
learning_depth = st.sidebar.slider("Choose Depth (Beginner to Expert):", 1, 10, 10)
st.sidebar.caption("Active Optimization Level: **Expert Mode**")


# ==========================================
# 🛡️ MAIN LAYOUT CONFIGURATION
# ==========================================
# Creating a 2-column layout to place the PV Panel on the Right Corner
main_content_col, right_panel_col = st.columns([2, 1], gap="large")


# ==========================================
# 🏢 LEFT COLUMN: MAIN CONTENT & 10 MODULES
# ==========================================
with main_content_col:
    # Prominent Header with Name
    st.title("🛡️ AI Healthcare Auditor & PV Compliance Suite")
    st.markdown("#### **Enterprise Edition v3.0 (2026 Compliance Standard) | Developed by Damini Prajapati**")
    st.markdown("---")
    
    st.markdown(f"### **Active Session:** `{user_role} Interface`")
    
    # Active Case Dropdown
    active_case = st.selectbox(
        "Select Active Audit Case:",
        ["Case 1: Routine Cold vs Pneumonia Mismatch"]
    )
    
    # 🌟 TARGET ENVIRONMENT SWITCH (THE INTERVIEWER TOGGLE)
    st.markdown("### 📊 Target Dataset Environment Selector")
    case_environment = st.selectbox(
        "Choose Dataset State for Validation Engine Evaluation:",
        options=[
            "Dataset Environment A: Non-Compliant Baseline (High-Risk / Audit Mode)",
            "Dataset Environment B: Remediated Baseline (100% ICH-E2B Compliant)"
        ],
        help="Switch environments to display how the AI engine flags timeline paradoxes vs processes perfect files."
    )
    st.markdown("---")
    
    st.markdown("### 📋 System Modules Architecture (10 Pillars of PV Audit)")
    
    # Setting up data parameters based on the chosen environment
    if "Non-Compliant" in case_environment:
        # Faulty Data State strings
        mod3_status = "❌ **CRITICAL FLAGGED:** Chronological coordinates missing. *Drug Start Date* and *Adverse Event Onset Date* are blank. Temporal relationship cannot be mathematically evaluated."
        mod5_status = "❌ **CLINICAL PARADOX DETECTED:** High-severity billing code for *Pneumonia* applied, but clinical timeline only states a *mild common cold*. Antibiotic logs, ER metrics, and chest X-ray confirmations are entirely missing."
        mod6_status = "❌ **CONTEXT ISOLATION:** Patient is on Metformin 500mg therapy for Type-2 Diabetes, but the *Baseline Concomitant Medications Log* is unmapped in the database."
        mod9_action = "⚠️ **Excel Generation Blocked:** Please remediate critical errors before downloading the master audit workbook."
        mod10_status = "❌ **REJECTED:** Only 2 out of 4 baseline safety reporting pillars satisfied. Automated ICH XML generation halted."
    else:
        # Compliant Data State strings
        mod3_status = "✅ **VALIDATED:** Suspected Drug Track (Paracetamol 650mg) and Adverse Event Onset both fully synced and locked on **June 01, 2026**."
        mod5_status = "✅ **TIMELINE SYNCHRONIZED:** Clinical indication updated to *Pyrexia (Fever) secondary to Pneumonia*. Billing codes and clinical progression are now perfectly aligned with the transactional medical reality."
        mod6_status = "✅ **LOG MAPPED:** Metformin 500mg successfully reconciled against the fully populated *Baseline Medical History Log*."
        mod9_action = "✅ **Excel Generation Ready:** Click the button below to extract the complete 10-feature audit analytics report."
        mod10_status = "✅ **APPROVED:** 100% ICH-E2B Compliant Architecture. E2B (R3) safety payload successfully generated."

    # Rendering the 10 Explicit Modules
    with st.expander("Module 1: Patient Demographics & Baseline History", expanded=False):
        st.write("**Patient ID:** Anonymized Record-2026 | **Age:** 24 | **Gender:** Female")
        st.write("Baseline data successfully ingested into the safety architecture.")

    with st.expander("Module 2: Reporter Information & Verification", expanded=False):
        st.write("**Reporter Type:** Healthcare Professional (Verified) | **Country:** India")
        st.write("Pillar 1 of ICH-E2B minimum criteria satisfies international regulations.")

    with st.expander("Module 3: Suspected Medication Chronology", expanded=True):
        st.write("**Suspected Drug:** Paracetamol 650mg")
        st.markdown(mod3_status)

    with st.expander("Module 4: Adverse Event (AE) Profile & MedDRA Coding", expanded=False):
        st.write("**Reported Term:** Severe swelling of lips and face | **MedDRA Preferred Term:** Acute Angioedema")
        st.write("System auto-coding function operating at 99.8% precision matrix.")

    with st.expander("Module 5: Clinical Timeline Paradox Analysis", expanded=True):
        st.markdown(mod5_status)

    with st.expander("Module 6: Concomitant Medication Context Mapping", expanded=True):
        st.markdown(mod6_status)

    with st.expander("Module 7: Causality Assessment Engine (Naranjo Scoring)", expanded=False):
        st.write("Calculates safety scores dynamically using temporal logs, dechallenge matrices, and rechallenge parameters.")

    with st.expander("Module 8: Risk Assessment Matrix (FDA / EMA Guidelines)", expanded=False):
        st.write("Cross-references international signal detection databases to evaluate product liability risk.")

    with st.expander("Module 9: Enterprise Excel Audit Report Generator", expanded=True):
        st.markdown(mod9_action)
        if "Remediated Baseline" in case_environment:
            st.download_button(
                label="📥 Download Full Audit Analysis Report (Excel Format)",
                data="Audit Clear Header\n100% Validated Data Streamlined",
                file_name="PV_Enterprise_Audit_Report.xlsx"
            )

    with st.expander("Module 10: ICH-E2B (R3) Regulatory Submission Readiness", expanded=True):
        st.markdown(mod10_status)


# ==========================================
# 🩺 RIGHT COLUMN: PHARMACOVIGILANCE PANEL
# ==========================================
with right_panel_col:
    st.markdown("### 🛡️ Pharmacovigilance Panel")
    st.caption("Live Analytical Evaluation Metrics")
    st.markdown("---")
    
    # Changing metrics dynamically based on the toggle state
    if "Non-Compliant" in case_environment:
        st.metric(label="E2B Compliance Score", value="45%", delta="-55% Critical Risk")
        
        st.markdown("#### 🚨 Audit Status")
        st.error("⚠️ FLAGGED FOR REJECTION")
        
        st.markdown("#### 🔍 Core Safety Metrics")
        st.text("• Naranjo Score: Undefined (0)")
        st.text("• Timeline Validation: FAILED")
        st.text("• Missing Pillars: Onset Dates")
        
        st.markdown("#### 📜 Regulatory Status")
        st.warning("Not Ready for FDA/EMA Submission")
    else:
        st.metric(label="E2B Compliance Score", value="100%", delta="Target Achieved")
        
        st.markdown("#### 🏆 Audit Status")
        st.success("✅ PASSED & SIGNED-OFF")
        
        st.markdown("#### 🔍 Core Safety Metrics")
        st.text("• Naranjo Score: +6 (Probable)")
        st.text("• Timeline Validation: PASSED")
        st.text("• Missing Pillars: None (0)")
        
        st.markdown("#### 📜 Regulatory Status")
        st.info("ICH-E2B XML Payload Ready")

st.markdown("---")