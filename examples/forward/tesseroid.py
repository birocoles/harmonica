"""
Tesseroid Forward Modelling
===========================

Computing the gravitational fields generated by regional or global scale structures
require to take into account the curvature of the Earth. One common approach is to use
spherical prisms also known as tesseroids. We will compute the radial component of the
gravitational acceleration generated by a single tesseroid on a computation grid through
the :func:`harmonica.tesseroid_gravity` function.
"""
import harmonica as hm
import verde as vd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


# Get default ellipsoid (WGS84) to obtain the mean Earth radius
ellipsoid = hm.get_ellipsoid()

# Define tesseroid with top surface at the mean Earth radius, thickness of 10km
# (bottom = top - thickness) and density of 2670kg/m^3
tesseroid = [-70, -50, -40, -20, ellipsoid.mean_radius - 10e3, ellipsoid.mean_radius]
density = 2670

# Define computation points on a regular grid at 100km above the mean Earth radius
coordinates = vd.grid_coordinates(region=[-80, -40, -50, -10], shape=(80, 80),
                                  extra_coords=100e3 + ellipsoid.mean_radius)

# Compute the radial component of the acceleration
gravity = hm.tesseroid_gravity(coordinates, tesseroid, density, field="g_r")
print(gravity)

# Plot the gravitational field
fig = plt.figure(figsize=(8, 9))
ax = plt.axes(projection=ccrs.Orthographic(central_longitude=-60))
img = ax.pcolormesh(*coordinates[:2], gravity, transform=ccrs.PlateCarree())
plt.colorbar(
    img, ax=ax, pad=0, aspect=50, orientation="horizontal", label="mGal",
)
ax.coastlines()
ax.set_title("Radial component of gravitational acceleration")
plt.show()