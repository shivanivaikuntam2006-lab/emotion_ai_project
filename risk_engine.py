def calculate_risk(emotion, health):
    score = 0

    score += emotion["fear"] * 0.3
    score += emotion["stress"] * 0.3
    score += emotion["panic"] * 0.4

    if health["heart_rate"] > 110:
        score += 20

    if health["temperature"] > 38:
        score += 20

    if score < 50:
        return "LOW"
    elif score < 100:
        return "MEDIUM"
    else:
        return "CRITICAL"
