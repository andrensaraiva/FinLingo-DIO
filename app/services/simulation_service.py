"""
FinLingo — Simulation Service Module
Financial calculation logic for all simulators.
"""

import math


def calculate_installment(price: float, monthly_rate: float, num_installments: int) -> dict:
    """
    Calculate installment payment details.

    Args:
        price: Item price in dollars.
        monthly_rate: Monthly interest rate as a decimal (e.g., 0.015 for 1.5%).
        num_installments: Number of monthly installments.

    Returns:
        Dict with monthly_payment, total_paid, total_interest, interest_percentage.
    """
    if monthly_rate == 0:
        monthly_payment = price / num_installments
        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_paid": round(price, 2),
            "total_interest": 0.0,
            "interest_percentage": 0.0
        }

    # Standard amortization formula: M = P * [r(1+r)^n] / [(1+r)^n - 1]
    r = monthly_rate
    n = num_installments
    monthly_payment = price * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    total_paid = monthly_payment * n
    total_interest = total_paid - price

    return {
        "monthly_payment": round(monthly_payment, 2),
        "total_paid": round(total_paid, 2),
        "total_interest": round(total_interest, 2),
        "interest_percentage": round((total_interest / price) * 100, 2)
    }


def calculate_loan(principal: float, annual_rate: float, term_months: int) -> dict:
    """
    Calculate loan repayment details.

    Args:
        principal: Loan amount in dollars.
        annual_rate: Annual interest rate as a decimal (e.g., 0.08 for 8%).
        term_months: Loan term in months.

    Returns:
        Dict with monthly_payment, total_repaid, total_interest, effective_annual_rate.
    """
    monthly_rate = annual_rate / 12

    if monthly_rate == 0:
        monthly_payment = principal / term_months
        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_repaid": round(principal, 2),
            "total_interest": 0.0,
            "effective_annual_rate": 0.0
        }

    r = monthly_rate
    n = term_months
    monthly_payment = principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    total_repaid = monthly_payment * n
    total_interest = total_repaid - principal
    effective_annual_rate = ((1 + monthly_rate) ** 12 - 1) * 100

    return {
        "monthly_payment": round(monthly_payment, 2),
        "total_repaid": round(total_repaid, 2),
        "total_interest": round(total_interest, 2),
        "effective_annual_rate": round(effective_annual_rate, 2)
    }


def calculate_loan_comparison(principal: float, annual_rate: float, terms: list) -> list:
    """
    Compare loan costs across different terms.

    Args:
        principal: Loan amount.
        annual_rate: Annual interest rate as decimal.
        terms: List of term lengths in months.

    Returns:
        List of dicts with term, monthly_payment, total_interest.
    """
    results = []
    for term in terms:
        calc = calculate_loan(principal, annual_rate, term)
        results.append({
            "term_months": term,
            "monthly_payment": calc["monthly_payment"],
            "total_interest": calc["total_interest"]
        })
    return results


def calculate_savings_goal(goal: float, monthly_contribution: float, annual_rate: float) -> dict:
    """
    Calculate how long to reach a savings goal with monthly contributions.

    Args:
        goal: Target savings amount.
        monthly_contribution: Monthly deposit amount.
        annual_rate: Annual interest rate as decimal (e.g., 0.04 for 4%).

    Returns:
        Dict with months_to_goal, total_contributed, interest_earned, interest_percentage.
    """
    monthly_rate = annual_rate / 12

    if monthly_rate == 0:
        months = math.ceil(goal / monthly_contribution)
        return {
            "months_to_goal": months,
            "total_contributed": round(monthly_contribution * months, 2),
            "interest_earned": 0.0,
            "interest_percentage": 0.0
        }

    # Future value of annuity formula: FV = PMT * [((1+r)^n - 1) / r]
    # Solve for n: n = log(1 + goal * r / PMT) / log(1 + r)
    r = monthly_rate
    pmt = monthly_contribution

    months = math.ceil(math.log(1 + goal * r / pmt) / math.log(1 + r))
    total_contributed = pmt * months

    # Calculate actual total with interest
    total_with_interest = pmt * ((1 + r) ** months - 1) / r
    interest_earned = total_with_interest - total_contributed

    return {
        "months_to_goal": months,
        "total_contributed": round(total_contributed, 2),
        "interest_earned": round(interest_earned, 2),
        "interest_percentage": round((interest_earned / goal) * 100, 2)
    }


