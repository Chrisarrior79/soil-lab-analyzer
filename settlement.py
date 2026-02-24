import math

def calculate_primary_consolidation(H, Cc, e0, sigma0, delta_sigma):
    """
    Calculates primary consolidation settlement using Terzaghi theory
    for normally consolidated soils.

    Returns:
        settlement_m (float)
        settlement_mm (float)
    """

    if sigma0 <= 0 or (sigma0 + delta_sigma) <= 0:
        return None, None

    settlement_m = (Cc / (1 + e0)) * H * math.log10((sigma0 + delta_sigma) / sigma0)

    settlement_m = round(settlement_m, 6)
    settlement_mm = round(settlement_m * 1000, 2)

    return settlement_m, settlement_mm