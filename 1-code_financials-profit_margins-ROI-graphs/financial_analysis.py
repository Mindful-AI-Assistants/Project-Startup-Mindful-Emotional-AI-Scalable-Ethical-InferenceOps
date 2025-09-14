
import matplotlib.pyplot as plt
import numpy as np
import os

# Financial data (USD)
years = np.array([1,2,3])
revenue = np.array([3_000_000, 8_000_000, 15_750_000])
costs = np.array([900_000, 1_500_000, 2_300_000])
profit = revenue - costs

profit_margin = profit / revenue * 100
roi = (profit) / costs * 100

print("Financial Analysis")
for i,y in enumerate(years):
    print(f"Year {y}: Revenue=${revenue[i]:,.0f} | Costs=${costs[i]:,.0f} | Profit=${profit[i]:,.0f} | Margin={profit_margin[i]:.2f}% | ROI={roi[i]:.2f}%")

# Save profit margin plot (dark turquoise theme)
os.makedirs("assets/diagrams", exist_ok=True)
bg_color = "#0b1a1f"
panel_color = "#081018"
accent = "#2ee6d6"
text_color = "#e6f7f6"

plt.figure(figsize=(8,4))
fig = plt.gcf(); fig.patch.set_facecolor(bg_color)
ax = plt.gca(); ax.set_facecolor(panel_color)
ax.plot(years, profit_margin, marker='o', color=accent, linewidth=2.5)
ax.set_title("Profit Margin (%)", color=text_color)
ax.set_xlabel("Year", color=text_color); ax.set_ylabel("%", color=text_color)
ax.tick_params(colors=text_color)
ax.grid(True, linestyle='--', color='#073239', alpha=0.6)
plt.tight_layout()
plt.savefig("assets/diagrams/profit_margin_dark_turquoise.png", dpi=180, facecolor=fig.get_facecolor())
plt.close()
