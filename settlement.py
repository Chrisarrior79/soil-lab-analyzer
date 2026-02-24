import math

def calculate_primary_consolidation(H, Cc, e0, sigma0, delta_sigma):
    """
    Calculates primary consolidation settlement using Terzaghi theory
    for normally consolidated soils.
    """

    if sigma0 <= 0 or (sigma0 + delta_sigma) <= 0:
        return None

    settlement = (Cc / (1 + e0)) * H * math.log10((sigma0 + delta_sigma) / sigma0)

    return round(settlement, 6)