from point import Point
from nelder_mead import nelder_mead


def sphere(p: Point) -> float:
    return p.x**2 + p.y**2


def rosenbrock(p: Point) -> float:
    return (1 - p.x) + 100*((p.y-(p.x*p.x))*(p.y-(p.x*p.x)))


def example(p: Point) -> float:
    return p.x**2 - 4*p.x + p.y**2 - p.y - p.x*p.y


sphere_result = nelder_mead(sphere)
rosenbrock_result = nelder_mead(rosenbrock)
example_result = nelder_mead(
    f=example, alpha=1.0, rho=1.0, gamma=1.0, sigma=1.0)

print(f"Sphere: {sphere_result}")
print(f"Rosenbrock: {rosenbrock_result}")
print(f"Example: {example_result}")
