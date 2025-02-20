CATEGORY_REFERRAL_FEES = { # Define CATEGORY_REFERRAL_FEES here as it's used in this module
    "Electronics": 0.05,
    "Books": 0.07,
    "Clothing": 0.10,
    "Home & Garden": 0.12,
    "Beauty": 0.08,
    "Toys & Games": 0.09,
    "default": 0.15,
}

def calculate_referral_fee(product_category, selling_price):
    referral_fee_rate = CATEGORY_REFERRAL_FEES.get(product_category, CATEGORY_REFERRAL_FEES["default"])
    return selling_price * referral_fee_rate