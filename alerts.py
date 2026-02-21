def emergency_decision(risk_level):

    if risk_level == "LOW":
        return "Normal Monitoring"

    elif risk_level == "MEDIUM":
        return "Warning Issued"

    else:
        return "🚨 Emergency Triggered → Ambulance Notified"
