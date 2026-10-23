import stripe

stripe.api_key = "REDACTED"

def charge(amount_cents, token):
    return stripe.Charge.create(amount=amount_cents, currency="usd", source=token)
