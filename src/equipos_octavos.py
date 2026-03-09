"""
Equipos y enfrentamientos de Octavos de Final - Champions League 2026
"""

# 16 equipos en octavos
equipos = [
    'Liverpool',
    'Galatasaray',
    'Barcelona',
    'Newcastle',
    'Tottenham',
    'Atlético Madrid',
    'Bayern Munich',
    'Atalanta',
    'Arsenal',
    'Bayer Leverkusen',
    'Chelsea',
    'Paris Saint-Germain',
    'Sporting Lisboa',
    'Bodø/Glimt',
    'Manchester City',
    'Real Madrid'
]

# Enfrentamientos (IDA - 10-11 Marzo)
enfrentamientos = {
    'tie_1': {
        'local': 'Galatasaray',
        'visitante': 'Liverpool',
        'fecha_ida': '2026-03-10',
        'hora_ida': '14:45'
    },
    'tie_2': {
        'local': 'Newcastle',
        'visitante': 'Barcelona',
        'fecha_ida': '2026-03-10',
        'hora_ida': '17:00'
    },
    'tie_3': {
        'local': 'Atlético Madrid',
        'visitante': 'Tottenham',
        'fecha_ida': '2026-03-10',
        'hora_ida': '17:00'
    },
    'tie_4': {
        'local': 'Atalanta',
        'visitante': 'Bayern Munich',
        'fecha_ida': '2026-03-10',
        'hora_ida': '17:00'
    },
    'tie_5': {
        'local': 'Bayer Leverkusen',
        'visitante': 'Arsenal',
        'fecha_ida': '2026-03-11',
        'hora_ida': '14:45'
    },
    'tie_6': {
        'local': 'Paris Saint-Germain',
        'visitante': 'Chelsea',
        'fecha_ida': '2026-03-11',
        'hora_ida': '17:00'
    },
    'tie_7': {
        'local': 'Bodø/Glimt',
        'visitante': 'Sporting Lisboa',
        'fecha_ida': '2026-03-11',
        'hora_ida': '17:00'
    },
    'tie_8': {
        'local': 'Real Madrid',
        'visitante': 'Manchester City',
        'fecha_ida': '2026-03-11',
        'hora_ida': '17:00'
    }
}

# Códigos de equipos (para scraping)
equipos_codes = {
    'Liverpool': 'LIV',
    'Galatasaray': 'GAL',
    'Barcelona': 'BAR',
    'Newcastle': 'NEW',
    'Tottenham': 'TOT',
    'Atlético Madrid': 'ATM',
    'Bayern Munich': 'BAY',
    'Atalanta': 'ATA',
    'Arsenal': 'ARS',
    'Bayer Leverkusen': 'LEV',
    'Chelsea': 'CHE',
    'Paris Saint-Germain': 'PSG',
    'Sporting Lisboa': 'SPO',
    'Bodø/Glimt': 'BOD',
    'Manchester City': 'MCI',
    'Real Madrid': 'RMA'
}

if __name__ == "__main__":
    print("=== OCTAVOS DE FINAL - CHAMPIONS LEAGUE 2026 ===\n")
    
    for tie_name, tie_info in enfrentamientos.items():
        print(f"{tie_info['local']} vs {tie_info['visitante']}")
        print(f"  Fecha IDA: {tie_info['fecha_ida']} - {tie_info['hora_ida']}")
        print()
