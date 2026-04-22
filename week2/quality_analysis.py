import matplotlib.pyplot as plt
import numpy as np

# Quality characteristics
categories = [
    'Functional Suitability',
    'Performance Efficiency',
    'Compatibility',
    'Usability',
    'Reliability',
    'Security',
    'Maintainability',
    'Portability'
]

# Replace with your actual scores
google_maps_scores = [5, 4, 5, 4, 4, 3, 4, 5]
apple_maps_scores = [4, 4, 3, 5, 4, 4, 3, 3]

# Number of variables
N = len(categories)

# Angles for radar
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

# Close the circle
google_maps_scores += google_maps_scores[:1]
apple_maps_scores += apple_maps_scores[:1]
angles += angles[:1]

# Create figure
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Plot Google Maps (Blue)
ax.plot(angles, google_maps_scores, linewidth=2, linestyle='solid', label='Google Maps', color='blue')
ax.fill(angles, google_maps_scores, alpha=0.2, color='blue')

# Plot Apple Maps (Red)
ax.plot(angles, apple_maps_scores, linewidth=2, linestyle='solid', label='Apple Maps', color='red')
ax.fill(angles, apple_maps_scores, alpha=0.2, color='red')

# Labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Title
plt.title("Quality Profile Radar Chart", size=14)

# Legend (Infographic Box)
legend = plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Add extra infographic text box
info_text = (
    "Blue  → Google Maps\n"
    "Red   → Apple Maps\n\n"
    "Scale: 1 (Poor) to 5 (Excellent)"
)

plt.gcf().text(0.02, 0.02, info_text, fontsize=10,
               bbox=dict(facecolor='lightgray', alpha=0.5))

# Show chart
plt.show()