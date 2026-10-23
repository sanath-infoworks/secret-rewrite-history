SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/FAKEXXXXXXXXXXXXXXXXXXXX"

def notify(msg):
    print(f"posting to {SLACK_WEBHOOK}: {msg}")
