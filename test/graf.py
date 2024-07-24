def generate_red_gradient(N):
    """
    Generate a list of colors in hexadecimal format corresponding to a gradient from red to black.
    
    Parameters:
    N (int): The number of colors in the gradient.
    
    Returns:
    List[str]: A list of hexadecimal color strings.
    """
    if N <= 0:
        return []

    gradient = []
    for i in range(N):
        # Calculate the intensity of the red color
        intensity = int(255 * (1 - i / (N - 1))) if N > 1 else 255
        # Format the color as a hexadecimal string
        hex_color = f'#{intensity:02X}0000'
        gradient.append(hex_color)
    
    return gradient

import glob
import matplotlib.pyplot as plt
import xarray as xr

N = 5
list_files = sorted(glob.glob("downloads/*.nc"))[:N]
# lista colores
colores = generate_red_gradient(len(list_files))

f, ax = plt.subplots()

i = 0
for f in list_files:
    
    df = xr.open_dataset(f)

    ax.scatter(
        df["event_lon"].values,
        df["event_lat"].values,
        color = colores[i], marker = "+"
    )
    i = i + 1

ax.set_xlim(-69, -60)
ax.set_ylim(-26, -20)

plt.savefig("assets/test.png")
plt.close()