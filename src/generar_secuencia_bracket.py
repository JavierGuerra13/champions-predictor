"""
GENERADOR DE SECUENCIA DE BRACKET
Crea 4 PNGs progresivos para animación en video

Salida:
- bracket_1_octavos.html
- bracket_2_cuartos.html  
- bracket_3_semis.html
- bracket_4_final.html
"""

import plotly.graph_objects as go

# ============================================
# DATOS DEL TORNEO (usa los de tu simulación)
# ============================================

resultados_simulacion = {
    'octavos_a': [
        ('Paris Saint-Germain', 'Chelsea', 'Chelsea'),
        ('Liverpool', 'Galatasaray', 'Liverpool'),
        ('Bayern Munich', 'Atalanta', 'Bayern Munich'),
        ('Real Madrid', 'Manchester City', 'Real Madrid')
    ],
    'octavos_b': [
        ('Sporting Lisboa', 'Bodø/Glimt', 'Sporting Lisboa'),
        ('Arsenal', 'Bayer Leverkusen', 'Arsenal'),
        ('Barcelona', 'Newcastle United', 'Newcastle United'),
        ('Tottenham Hotspur', 'Atlético Madrid', 'Atlético Madrid')
    ],
    'cuartos_a': [
        ('Chelsea', 'Liverpool', 'Liverpool'),
        ('Bayern Munich', 'Real Madrid', 'Bayern Munich')
    ],
    'cuartos_b': [
        ('Sporting Lisboa', 'Arsenal', 'Arsenal'),
        ('Newcastle United', 'Atlético Madrid', 'Atlético Madrid')
    ],
    'semi_a': ('Liverpool', 'Bayern Munich', 'Bayern Munich'),
    'semi_b': ('Arsenal', 'Atlético Madrid', 'Arsenal'),
    'final': ('Bayern Munich', 'Arsenal', 'Arsenal')
}

# Diccionario de nombres cortos
nombres_cortos = {
    'Paris Saint-Germain': 'PSG',
    'Manchester City': 'Man City',
    'Bayern Munich': 'Bayern',
    'Real Madrid': 'R. Madrid',
    'Sporting Lisboa': 'Sporting',
    'Bayer Leverkusen': 'Leverkusen',
    'Newcastle United': 'Newcastle',
    'Tottenham Hotspur': 'Tottenham',
    'Atlético Madrid': 'Atlético',
    'Bodø/Glimt': 'Bodø'
}

# ============================================
# FUNCIONES HELPER (iguales que antes)
# ============================================

def agregar_equipo(fig, x, y, equipo, es_ganador=False, color_fondo='#2c3e50'):
    """Agrega un equipo al bracket"""
    equipo_display = nombres_cortos.get(equipo, equipo)
    
    if es_ganador:
        color_texto = '#2ecc71'
        peso = 'bold'
        borde = 3
    else:
        color_texto = '#95a5a6'
        peso = 'normal'
        borde = 1
    
    fig.add_shape(
        type="rect",
        x0=x-0.25, y0=y-0.25,
        x1=x+0.25, y1=y+0.25,
        fillcolor=color_fondo,
        line=dict(color=color_texto, width=borde),
        opacity=0.9
    )
    
    fig.add_annotation(
        x=x, y=y,
        text=f"<b>{equipo_display}</b>" if es_ganador else equipo_display,
        showarrow=False,
        font=dict(size=9, color=color_texto, family='Arial'),
        xanchor='center',
        yanchor='middle'
    )

def agregar_linea(fig, x1, y1, x2, y2, color='#34495e'):
    """Conecta dos equipos"""
    fig.add_shape(
        type="line",
        x0=x1, y0=y1,
        x1=x2, y1=y2,
        line=dict(color=color, width=2, dash='dot')
    )

