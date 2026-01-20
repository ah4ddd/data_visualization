import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(16, 10))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# ============ SKY - Light cyan/turquoise ============
sky = patches.Rectangle((0, 0), 100, 100, color='#5dbadb', ec='none')
ax.add_patch(sky)

# ============ CLOUDS - Long horizontal streaks BEHIND mountain ============
def draw_wispy_cloud(x, y, length, thickness):
    # Multiple overlapping ellipses for wispy effect
    num_segments = 8
    for i in range(num_segments):
        x_pos = x + i * (length / num_segments) * 0.8
        width = length / num_segments * 1.5
        alpha = 0.7 if i % 2 == 0 else 0.5
        ax.add_patch(patches.Ellipse((x_pos, y), width, thickness,
                                    color='white', ec='none', alpha=alpha))

# Top left wispy cloud
draw_wispy_cloud(8, 92, 25, 1.2)

# Top middle wispy cloud
draw_wispy_cloud(52, 94, 20, 1)

# Right side clouds - more puffy
cloud_right_centers = [(72, 88), (80, 89), (88, 87.5)]
for cx, cy in cloud_right_centers:
    for dx, dy, w, h in [(-1.5, 0, 3, 2.5), (0, 0.5, 3.5, 2.8), (1.5, 0, 3, 2.5)]:
        ax.add_patch(patches.Ellipse((cx+dx, cy+dy), w, h,
                                    color='white', ec='none', alpha=0.9))

# Bottom left puffy clouds
cloud_left_centers = [(18, 85), (25, 86), (32, 85.5)]
for cx, cy in cloud_left_centers:
    for dx, dy, w, h in [(-1.2, 0, 2.5, 2), (0, 0.3, 2.8, 2.3), (1.2, 0, 2.5, 2)]:
        ax.add_patch(patches.Ellipse((cx+dx, cy+dy), w, h,
                                    color='white', ec='none', alpha=0.9))

# ============ MOUNTAIN - ONE big central mountain ============
# Large dominant mountain - smooth and simple
mountain = Polygon([
    (0, 35), (10, 38), (20, 42), (25, 48), (30, 54), (35, 62),
    (40, 70), (43, 76), (46, 82), (48, 86), (50, 88),  # Peak
    (52, 86), (54, 82), (57, 76), (60, 70), (65, 62),
    (70, 54), (75, 48), (80, 42), (90, 38), (100, 35),
    (100, 0), (0, 0)
], color='#d4e6ef', ec='none', zorder=5)
ax.add_patch(mountain)

# Snow cap on peak - bright white
snow_cap = Polygon([
    (40, 70), (43, 76), (46, 82), (48, 86), (50, 88),
    (52, 86), (54, 82), (57, 76), (60, 70),
    (55, 74), (50, 78), (45, 74)
], color='white', ec='none', alpha=1, zorder=6)
ax.add_patch(snow_cap)

# Left shoulder snow
left_snow = Polygon([
    (30, 54), (33, 60), (35, 62), (40, 70),
    (37, 65), (34, 58), (31, 55)
], color='white', ec='none', alpha=0.95, zorder=6)
ax.add_patch(left_snow)

# Right shoulder snow
right_snow = Polygon([
    (60, 70), (65, 62), (68, 58), (70, 54),
    (67, 57), (64, 63), (61, 68)
], color='white', ec='none', alpha=0.95, zorder=6)
ax.add_patch(right_snow)

# Mountain shadow for depth
shadow = Polygon([
    (48, 86), (50, 88), (52, 86), (51, 86)
], color='#c0d8e5', ec='none', alpha=0.6, zorder=6)
ax.add_patch(shadow)

# ============ FOREST - Dense dark silhouette ============
# Background forest layer
forest_back = Polygon([
    (0, 30), (20, 34), (40, 32), (60, 33), (80, 31), (100, 32),
    (100, 0), (0, 0)
], color='#2d4f3c', ec='none', zorder=7)
ax.add_patch(forest_back)

# Middle forest layer
forest_mid = Polygon([
    (0, 25), (25, 28), (50, 26), (75, 27), (100, 26),
    (100, 0), (0, 0)
], color='#234433', ec='none', zorder=8)
ax.add_patch(forest_mid)

