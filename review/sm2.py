def calculate_sm2(
    ease_factor: float,
    interval: int,
    quality: int,
    max_interval: int = 365
) -> tuple[float, int]:

    if quality not in range(6):
        raise ValueError("quality deve estar entre 0 e 5")

    if quality < 3:
        interval = 1
        ease_factor = max(1.3, ease_factor - 0.2)
    else:
        interval = 6 if interval == 1 else round(interval * ease_factor)
        difficulty = 5 - quality
        adjustment = 0.1 - difficulty * (0.08 + difficulty * 0.02)
        ease_factor = max(1.3, ease_factor + adjustment)

    interval = min(interval, max_interval)

    return ease_factor, interval