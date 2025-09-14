
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('assets/diagrams', exist_ok=True)

years = np.array([1,2,3])
revenue = np.array([3_000_000, 8_000_000, 15_750_000])
costs = np.array([900_000, 1_500_000, 2_300_000])
profit = revenue - costs

bg_color = '#0b1a1f'; panel_color = '#081018'
accent_turquoise = '#2ee6d6'; accent_teal = '#00b3a6'; text_color = '#e6f7f6'

# revenue vs costs
plt.figure(figsize=(8,5))
fig = plt.gcf(); fig.patch.set_facecolor(bg_color)
ax = plt.gca(); ax.set_facecolor(panel_color)
ax.plot(years, revenue/1e6, marker='o', linewidth=2.5, color=accent_turquoise, label='Revenue (M USD)')
ax.plot(years, costs/1e6, marker='o', linewidth=2.5, color=accent_teal, label='Costs (M USD)')
ax.set_title('Projected Revenue vs Costs (3 Years)', color=text_color)
ax.set_xlabel('Year', color=text_color); ax.set_ylabel('USD (millions)', color=text_color)
ax.set_xticks(years); ax.tick_params(colors=text_color)
ax.grid(True, color='#073239', linestyle='--', alpha=0.7)
ax.legend(facecolor=panel_color, edgecolor='#13393a', labelcolor=text_color)
plt.tight_layout()
plt.savefig('assets/diagrams/revenue_vs_costs_dark_turquoise.png', dpi=180, facecolor=fig.get_facecolor())
plt.close()

# profit bar
plt.figure(figsize=(8,5))
fig = plt.gcf(); fig.patch.set_facecolor(bg_color)
ax = plt.gca(); ax.set_facecolor(panel_color)
bars = ax.bar(years, profit/1e6, color=[accent_turquoise, accent_teal, accent_turquoise], edgecolor='#0f3b3b', linewidth=0.8)
ax.set_title('Projected Net Profit (3 Years)', color=text_color)
ax.set_xlabel('Year', color=text_color); ax.set_ylabel('Net Profit (M USD)', color=text_color)
ax.set_xticks(years); ax.tick_params(colors=text_color)
ax.grid(axis='y', color='#073239', linestyle='--', linewidth=0.5, alpha=0.6)
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + 0.05, f"{h:.2f}", ha='center', va='bottom', color=text_color, fontsize=10)
plt.tight_layout()
plt.savefig('assets/diagrams/profit_dark_turquoise.png', dpi=180, facecolor=fig.get_facecolor())
plt.close()