# Front forest base
forest_front = patches.Rectangle((0, 0), 100, 22, color='#1a3328', ec='none', zorder=9)
ax.add_patch(forest_front)

# Pine trees - LOTS of them for dense forest
def draw_pine(x, y, h, color, zorder=10):
    # Trunk
    trunk_w = h * 0.06
    ax.add_patch(patches.Rectangle((x-trunk_w/2, y), trunk_w, h*0.2,
                                   color='#2a1810', ec='none', zorder=zorder))
    # Pine triangles - 3 layers
    for i in range(3):
        th = h * 0.35
        tw = h * 0.35 * (1 - i*0.15)
        yp = y + h*0.15 + i*h*0.22
        tri = Polygon([(x, yp+th), (x-tw, yp), (x+tw, yp)],
                     color=color, ec='none', zorder=zorder)
        ax.add_patch(tri)

# Background trees
for x in np.linspace(2, 98, 50):
    y = 28 + np.sin(x*0.5) * 2
    h = 4.5 + np.random.rand() * 1.5
    draw_pine(x, y, h, '#2d4f3c', zorder=10)

# Middle trees
for x in np.linspace(1, 99, 55):
    y = 22 + np.sin(x*0.4) * 1.5
    h = 5 + np.random.rand() * 2
    draw_pine(x, y, h, '#234433', zorder=11)

# Front trees - darkest and most visible
for x in np.linspace(0.5, 99.5, 60):
    y = 17
    h = 6 + np.random.rand() * 2.5
    draw_pine(x, y, h, '#1a3328', zorder=12)

# ============ WATER - Bright blue with reflections ============
water = patches.Rectangle((0, 6), 100, 11, color='#4b9ec8', ec='none', zorder=13)
ax.add_patch(water)

# Tree reflections - inverted pines in water
reflection_positions = np.linspace(5, 95, 40)
for x in reflection_positions:
    # Inverted triangle reflections
    y_start = 16.5
    for i in range(3):
        width = 1.2 - i * 0.3
        height = 2.5
        y_base = y_start - i * 1.8
        reflection = Polygon([
            (x, y_base),
            (x - width, y_base - height),
            (x + width, y_base - height)
        ], color='#1a3328', ec='none', alpha=0.5 + np.random.rand()*0.2, zorder=14)
        ax.add_patch(reflection)

# Water ripples - white highlights
for i in range(100):
    x = np.random.rand() * 100
    y = 6 + np.random.rand() * 11
    w = 0.8 + np.random.rand() * 2.5
    h = 0.15 + np.random.rand() * 0.25
    alpha = 0.3 + np.random.rand() * 0.4
    ax.add_patch(patches.Ellipse((x, y), w, h,
                                color='white', ec='none', alpha=alpha, zorder=15))

# Darker water patches for depth
for i in range(60):
    x = np.random.rand() * 100
    y = 6 + np.random.rand() * 11
    w = 1 + np.random.rand() * 2
    ax.add_patch(patches.Rectangle((x, y), w, 0.5,
                                   color='#3a7ea8', ec='none', alpha=0.4, zorder=14))

# ============ FOREGROUND GRASS ============
grass = patches.Rectangle((0, 0), 100, 6, color='#7fa858', ec='none', zorder=16)
ax.add_patch(grass)

# Grass blades at water edge - yellowish green
for x in np.linspace(1, 40, 150):
    for offset in [0, 0.25, 0.5]:
        bx = x + offset + np.random.rand() * 0.3
        by = 6
        h = 1.5 + np.random.rand() * 2
        curve = bx + (np.random.rand() - 0.5) * 0.6
        ax.plot([bx, curve], [by, by + h],
               color='#92b05c', linewidth=1.3, alpha=0.75, zorder=17)

# Lower grass detail
for x in np.linspace(0, 100, 200):
    bx = x + np.random.rand() * 0.4
    h = np.random.rand() * 2.5
    ax.plot([bx, bx + (np.random.rand()-0.5)*0.4], [0, h],
           color='#6a8e48', linewidth=0.9, alpha=0.6, zorder=16)

plt.tight_layout()
plt.savefig('mountain_lake_scenery.png', dpi=300, bbox_inches='tight',
            facecolor='#5dbadb', pad_inches=0)
plt.show()
