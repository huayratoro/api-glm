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

# # Example usage
# N = 10
# colors = generate_red_gradient(N)
# print(colors)

import glob
import matplotlib.pyplot as plt
import xarray as xr

list_files = sorted(glob.glob("downloads/"))
# listac olores

for f in list_files[:3]:
    
    df = xr.open_dataset(f)

    f, ax = plt.subplots()

    ax.scatter(
        df["event_lon"].values,
        df["event_lon"].values
    )