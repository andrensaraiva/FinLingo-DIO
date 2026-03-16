"""
FinLingo — Simulators Page
Interactive financial calculators.
"""

import streamlit as st
from app.services.simulation_service import (
    calculate_installment, calculate_loan, calculate_loan_comparison,
    calculate_savings_goal, calculate_emergency_fund, compare_purchase
)
from app.services.user_service import save_user_data, update_user_xp, increment_counter
from app.services.gamification_service import get_xp_for_action
from app.config import MASCOT_NAME
import pandas as pd


def render_simulators():
    """Render the simulators page."""

    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back"):
            st.session_state.current_page = "home"
            st.rerun()
    with col2:
        st.markdown("### 🔢 Financial Simulators")

    st.markdown("Plug in numbers to see how finance works in practice.")
    st.markdown("---")

    # Simulator selection
    simulator = st.selectbox(
        "Choose a simulator:",
        options=[
            "💳 Installment Calculator",
            "🏦 Loan Simulator",
            "🎯 Savings Goal Calculator",
            "🛡️ Emergency Fund Planner",
            "🛒 Purchase Comparison"
        ]
    )

    st.markdown("")

    if "Installment" in simulator:
        _render_installment_calculator()
    elif "Loan" in simulator:
        _render_loan_simulator()
    elif "Savings" in simulator:
        _render_savings_calculator()
    elif "Emergency" in simulator:
        _render_emergency_planner()
    elif "Purchase" in simulator:
        _render_purchase_comparison()

    # Disclaimer
    st.markdown("---")
    st.markdown(
        "<div class='disclaimer'>💡 This simulation is for learning purposes only. "
        "Actual results depend on real-world conditions, fees, and terms.</div>",
        unsafe_allow_html=True
    )


def _award_simulation_xp():
    """Award XP for running a simulation."""
    user = st.session_state.user_data
    xp = get_xp_for_action("simulation")
    user = update_user_xp(user, xp)
    user = increment_counter(user, "total_simulations")
    st.session_state.user_data = user
    save_user_data(user)
    st.toast(f"🔢 Simulation complete! +{xp} XP", icon="✨")


def _render_installment_calculator():
    """Installment payment calculator."""
    st.markdown("#### 💳 Installment Calculator")
    st.markdown("See the true cost of buying in installments.")

    col1, col2, col3 = st.columns(3)
    with col1:
        price = st.number_input("Item Price ($)", min_value=1.0, value=1200.0, step=50.0)
    with col2:
        installments = st.number_input("Number of Installments", min_value=2, max_value=48, value=12)
    with col3:
        rate = st.number_input("Monthly Interest Rate (%)", min_value=0.0, max_value=20.0, value=1.5, step=0.1)

    if st.button("Calculate 📊", type="primary", key="calc_installment"):
        result = calculate_installment(price, rate / 100, installments)
        _award_simulation_xp()

        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Monthly Payment", f"${result['monthly_payment']:,.2f}")
        with col2:
            st.metric("Total Paid", f"${result['total_paid']:,.2f}")
        with col3:
            st.metric("Total Interest", f"${result['total_interest']:,.2f}")
        with col4:
            st.metric("Interest %", f"{result['interest_percentage']}%")

        st.info(
            f"🦊 **{MASCOT_NAME} says:** Splitting into {installments} installments at "
            f"{rate}%/month means you're paying ${result['total_interest']:,.2f} extra — "
            f"that's {result['interest_percentage']}% more than the original price! "
            f"If you can, paying in fewer installments (or upfront) saves real money."
        )


def _render_loan_simulator():
    """Loan repayment simulator."""
    st.markdown("#### 🏦 Loan Simulator")
    st.markdown("Understand the total cost of borrowing.")

    col1, col2, col3 = st.columns(3)
    with col1:
        principal = st.number_input("Loan Amount ($)", min_value=100.0, value=10000.0, step=500.0)
    with col2:
        annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, max_value=50.0, value=8.0, step=0.5)
    with col3:
        term = st.number_input("Loan Term (months)", min_value=6, max_value=360, value=36)

    if st.button("Calculate 📊", type="primary", key="calc_loan"):
        result = calculate_loan(principal, annual_rate / 100, term)
        _award_simulation_xp()

        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Monthly Payment", f"${result['monthly_payment']:,.2f}")
        with col2:
            st.metric("Total Repaid", f"${result['total_repaid']:,.2f}")
        with col3:
            st.metric("Total Interest", f"${result['total_interest']:,.2f}")
        with col4:
            st.metric("Effective Rate", f"{result['effective_annual_rate']}%")

        # Comparison table
        st.markdown("**📊 Term Comparison:**")
        comparison = calculate_loan_comparison(principal, annual_rate / 100, [24, 36, 48, 60])
        df = pd.DataFrame(comparison)
        df.columns = ["Term (months)", "Monthly Payment ($)", "Total Interest ($)"]
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.info(
            f"🦊 **{MASCOT_NAME} says:** A longer term means lower monthly payments but MORE "
            f"total interest. Compare the terms above — time is money, literally!"
        )


