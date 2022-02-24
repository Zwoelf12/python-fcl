import fcl
import numpy as np

def print_distance_result(o1_name, o2_name, result):
    print('Distance between {} and {}:'.format(o1_name, o2_name))
    print('-'*30)
    print('Distance: {}'.format(result.min_distance))
    print('Closest Points:')
    print(result.nearest_points[0])
    print(result.nearest_points[1])
    print('')

# set up geometry and transformations
pos_box = np.array([1.3,0.1,0])
Shape_box = np.array([2,2,2])
quat_box = np.array([1, 0, 0, 0])

pos_sph = np.array([0,0,0])
Shape_sph = np.array([0.5])
quat_sph = np.array([1, 0, 0, 0])

box = fcl.CollisionObject(fcl.Box(Shape_box[0], Shape_box[1], Shape_box[2]),fcl.Transform(quat_box,pos_box))
sph = fcl.CollisionObject(fcl.Sphere(Shape_sph[0]),fcl.Transform(quat_sph,pos_sph))

# enable signed distances for correct calculation of the nearest points
req = fcl.DistanceRequest(enable_nearest_points=True, enable_signed_distance=True)
res = fcl.DistanceResult()

dist = fcl.distance(sph, box, req, res)
print_distance_result('sphere', 'box', res)

