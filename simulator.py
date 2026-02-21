import random

def generate_emotion_data():
    return {
        "fear": random.randint(10, 95),
        "stress": random.randint(20, 90),
        "panic": random.randint(5, 85)
    }

def generate_health_data():
    return {
        "heart_rate": random.randint(60, 140),
        "temperature": round(random.uniform(36.0, 39.5), 1),
        "motion": random.choice(["Normal", "Low", "Abnormal"])
    }