def _render_savings_calculator():
    """Savings goal calculator."""
    st.markdown("#### 🎯 Savings Goal Calculator")
    st.markdown("How long until you reach your savings goal?")

    col1, col2, col3 = st.columns(3)
    with col1:
        goal = st.number_input("Savings Goal ($)", min_value=100.0, value=5000.0, step=100.0)
    with col2:
        monthly = st.number_input("Monthly Contribution ($)", min_value=10.0, value=200.0, step=25.0)
    with col3:
        rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, max_value=20.0, value=4.0, step=0.5)

    if st.button("Calculate 📊", type="primary", key="calc_savings"):
        result = calculate_savings_goal(goal, monthly, rate / 100)
        _award_simulation_xp()

        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            years = result["months_to_goal"] // 12
            months = result["months_to_goal"] % 12
            st.metric("Time to Goal", f"{years}y {months}m" if years > 0 else f"{months} months")
        with col2:
            st.metric("Total Contributed", f"${result['total_contributed']:,.2f}")
        with col3:
            st.metric("Interest Earned", f"${result['interest_earned']:,.2f}")

        st.progress(min(1.0, monthly * 12 / goal), text=f"First year progress")

        st.info(
            f"🦊 **{MASCOT_NAME} says:** By saving ${monthly:,.0f}/month with {rate}% annual interest, "
            f"you'd reach your ${goal:,.0f} goal in about {result['months_to_goal']} months "
            f"and earn ${result['interest_earned']:,.2f} in interest! Even small amounts add up. "
            f"The hardest part is starting."
        )


def _render_emergency_planner():
    """Emergency fund planner."""
    st.markdown("#### 🛡️ Emergency Fund Planner")
    st.markdown("Plan your financial safety net.")

    col1, col2 = st.columns(2)
    with col1:
        expenses = st.number_input("Monthly Essential Expenses ($)", min_value=100.0, value=2000.0, step=100.0)
        coverage = st.slider("Months of Coverage", min_value=3, max_value=12, value=6)
    with col2:
        current = st.number_input("Current Savings ($)", min_value=0.0, value=1500.0, step=100.0)
        monthly_save = st.number_input("Monthly Amount You Can Save ($)", min_value=0.0, value=300.0, step=25.0)

    if st.button("Calculate 📊", type="primary", key="calc_emergency"):
        result = calculate_emergency_fund(expenses, coverage, current, monthly_save)
        _award_simulation_xp()

        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Target Fund", f"${result['target']:,.2f}")
        with col2:
            st.metric("Still Needed", f"${result['amount_needed']:,.2f}")
        with col3:
            if result['months_to_reach'] == float('inf'):
                st.metric("Months to Goal", "∞")
            else:
                st.metric("Months to Goal", f"{result['months_to_reach']}")
        with col4:
            st.metric("Progress", f"{result['percentage_complete']}%")

        # Progress bar
        st.progress(result['percentage_complete'] / 100,
                   text=f"${current:,.0f} / ${result['target']:,.0f}")

        st.info(
            f"🦊 **{MASCOT_NAME} says:** Your target is ${result['target']:,.0f} "
            f"({coverage} months of expenses). You're {result['percentage_complete']}% there — "
            f"{'great start!' if result['percentage_complete'] > 0 else 'time to start!'} "
            f"Pro tip: aim for 1 month (${result['one_month_milestone']:,.0f}) as your first milestone."
        )


def _render_purchase_comparison():
    """Purchase comparison: buy now vs. save first."""
    st.markdown("#### 🛒 Purchase Comparison")
    st.markdown("Should you buy now (installments) or save up?")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Buy Now (Installments)**")
        price = st.number_input("Item Price ($)", min_value=50.0, value=800.0, step=50.0)
        inst_rate = st.number_input("Installment Interest Rate (%/month)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)
        num_inst = st.number_input("Number of Installments", min_value=2, max_value=24, value=10)

    with col2:
        st.markdown("**Save First**")
        monthly_save = st.number_input("Monthly Savings ($)", min_value=10.0, value=100.0, step=25.0)
        save_rate = st.number_input("Savings Account Rate (%/year)", min_value=0.0, max_value=15.0, value=4.0, step=0.5)

    if st.button("Compare 📊", type="primary", key="calc_compare"):
        result = compare_purchase(price, inst_rate / 100, num_inst, monthly_save, save_rate / 100)
        _award_simulation_xp()

        st.markdown("---")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**💳 Buy Now**")
            st.metric("Total Cost", f"${result['buy_now']['total_cost']:,.2f}")
            st.metric("Monthly Payment", f"${result['buy_now']['monthly_payment']:,.2f}")
            st.metric("Interest Paid", f"${result['buy_now']['interest_paid']:,.2f}")
            st.metric("Time", f"{result['buy_now']['time_months']} months")

        with col2:
            st.markdown("**🏦 Save First**")
            st.metric("Total Cost", f"${result['save_first']['total_cost']:,.2f}")
            st.metric("Monthly Saving", f"${result['save_first']['monthly_saving']:,.2f}")
            st.metric("Interest Earned", f"+${result['save_first']['interest_earned']:,.2f}")
            st.metric("Time", f"~{result['save_first']['time_months']} months")

        if result['you_save'] > 0:
            st.success(f"💰 By saving first, you would save **${result['you_save']:,.2f}**!")
        else:
            st.info("In this case, both options have similar costs.")

        st.info(
            f"🦊 **{MASCOT_NAME} says:** Buying on installments costs "
            f"${result['buy_now']['interest_paid']:,.2f} in interest. "
            f"Saving up means you'd have enough in ~{result['save_first']['time_months']} months "
            f"and earn interest instead of paying it! The trade-off? You wait longer, "
            f"but save money and avoid debt."
        )
