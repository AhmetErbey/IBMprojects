import math
# Öklid mesafesini hesaplanması
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

#liste kısmı

points = [(1, 2), (9, 4), (5, 32), (43, 67), (7, 40)]

distances = []

for i in range(len(points)):
    for k in range(i + 1, len(points)): 
        distance = euclideanDistance(points[i], points[k])
        distances.append(distance)

# Minimum mesafe
min_distance = min(distances)

# Sonuçlar
print(f"Her iki nokta çifti arasindaki tüm mesafeler: {distances}")
print(f"Minimum mesafe: {min_distance:.2f}")