def crear_base_layout():
    """Crea el layout base para todos los brackets"""
    fig = go.Figure()
    
    # Labels de rondas
    fig.add_annotation(x=0, y=15.5, text="<b>OCTAVOS</b>", showarrow=False, 
                      font=dict(size=14, color='white'))
    fig.add_annotation(x=1, y=15.5, text="<b>CUARTOS</b>", showarrow=False,
                      font=dict(size=14, color='white'))
    fig.add_annotation(x=2, y=15.5, text="<b>SEMIS</b>", showarrow=False,
                      font=dict(size=14, color='white'))
    fig.add_annotation(x=3.5, y=15.5, text="<b>FINAL</b>", showarrow=False,
                      font=dict(size=14, color='white'))
    
    # Separador
    fig.add_shape(
        type="line",
        x0=-0.5, y0=7.2,
        x1=3.5, y1=7.2,
        line=dict(color='rgba(255,255,255,0.2)', width=2, dash='dash')
    )
    
    # LADO A / LADO B
    fig.add_annotation(x=-0.6, y=11, text="LADO A", showarrow=False,
                      font=dict(size=12, color='#e74c3c'))
    fig.add_annotation(x=-0.6, y=3, text="LADO B", showarrow=False,
                      font=dict(size=12, color='#3498db'))
    
    return fig

# ============================================
# VERSIÓN 1: SOLO OCTAVOS
# ============================================

print("🎬 Generando Versión 1: Solo Octavos...")

fig1 = crear_base_layout()

# OCTAVOS A
y_oct_a = [14, 12, 10, 8]
for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['octavos_a']):
    y = y_oct_a[i]
    agregar_equipo(fig1, 0, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig1, 0, y-0.5, eq2, eq2==ganador)

# OCTAVOS B
y_oct_b = [6, 4, 2, 0]
for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['octavos_b']):
    y = y_oct_b[i]
    agregar_equipo(fig1, 0, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig1, 0, y-0.5, eq2, eq2==ganador)

fig1.update_layout(
    title='🏆 Champions League 2025-26 - Octavos de Final',
    xaxis=dict(range=[-0.7, 4.8], showgrid=False, showticklabels=False, zeroline=False),
    yaxis=dict(range=[-1, 16], showgrid=False, showticklabels=False, zeroline=False),
    plot_bgcolor='#0a0e27',
    paper_bgcolor='#0a0e27',
    height=900,
    width=1400,
    showlegend=False,
    font=dict(color='white')
)

fig1.write_html('../visualizations/bracket_1_octavos.html')
print("✅ Guardado: bracket_1_octavos.html")

# ============================================
# VERSIÓN 2: HASTA CUARTOS
# ============================================

print("🎬 Generando Versión 2: Hasta Cuartos...")

fig2 = crear_base_layout()

# OCTAVOS (igual que antes)
for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['octavos_a']):
    y = y_oct_a[i]
    agregar_equipo(fig2, 0, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig2, 0, y-0.5, eq2, eq2==ganador)

for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['octavos_b']):
    y = y_oct_b[i]
    agregar_equipo(fig2, 0, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig2, 0, y-0.5, eq2, eq2==ganador)

# CUARTOS A
y_cua_a = [13, 9]
for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['cuartos_a']):
    y = y_cua_a[i]
    agregar_equipo(fig2, 1, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig2, 1, y-0.5, eq2, eq2==ganador)
    agregar_linea(fig2, 0.25, y_oct_a[i*2]+0.5, 0.75, y+0.5)
    agregar_linea(fig2, 0.25, y_oct_a[i*2]-0.5, 0.75, y-0.5)

# CUARTOS B
y_cua_b = [5, 1]
for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['cuartos_b']):
    y = y_cua_b[i]
    agregar_equipo(fig2, 1, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig2, 1, y-0.5, eq2, eq2==ganador)
    agregar_linea(fig2, 0.25, y_oct_b[i*2]+0.5, 0.75, y+0.5)
    agregar_linea(fig2, 0.25, y_oct_b[i*2]-0.5, 0.75, y-0.5)

fig2.update_layout(
    title='🏆 Champions League 2025-26 - Cuartos de Final',
    xaxis=dict(range=[-0.7, 4.8], showgrid=False, showticklabels=False, zeroline=False),
    yaxis=dict(range=[-1, 16], showgrid=False, showticklabels=False, zeroline=False),
    plot_bgcolor='#0a0e27',
    paper_bgcolor='#0a0e27',
    height=900,
    width=1400,
    showlegend=False,
    font=dict(color='white')
)

