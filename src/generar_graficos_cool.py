"""
Gráfico de Probabilidades de Campeón - VERSIÓN MEJORADA
Más cool, más profesional, mejores colores
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Cargar datos
df_prob = pd.read_csv('../data/processed/probabilidades_campeon.csv')

# Top 10 para no saturar
top_10 = df_prob.head(10).copy()

# ============================================
# OPCIÓN 1: Gradiente Viridis (Profesional)
# ============================================

fig1 = go.Figure()

# Color gradiente basado en probabilidad
colors_viridis = px.colors.sample_colorscale(
    'Viridis', 
    [i/(len(top_10)-1) for i in range(len(top_10))]
)

fig1.add_trace(go.Bar(
    y=top_10['Equipo'][::-1],
    x=top_10['Prob_Campeon'][::-1],
    orientation='h',
    marker=dict(
        color=top_10['Prob_Campeon'][::-1],
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(
            title="Prob %",
            thickness=15,
            len=0.7
        ),
        line=dict(color='rgba(255,255,255,0.3)', width=1)
    ),
    text=top_10['Prob_Campeon'][::-1].round(1),
    texttemplate='%{text}%',
    textposition='outside',
    textfont=dict(size=14, color='white', family='Arial Black'),
    hovertemplate='<b>%{y}</b><br>Probabilidad: %{x:.1f}%<extra></extra>'
))

fig1.update_layout(
    title={
        'text': '🏆 Probabilidades de ser CAMPEÓN<br><sub>Champions League 2025-26 • 10,000 simulaciones Monte Carlo</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 24, 'color': 'white', 'family': 'Arial Black'}
    },
    xaxis_title='Probabilidad (%)',
    yaxis_title='',
    plot_bgcolor='#0a0e27',
    paper_bgcolor='#0a0e27',
    font=dict(size=13, color='white', family='Arial'),
    height=600,
    showlegend=False,
    xaxis=dict(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='rgba(255,255,255,0.1)',
        range=[0, top_10['Prob_Campeon'].max() + 5]
    ),
    yaxis=dict(
        showgrid=False
    )
)

fig1.show()
fig1.write_html('../visualizations/probabilidades_v1_viridis.html')
print("✅ Versión 1 guardada: viridis theme")

# ============================================
# OPCIÓN 2: Sunset (Naranja/Rojo/Morado)
# ============================================

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    y=top_10['Equipo'][::-1],
    x=top_10['Prob_Campeon'][::-1],
    orientation='h',
    marker=dict(
        color=top_10['Prob_Campeon'][::-1],
        colorscale='Sunset',
        showscale=True,
        colorbar=dict(
            title="Prob %",
            thickness=15,
            len=0.7
        ),
        line=dict(color='rgba(255,255,255,0.5)', width=2)
    ),
    text=top_10['Prob_Campeon'][::-1].round(1),
    texttemplate='<b>%{text}%</b>',
    textposition='outside',
    textfont=dict(size=14, color='white', family='Arial Black'),
    hovertemplate='<b>%{y}</b><br>Probabilidad: %{x:.1f}%<extra></extra>'
))

fig2.update_layout(
    title={
        'text': '🏆 Probabilidades de ser CAMPEÓN<br><sub>Champions League 2025-26 • 10,000 simulaciones Monte Carlo</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 24, 'color': 'white', 'family': 'Arial Black'}
    },
    xaxis_title='Probabilidad (%)',
    yaxis_title='',
    plot_bgcolor='#1a1625',
    paper_bgcolor='#1a1625',
    font=dict(size=13, color='white', family='Arial'),
    height=600,
    showlegend=False,
    xaxis=dict(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='rgba(255,255,255,0.1)',
        range=[0, top_10['Prob_Campeon'].max() + 5]
    )
)

fig2.show()
fig2.write_html('../visualizations/probabilidades_v2_sunset.html')
print("✅ Versión 2 guardada: sunset theme")

# ============================================
# OPCIÓN 3: Turbo (Multicolor vibrante)
# ============================================

fig3 = go.Figure()

fig3.add_trace(go.Bar(
    y=top_10['Equipo'][::-1],
    x=top_10['Prob_Campeon'][::-1],
    orientation='h',
    marker=dict(
        color=top_10['Prob_Campeon'][::-1],
        colorscale='Turbo',
        showscale=True,
        colorbar=dict(
            title="Prob %",
            thickness=15,
            len=0.7
        ),
        line=dict(color='white', width=2)
    ),
    text=top_10['Prob_Campeon'][::-1].round(1),
    texttemplate='<b>%{text}%</b>',
    textposition='outside',
    textfont=dict(size=15, color='white', family='Arial Black'),
    hovertemplate='<b>%{y}</b><br>Probabilidad: %{x:.1f}%<extra></extra>'
))

fig3.update_layout(
    title={
        'text': '🏆 Probabilidades de ser CAMPEÓN<br><sub>Champions League 2025-26 • 10,000 simulaciones Monte Carlo</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 24, 'color': 'white', 'family': 'Arial Black'}
    },
    xaxis_title='Probabilidad (%)',
    yaxis_title='',
    plot_bgcolor='#0f0f23',
    paper_bgcolor='#0f0f23',
    font=dict(size=13, color='white', family='Arial'),
    height=600,
    showlegend=False,
    xaxis=dict(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='rgba(255,255,255,0.15)',
        range=[0, top_10['Prob_Campeon'].max() + 5]
    )
)

fig3.show()
fig3.write_html('../visualizations/probabilidades_v3_turbo.html')
print("✅ Versión 3 guardada: turbo theme")

# ============================================
# OPCIÓN 4: Colores por Tier (Categorías)
# ============================================

fig4 = go.Figure()

# Definir colores por tier
def get_tier_color(prob):
    if prob >= 20:
        return '#FFD700'  # Oro - Favoritos
    elif prob >= 15:
        return '#FF6B35'  # Naranja - Contendientes
    elif prob >= 10:
        return '#4ECDC4'  # Cyan - Outsiders
    elif prob >= 5:
        return '#9B59B6'  # Morado - Dark horses
    else:
        return '#95A5A6'  # Gris - Underdogs

colors_tier = [get_tier_color(p) for p in top_10['Prob_Campeon'][::-1]]

fig4.add_trace(go.Bar(
    y=top_10['Equipo'][::-1],
    x=top_10['Prob_Campeon'][::-1],
    orientation='h',
    marker=dict(
        color=colors_tier,
        line=dict(color='white', width=2)
    ),
    text=top_10['Prob_Campeon'][::-1].round(1),
    texttemplate='<b>%{text}%</b>',
    textposition='outside',
    textfont=dict(size=15, color='white', family='Arial Black'),
    hovertemplate='<b>%{y}</b><br>Probabilidad: %{x:.1f}%<extra></extra>'
))

fig4.update_layout(
    title={
        'text': '🏆 Probabilidades de ser CAMPEÓN<br><sub>Champions League 2025-26 • 10,000 simulaciones Monte Carlo</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 24, 'color': 'white', 'family': 'Arial Black'}
    },
    xaxis_title='Probabilidad (%)',
    yaxis_title='',
    plot_bgcolor='#1e1e2e',
    paper_bgcolor='#1e1e2e',
    font=dict(size=13, color='white', family='Arial'),
    height=600,
    showlegend=False,
    xaxis=dict(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='rgba(255,255,255,0.1)',
        range=[0, top_10['Prob_Campeon'].max() + 5]
    ),
    annotations=[
        dict(
            x=1, y=-0.15,
            xref='paper', yref='paper',
            text='🟡 >20% Favoritos  🟠 15-20% Contendientes  🔵 10-15% Outsiders  🟣 5-10% Dark Horses',
            showarrow=False,
            font=dict(size=11, color='white')
        )
    ]
)

fig4.show()
fig4.write_html('../visualizations/probabilidades_v4_tier.html')
print("✅ Versión 4 guardada: tier colors")

print("\n" + "="*60)
print("✅ 4 VERSIONES CREADAS:")
print("   1. Viridis (profesional)")
print("   2. Sunset (cálido)")
print("   3. Turbo (vibrante)")
print("   4. Tier Colors (por categorías)")
print("\nAbre los HTML y elige tu favorito 🎨")
print("="*60)
