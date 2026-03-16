"""
Tests for FinLingo Simulation Service.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from app.services.simulation_service import (
    calculate_installment,
    calculate_loan,
    calculate_loan_comparison,
    calculate_savings_goal,
    calculate_savings_monthly,
    calculate_emergency_fund,
    compare_purchase,
)


# ─── Installment Calculator Tests ────────────────────

class TestCalculateInstallment:
    def test_basic_calculation(self):
        """Test standard installment calculation."""
        result = calculate_installment(1200, 0.015, 12)
        assert result["monthly_payment"] > 0
        assert result["total_paid"] > 1200
        assert result["total_interest"] > 0
        assert result["interest_percentage"] > 0

    def test_zero_interest(self):
        """Zero interest means total equals price."""
        result = calculate_installment(1000, 0, 10)
        assert result["monthly_payment"] == 100.0
        assert result["total_paid"] == 1000.0
        assert result["total_interest"] == 0.0
        assert result["interest_percentage"] == 0.0

    def test_higher_rate_costs_more(self):
        """Higher interest rates should cost more."""
        result_low = calculate_installment(1000, 0.01, 12)
        result_high = calculate_installment(1000, 0.05, 12)
        assert result_high["total_paid"] > result_low["total_paid"]

    def test_more_installments_cost_more(self):
        """More installments means more total interest."""
        result_few = calculate_installment(1000, 0.02, 6)
        result_many = calculate_installment(1000, 0.02, 24)
        assert result_many["total_interest"] > result_few["total_interest"]


# ─── Loan Calculator Tests ───────────────────────────

class TestCalculateLoan:
    def test_basic_loan(self):
        """Test standard loan calculation."""
        result = calculate_loan(10000, 0.08, 36)
        assert result["monthly_payment"] > 0
        assert result["total_repaid"] > 10000
        assert result["total_interest"] > 0
        assert result["effective_annual_rate"] > 0

    def test_zero_interest_loan(self):
        """Zero interest loan — total equals principal."""
        result = calculate_loan(12000, 0, 12)
        assert result["monthly_payment"] == 1000.0
        assert result["total_repaid"] == 12000.0
        assert result["total_interest"] == 0.0

    def test_shorter_term_higher_payment(self):
        """Shorter terms should have higher monthly payments but less total interest."""
        result_short = calculate_loan(10000, 0.08, 24)
        result_long = calculate_loan(10000, 0.08, 60)
        assert result_short["monthly_payment"] > result_long["monthly_payment"]
        assert result_short["total_interest"] < result_long["total_interest"]


# ─── Loan Comparison Tests ───────────────────────────

class TestCalculateLoanComparison:
    def test_comparison_returns_correct_count(self):
        """Should return one result per term."""
        result = calculate_loan_comparison(10000, 0.08, [12, 24, 36])
        assert len(result) == 3

    def test_comparison_increasing_interest(self):
        """Longer terms should have more total interest."""
        result = calculate_loan_comparison(10000, 0.08, [12, 24, 36, 48])
        for i in range(len(result) - 1):
            assert result[i]["total_interest"] < result[i + 1]["total_interest"]


# ─── Savings Goal Tests ─────────────────────────────

class TestCalculateSavingsGoal:
    def test_basic_savings(self):
        result = calculate_savings_goal(5000, 200, 0.04)
        assert result["months_to_goal"] > 0
        assert result["total_contributed"] > 0
        assert result["interest_earned"] >= 0

    def test_zero_interest_savings(self):
        result = calculate_savings_goal(1000, 100, 0)
        assert result["months_to_goal"] == 10
        assert result["total_contributed"] == 1000.0
        assert result["interest_earned"] == 0.0

    def test_higher_rate_fewer_months(self):
        """Higher interest should reach goal faster."""
        result_low = calculate_savings_goal(10000, 200, 0.02)
        result_high = calculate_savings_goal(10000, 200, 0.10)
        assert result_high["months_to_goal"] <= result_low["months_to_goal"]


# ─── Savings Monthly Tests ──────────────────────────

class TestCalculateSavingsMonthly:
    def test_basic_monthly(self):
        result = calculate_savings_monthly(5000, 24, 0.04)
        assert result["monthly_contribution"] > 0
        assert result["total_contributed"] > 0

    def test_zero_interest_monthly(self):
        result = calculate_savings_monthly(1200, 12, 0)
        assert result["monthly_contribution"] == 100.0
        assert result["interest_earned"] == 0.0


# ─── Emergency Fund Tests ───────────────────────────

class TestCalculateEmergencyFund:
    def test_basic_emergency_fund(self):
        result = calculate_emergency_fund(2000, 6, 1500, 300)
        assert result["target"] == 12000.0
        assert result["amount_needed"] == 10500.0
        assert result["months_to_reach"] == 35
        assert result["percentage_complete"] == 12.5

    def test_already_funded(self):
        """User already has enough."""
        result = calculate_emergency_fund(1000, 3, 5000, 200)
        assert result["amount_needed"] == 0.0
        assert result["months_to_reach"] == 0
        assert result["percentage_complete"] == 100

    def test_no_savings_capacity(self):
        """User can't save — infinite months."""
        result = calculate_emergency_fund(2000, 6, 0, 0)
        assert result["months_to_reach"] == float('inf')

    def test_milestones(self):
        result = calculate_emergency_fund(2000, 6, 0, 500)
        assert result["one_month_milestone"] == 2000.0
        assert result["three_month_milestone"] == 6000.0


# ─── Purchase Comparison Tests ──────────────────────

class TestComparePurchase:
    def test_basic_comparison(self):
        result = compare_purchase(800, 0.02, 10, 100, 0.04)
        assert result["buy_now"]["total_cost"] > 800
        assert result["save_first"]["total_cost"] == 800.0
        assert result["you_save"] > 0

    def test_buy_now_always_costs_more_with_interest(self):
        """Installments with interest should always cost more than saving."""
        result = compare_purchase(500, 0.03, 6, 100, 0.02)
        assert result["buy_now"]["total_cost"] > result["save_first"]["total_cost"]