fig2.write_html('../visualizations/bracket_2_cuartos.html')
print("✅ Guardado: bracket_2_cuartos.html")

# ============================================
# VERSIÓN 3: HASTA SEMIS
# ============================================

print("🎬 Generando Versión 3: Hasta Semis...")

fig3 = crear_base_layout()

# Copiar todo de versión 2
for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['octavos_a']):
    y = y_oct_a[i]
    agregar_equipo(fig3, 0, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig3, 0, y-0.5, eq2, eq2==ganador)

for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['octavos_b']):
    y = y_oct_b[i]
    agregar_equipo(fig3, 0, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig3, 0, y-0.5, eq2, eq2==ganador)

for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['cuartos_a']):
    y = y_cua_a[i]
    agregar_equipo(fig3, 1, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig3, 1, y-0.5, eq2, eq2==ganador)
    agregar_linea(fig3, 0.25, y_oct_a[i*2]+0.5, 0.75, y+0.5)
    agregar_linea(fig3, 0.25, y_oct_a[i*2]-0.5, 0.75, y-0.5)

for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['cuartos_b']):
    y = y_cua_b[i]
    agregar_equipo(fig3, 1, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig3, 1, y-0.5, eq2, eq2==ganador)
    agregar_linea(fig3, 0.25, y_oct_b[i*2]+0.5, 0.75, y+0.5)
    agregar_linea(fig3, 0.25, y_oct_b[i*2]-0.5, 0.75, y-0.5)

# SEMIS A
eq1_a, eq2_a, ganador_a = resultados_simulacion['semi_a']
agregar_equipo(fig3, 2, 11.5, eq1_a, eq1_a==ganador_a)
agregar_equipo(fig3, 2, 10.5, eq2_a, eq2_a==ganador_a)
agregar_linea(fig3, 1.25, 13.5, 1.75, 11.5)
agregar_linea(fig3, 1.25, 8.5, 1.75, 10.5)

# SEMIS B
eq1_b, eq2_b, ganador_b = resultados_simulacion['semi_b']
agregar_equipo(fig3, 2, 3.5, eq1_b, eq1_b==ganador_b)
agregar_equipo(fig3, 2, 2.5, eq2_b, eq2_b==ganador_b)
agregar_linea(fig3, 1.25, 5.5, 1.75, 3.5)
agregar_linea(fig3, 1.25, 0.5, 1.75, 2.5)

fig3.update_layout(
    title='🏆 Champions League 2025-26 - Semifinales',
    xaxis=dict(range=[-0.7, 4.8], showgrid=False, showticklabels=False, zeroline=False),
    yaxis=dict(range=[-1, 16], showgrid=False, showticklabels=False, zeroline=False),
    plot_bgcolor='#0a0e27',
    paper_bgcolor='#0a0e27',
    height=900,
    width=1400,
    showlegend=False,
    font=dict(color='white')
)

fig3.write_html('../visualizations/bracket_3_semis.html')
print("✅ Guardado: bracket_3_semis.html")

# ============================================
# VERSIÓN 4: COMPLETO CON FINAL
# ============================================

print("🎬 Generando Versión 4: Final Completa...")

fig4 = crear_base_layout()

# Copiar todo de versión 3
for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['octavos_a']):
    y = y_oct_a[i]
    agregar_equipo(fig4, 0, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig4, 0, y-0.5, eq2, eq2==ganador)

for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['octavos_b']):
    y = y_oct_b[i]
    agregar_equipo(fig4, 0, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig4, 0, y-0.5, eq2, eq2==ganador)

for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['cuartos_a']):
    y = y_cua_a[i]
    agregar_equipo(fig4, 1, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig4, 1, y-0.5, eq2, eq2==ganador)
    agregar_linea(fig4, 0.25, y_oct_a[i*2]+0.5, 0.75, y+0.5)
    agregar_linea(fig4, 0.25, y_oct_a[i*2]-0.5, 0.75, y-0.5)

