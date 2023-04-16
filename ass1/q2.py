def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"
print(predict_paid_or_unpaid(3.5))
print(predict_paid_or_unpaid(0.7))
print(predict_paid_or_unpaid(9))

