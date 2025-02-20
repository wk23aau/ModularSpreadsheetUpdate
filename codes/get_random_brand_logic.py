import random # Import random here as it's used in this module

def get_random_brand():
    brands = [
        "Nexora", "Bravora", "Veltrix", "Zenovia", "Stratosync", "Lumosia",
        "Aetheron", "Novatrax", "Veridyn", "Omnexis", "Quentis", "Evolvex",
        "Zyphoria", "Synergex", "Vortexis", "Aquilora", "Fluxora", "Hypernova",
        "Cognitron", "Elevonix"
    ]
    return random.choice(brands)