def calculate_savings_monthly(goal: float, target_months: int, annual_rate: float) -> dict:
    """
    Calculate required monthly contribution to reach a goal by a target date.

    Args:
        goal: Target savings amount.
        target_months: Number of months to reach the goal.
        annual_rate: Annual interest rate as decimal.

    Returns:
        Dict with monthly_contribution, total_contributed, interest_earned.
    """
    monthly_rate = annual_rate / 12

    if monthly_rate == 0:
        monthly_contribution = goal / target_months
        return {
            "monthly_contribution": round(monthly_contribution, 2),
            "total_contributed": round(goal, 2),
            "interest_earned": 0.0
        }

    # PMT = FV * r / ((1+r)^n - 1)
    r = monthly_rate
    n = target_months
    monthly_contribution = goal * r / ((1 + r) ** n - 1)
    total_contributed = monthly_contribution * n
    interest_earned = goal - total_contributed

    return {
        "monthly_contribution": round(monthly_contribution, 2),
        "total_contributed": round(total_contributed, 2),
        "interest_earned": round(max(interest_earned, 0), 2)
    }


def calculate_emergency_fund(monthly_expenses: float, months_coverage: int,
                              current_savings: float, monthly_saving: float) -> dict:
    """
    Plan an emergency fund.

    Args:
        monthly_expenses: Monthly essential expenses.
        months_coverage: Desired months of coverage (3-12).
        current_savings: Current amount saved.
        monthly_saving: Amount that can be saved monthly.

    Returns:
        Dict with target, amount_needed, months_to_reach, percentage_complete.
    """
    target = monthly_expenses * months_coverage
    amount_needed = max(target - current_savings, 0)

    if monthly_saving > 0 and amount_needed > 0:
        months_to_reach = math.ceil(amount_needed / monthly_saving)
    elif amount_needed <= 0:
        months_to_reach = 0
    else:
        months_to_reach = float('inf')

    percentage_complete = min(round((current_savings / target) * 100, 1), 100) if target > 0 else 0

    return {
        "target": round(target, 2),
        "amount_needed": round(amount_needed, 2),
        "months_to_reach": months_to_reach,
        "percentage_complete": percentage_complete,
        "one_month_milestone": round(monthly_expenses, 2),
        "three_month_milestone": round(monthly_expenses * 3, 2)
    }


def compare_purchase(price: float, installment_rate: float, num_installments: int,
                      monthly_saving: float, savings_rate: float) -> dict:
    """
    Compare buying now (installments) vs. saving and buying later.

    Args:
        price: Item price.
        installment_rate: Monthly interest rate for installments (decimal).
        num_installments: Number of installments.
        monthly_saving: How much user can save monthly toward this purchase.
        savings_rate: Annual savings account rate (decimal).

    Returns:
        Dict with buy_now and save_first scenarios, plus the difference.
    """
    # Buy now with installments
    installment_result = calculate_installment(price, installment_rate, num_installments)

    # Save and buy later
    monthly_savings_rate = savings_rate / 12
    if monthly_savings_rate > 0 and monthly_saving > 0:
        months_to_save = math.ceil(
            math.log(1 + price * monthly_savings_rate / monthly_saving) /
            math.log(1 + monthly_savings_rate)
        )
        total_saved = monthly_saving * ((1 + monthly_savings_rate) ** months_to_save - 1) / monthly_savings_rate
        interest_earned = total_saved - (monthly_saving * months_to_save)
    elif monthly_saving > 0:
        months_to_save = math.ceil(price / monthly_saving)
        interest_earned = 0
    else:
        months_to_save = float('inf')
        interest_earned = 0

    savings_total_cost = price  # You buy at face value after saving
    difference = installment_result["total_paid"] - savings_total_cost

    return {
        "buy_now": {
            "total_cost": installment_result["total_paid"],
            "monthly_payment": installment_result["monthly_payment"],
            "time_months": num_installments,
            "interest_paid": installment_result["total_interest"]
        },
        "save_first": {
            "total_cost": round(savings_total_cost, 2),
            "monthly_saving": round(monthly_saving, 2),
            "time_months": months_to_save,
            "interest_earned": round(max(interest_earned, 0), 2)
        },
        "you_save": round(difference, 2),
        "time_difference": months_to_save - num_installments
    }