for i, (eq1, eq2, ganador) in enumerate(resultados_simulacion['cuartos_b']):
    y = y_cua_b[i]
    agregar_equipo(fig4, 1, y+0.5, eq1, eq1==ganador)
    agregar_equipo(fig4, 1, y-0.5, eq2, eq2==ganador)
    agregar_linea(fig4, 0.25, y_oct_b[i*2]+0.5, 0.75, y+0.5)
    agregar_linea(fig4, 0.25, y_oct_b[i*2]-0.5, 0.75, y-0.5)

eq1_a, eq2_a, ganador_a = resultados_simulacion['semi_a']
agregar_equipo(fig4, 2, 11.5, eq1_a, eq1_a==ganador_a)
agregar_equipo(fig4, 2, 10.5, eq2_a, eq2_a==ganador_a)
agregar_linea(fig4, 1.25, 13.5, 1.75, 11.5)
agregar_linea(fig4, 1.25, 8.5, 1.75, 10.5)

eq1_b, eq2_b, ganador_b = resultados_simulacion['semi_b']
agregar_equipo(fig4, 2, 3.5, eq1_b, eq1_b==ganador_b)
agregar_equipo(fig4, 2, 2.5, eq2_b, eq2_b==ganador_b)
agregar_linea(fig4, 1.25, 5.5, 1.75, 3.5)
agregar_linea(fig4, 1.25, 0.5, 1.75, 2.5)

# FINAL
final_a, final_b, campeon = resultados_simulacion['final']
agregar_equipo(fig4, 3, 8, final_a, final_a==campeon, '#1e3a5f')
agregar_equipo(fig4, 3, 6, final_b, final_b==campeon, '#1e3a5f')
agregar_linea(fig4, 2.25, 11, 2.75, 8)
agregar_linea(fig4, 2.25, 3, 2.75, 6)

# CAMPEÓN
fig4.add_shape(
    type="rect",
    x0=3.8, y0=6.3,
    x1=4.7, y1=7.7,
    fillcolor='#FFD700',
    line=dict(color='#FFA500', width=5),
    opacity=1
)

fig4.add_annotation(
    x=4.25, y=7.3,
    text="🏆",
    showarrow=False,
    font=dict(size=35)
)

fig4.add_annotation(
    x=4.25, y=6.7,
    text=f"<b>{campeon}</b>",
    showarrow=False,
    font=dict(size=13, color='#000000', family='Arial Black')
)

agregar_linea(fig4, 3.25, 7, 3.8, 7, '#FFD700')

fig4.update_layout(
    title='🏆 Champions League 2025-26 - CAMPEÓN',
    xaxis=dict(range=[-0.7, 4.8], showgrid=False, showticklabels=False, zeroline=False),
    yaxis=dict(range=[-1, 16], showgrid=False, showticklabels=False, zeroline=False),
    plot_bgcolor='#0a0e27',
    paper_bgcolor='#0a0e27',
    height=900,
    width=1400,
    showlegend=False,
    font=dict(color='white')
)

fig4.write_html('../visualizations/bracket_4_final.html')
print("✅ Guardado: bracket_4_final.html")

# ============================================
# RESUMEN
# ============================================

print("\n" + "="*60)
print("🎉 ¡SECUENCIA COMPLETA GENERADA!")
print("="*60)
print("\n📁 Archivos creados en visualizations/:")
print("   1. bracket_1_octavos.html")
print("   2. bracket_2_cuartos.html")
print("   3. bracket_3_semis.html")
print("   4. bracket_4_final.html")
print("\n🎬 CÓMO USAR EN TU VIDEO:")
print("   1. Abre cada HTML en navegador")
print("   2. Haz screenshot de cada uno")
print("   3. En CapCut: importa las 4 imágenes")
print("   4. Duración: 1.5-2s cada una")
print("   5. Transición: Fade o Slide")
print("\n💡 TIP: El último (bracket_4_final.html) muéstralo más tiempo (3-5s)")
print("="*60)
